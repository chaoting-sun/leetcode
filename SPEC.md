# SPEC — LeetCode Notes Site (v2)

> Static site that publishes my LeetCode notes from a Notion database to
> `https://chaoting.tw/leetcode/`. Notion is the single source of authoring;
> Markdown and HTML are disposable build artifacts.
>
> **v2 scope (this revision):** client-side tag + difficulty filtering on the
> Problems page, full-text search over note content (Material built-in), and
> SEO metadata (`<meta description>`, canonical, Open Graph, Twitter Card) plus
> an auto-generated `sitemap.xml`.

---

## 1. Objective

Turn a Notion database (`LeetCode - Problems`) into a published, public-facing
notes site without manually copying content.

- **Pipeline:** `Notion data source → generated_docs/ (Markdown) → MkDocs (Material) → site/ (HTML) → GitHub Pages`.
- **Authoring stays in Notion.** No Markdown is hand-written or committed.
- **Target users:** public portfolio — readable by interviewers / peers, indexed
  by search engines (SEO + sitemap are now in scope).
- **Deploy targets:**
  - Site root → `https://chaoting.tw/leetcode/`
  - Problems index → `https://chaoting.tw/leetcode/problems/`
  - Per problem → `https://chaoting.tw/leetcode/problems/0001-two-sum/`
  - Patterns (later) → `https://chaoting.tw/leetcode/patterns/`

### Publish gate

A problem is published only when **both** hold:

1. `進度 (Progress) == Done`, and
2. it has real note content — page body blocks, or a non-empty `筆記` property
   as fallback.

Pages that are `Todo`, `ToNote`, empty, or metadata-only are skipped.

### v2 feature goals & acceptance criteria

**F1 — Tag + difficulty filtering (client-side, Problems page).**
- A filter toolbar sits above the Problems table: tag chips (multi-select),
  a difficulty dropdown (All / Easy / Medium / Hard), and a title search box.
- Selecting filters hides/shows table rows instantly, fully client-side, no page
  reload and no backend.
- Multiple selections combine with **AND** across dimensions (tags ∧ difficulty
  ∧ title text); multiple tag chips combine with **AND** (a row must carry all
  selected tags). A visible count ("showing N of M") updates live.
- Works under Material's `navigation.instant` (SPA-style nav): the filter
  re-initializes after instant page loads (subscribe to Material's `document$`).
- **Accept:** load `/problems/`, click a tag chip → only matching rows remain;
  add a difficulty → result is the AND; type in the search box → further
  narrows; clearing all restores the full table. Filtering survives navigating
  away and back via instant nav.

**F2 — Full-text search over note content (Material built-in).**
- The global search (top-right) returns matches from problem **note bodies**, not
  just titles. CJK (Chinese) note text is tokenized so Chinese queries work.
- **Accept:** searching a distinctive phrase that appears only inside one
  problem's notes surfaces that problem; a Chinese term in the notes is findable.
- This is mostly already provided by the Material `search` plugin; v2 work is
  verification and tuning the tokenizer separator, not new code.

**F3 — SEO metadata + sitemap.**
- Every problem page emits: `<title>`, `<meta name="description">`,
  `<link rel="canonical">` (absolute, under `/leetcode/`), and Open Graph +
  Twitter Card tags (`og:title`, `og:description`, `og:url`, `og:type`,
  `twitter:card`, `twitter:title`, `twitter:description`).
- `description` / `og:description` is **auto-derived from the first ~155
  characters of the note body** (Markdown stripped, whitespace collapsed,
  truncated at a word/character boundary).
- `sitemap.xml` is produced at the site root with absolute URLs for all pages.
- **Accept:** view-source on a problem page shows all the above tags with the
  correct absolute URL; `site/sitemap.xml` exists and lists the problem URLs;
  pasting a problem URL into a social/link-preview validator shows title +
  description.
- **Out of scope for v2:** auto-generated social preview *images* (Material
  `social` plugin) — would add `libcairo`/`pango` system deps in CI. Tracked as
  a future upgrade; the meta tags above are added via a lightweight template
  override instead.

**F4 — Per-page note layout (metadata + TOC headings).**
- **Metadata block shows only three fields:** Difficulty, Tags, and the LeetCode
  URL. Source / Proficiency / Blockers / Attempts / Date are no longer rendered
  on the page (they remain available in Notion and in the Problems index).
- **One H1 per page = the problem title.** The `## Notes` wrapper heading is
  removed, and the note body's own Notion headings are demoted one level
  (`heading_1 → ##`, `heading_2 → ###`, `heading_3 → ####`) so the sidebar TOC
  nests the note's headings under the page instead of showing a single "Notes"
  entry. Keeping exactly one `<h1>` also supports F3 (SEO correctness).
- **Accept:** a problem whose Notion notes contain multiple headings shows those
  headings in the sidebar TOC as a clickable, correctly nested hierarchy; the
  rendered page has exactly one `<h1>` (the title); the metadata block lists only
  Difficulty, Tags, and LeetCode.

---

## 2. Commands

Run from the project root (`leetcode/`).

| Command | Purpose |
|---|---|
| `python -m venv .venv && source .venv/bin/activate` | Create / enter the virtualenv |
| `pip install -r requirements.txt` | Install deps (mkdocs, mkdocs-material, notion-client, python-dotenv, python-slugify) |
| `cp .env.example .env` then edit | Provide `NOTION_TOKEN` locally |
| `python scripts/build_site_from_notion.py` | Fetch from Notion → write `generated_docs/` (with SEO front-matter) |
| `mkdocs build` | Render `generated_docs/` → `site/` (filtering JS, SEO meta, sitemap) |
| `mkdocs serve` → http://127.0.0.1:8000 | Local preview |

### Environment variables

| Var | Required | Default | Meaning |
|---|---|---|---|
| `NOTION_TOKEN` | yes | — | Internal integration token (local `.env` / CI secret only) |
| `NOTION_DATA_SOURCE_ID` | preferred | — | Notion 2025-09-03 data source id |
| `NOTION_DATABASE_ID` | fallback | — | Used when no data source id is set |
| `SITE_URL` | no | `https://chaoting.tw/leetcode/` | Public base URL — drives canonical + sitemap |
| `NOTION_MAX_WORKERS` | no | `8` | Concurrent page fetches |
| `NOTION_SAVE_EVERY` | no | `5` | Flush the edit-time index every N processed pages |
| `NOTION_NO_CACHE` | no | (off) | Set `1` to force a full re-fetch |
| `NOTION_NO_PRUNE` | no | (off) | Set `1` to disable removing unpublished pages |

> **v2 deploy note:** bump `CACHE_VERSION` in `scripts/notionmd/config.py` when
> shipping v2, so every page is re-fetched and re-emitted with the new SEO
> front-matter (the edit-time cache otherwise skips unchanged pages).

---

## 3. Project structure

```
leetcode/
├── SPEC.md                          # this file
├── .gitignore
├── .env.example                     # template; real .env is gitignored
├── requirements.txt                 # mkdocs, mkdocs-material, notion-client, python-dotenv, python-slugify
├── mkdocs.yml                       # Material theme, site_url, search, extra_css/js, nav
├── scripts/
│   ├── build_site_from_notion.py    # orchestration: Notion → generated_docs/
│   └── notionmd/
│       ├── config.py                # paths, COL_* names, knobs, CACHE_VERSION
│       ├── client.py                # Notion I/O, rate limiter, retries, queries
│       ├── convert.py               # blocks→Markdown, SEO front-matter, index table
│       └── cache.py                 # {page_id: last_edited_time} edit-time index
├── overrides/                       # committed theme assets (custom_dir), NOT regenerated
│   ├── main.html                    # extends base.html; injects OG/Twitter meta (F3)
│   ├── javascripts/
│   │   └── filter.js                # client-side tag/difficulty/title filter (F1)
│   └── stylesheets/
│       └── extra.css                # toolbar/chip styling + site tweaks
├── .github/workflows/
│   └── pages.yml                    # Notion → MkDocs → Pages (caches index + generated_docs)
│
│  # ---- build artifacts, all gitignored, never committed ----
├── generated_docs/                  # Markdown produced from Notion (source of truth for content)
│   ├── index.md
│   ├── problems/
│   │   ├── index.md                 # filter toolbar + HTML table with data-* attrs
│   │   └── 0001-two-sum/index.md    # one dir per problem (with SEO front-matter)
│   └── patterns/index.md            # placeholder
├── site/                            # MkDocs HTML output (+ sitemap.xml)
└── .notion_cache.json               # edit-time index: {page_id: last_edited_time}
```

### Key architectural decisions

- **`generated_docs/` is the source of truth for content.** Notes are written
  straight to disk; the build never re-derives content from the cache. Both
  `generated_docs/` and `.notion_cache.json` are cached **together** in CI so the
  edit-time index and the content folder never drift on ephemeral runners.
- **`.notion_cache.json` stores only `{page_id: last_edited_time}`.** Its sole
  job is deciding what to re-fetch. Never deleted at the start of a run. Bump
  `CACHE_VERSION` to force a full re-render when output format changes (e.g. v2
  front-matter).
- **Filtering is 100% client-side.** The build emits the data; the browser does
  the filtering. No server, no backend, no extra build-time pages per tag. The
  Problems index is emitted as an **HTML table** so each `<tr>` can carry
  `data-tags="array hash-table"` and `data-difficulty="easy"`; tag chips are
  derived by JS from the union of row tags (single source of truth = the rows).
- **SEO meta lives in two places:** per-page `description` is emitted as YAML
  **front-matter** by the build script (Material renders it into
  `<meta name="description">` and `og:description`); the OG/Twitter tag block and
  `og:url`/`og:type` come from a `overrides/main.html` template override. Canonical
  and `sitemap.xml` are produced by Material/MkDocs from `site_url`.
- **Subpath-safe everywhere:** all generated links are relative so they resolve
  under `/leetcode/`; canonical/OG URLs are absolute and built from `SITE_URL`.
- **Incremental & crash-safe** (unchanged from v1): changed pages fetched
  concurrently; edit-time index flushed every `NOTION_SAVE_EVERY` pages and in a
  `finally` block; atomic writes; interrupted runs resume.
- **Pruning at end of a successful, non-empty run:** problems removed from the
  query (deleted / progress ≠ Done / renamed slug) have their dirs removed; the
  guard `and pages` means an empty query never wipes the site.

---

## 4. Code style

- **Python 3.12**, standard library + the five pinned deps. No web framework.
- Front-end: **vanilla JS** (no framework, no bundler) in `overrides/`. One small
  file per concern. CSS hand-written in `extra.css`.
- Match existing `scripts/notionmd/` conventions:
  - Small pure helpers for Notion property extraction (`get_select`, `get_multi`, …).
  - Block→Markdown rendering kept pure where possible; network calls isolated and
    wrapped in `with_retry` (429 / 5xx backoff, honors `Retry-After`).
  - English comments, concise; explain *why*, not *what*.
  - Constants (column names, publish value, cache config) grouped near the top.
- **Notion column names live in one place** (the `COL_*` constants). Chinese
  column names referenced only through those constants.

### Per-page Markdown format (v2 — front-matter + trimmed metadata + TOC headings)

Only Difficulty / Tags / LeetCode are rendered (F4). There is no `## Notes`
wrapper; the note body's headings are demoted one level so the page keeps a
single H1 and the TOC nests the note's own headings.

```markdown
---
description: "First ~155 chars of the notes, Markdown stripped, quotes escaped."
---
# 0001. Two Sum

- Difficulty: Easy
- Tags: Array, Hash Table
- LeetCode: https://leetcode.com/problems/two-sum/

---

<Notion page body. heading_1 → `##`, heading_2 → `###`, heading_3 → `####`,
so the title is the only `<h1>` and the sidebar TOC nests these headings.
Falls back to the 筆記 property when the page body is empty.>
```

### Problems index format (v2 — HTML table + toolbar)

- A filter toolbar (`<div class="lc-filter">…`) followed by an HTML `<table>` (or
  Markdown table wrapped so attributes survive) where each row carries
  `data-difficulty` (slug) and `data-tags` (space-separated tag slugs).
- Tag slugs reuse the existing `slugify` rules so they are stable and match the
  chip labels derived client-side.

### SEO description extraction

- Pure helper in `convert.py`: take rendered note text, strip Markdown syntax,
  collapse whitespace/newlines, truncate to ~155 chars at a word/character
  boundary, escape for safe YAML (`"`/`\`). Empty notes → no `description` key.

### Supported Notion block types

`paragraph`, `heading_1/2/3`, `bulleted_list_item`, `numbered_list_item`,
`to_do`, `code`, `quote`, `divider`, `table` (+ `table_row`). `child_page` is
silently skipped. Any other type emits a warning and a
`> Unsupported block type: X` placeholder — report it to add support.

---

## 5. Testing strategy

Lightweight verification (no committed test suite). Before pushing, confirm:

**Build & pipeline (unchanged):**
1. `python scripts/build_site_from_notion.py` runs clean against real Notion.
2. `mkdocs build` produces **zero** build/link warnings.
3. URL structure exists: `/`, `/problems/`, `/problems/0001-two-sum/`.
4. A problem page shows the Notion body (or `筆記` fallback) — **no** embedded
   `.cpp` / `.py` solution code.
5. No `Todo` / `ToNote` / empty pages were published.
6. `git status` shows none of: `.env`, `generated_docs/`, `site/`, `.notion_cache.json`.
7. Incremental: a second run reports `0 to (re)fetch`; editing one Notion page
   re-fetches exactly one (after the v2 `CACHE_VERSION` bump, the first run
   re-fetches everything once).

**F1 — Filtering:**
8. On `/problems/`, clicking a tag chip shows only rows with that tag; selecting
   a difficulty ANDs with it; typing in the search box ANDs further; clearing
   restores all rows; the "showing N of M" count tracks correctly.
9. After an instant-nav to a problem page and back, the filter still works
   (re-initialized via `document$`).

**F2 — Search:**
10. Searching a phrase that appears only in one problem's notes returns that
    problem; a Chinese term in notes is findable.

**F3 — SEO:**
11. View-source on a problem page contains `<meta name="description">`,
    `<link rel="canonical">` (absolute, `/leetcode/...`), and `og:title`,
    `og:description`, `og:url`, `og:type`, `twitter:card`.
12. `site/sitemap.xml` exists and lists absolute problem URLs.

**F4 — Per-page layout:**
13. The metadata block on a problem page lists only Difficulty, Tags, LeetCode.
14. A problem with multiple Notion headings shows them nested and clickable in
    the sidebar TOC; the page has exactly one `<h1>` and no "Notes" heading.

Ad-hoc unit checks use a mock Notion client (in-memory pages/blocks) for slug
rules, block→Markdown, table rendering, cache hit/miss, prune, interruption
survival, and the new `description` extraction helper. Run on demand, not committed.

---

## 6. Boundaries

### Always

- Keep Notion as the only authoring surface; treat Markdown/HTML as disposable.
- Read secrets from the environment (`.env` locally, GitHub Secrets in CI).
- Log only the problem **title + slug** — never page body content.
- Generate relative in-site links; build canonical/OG URLs as absolute from `SITE_URL`.
- Keep filtering, search, and SEO **fully static / client-side** — no backend, no
  runtime API calls from the browser.
- Keep `generated_docs/`, `site/`, `.notion_cache.json`, `.env` in `.gitignore`;
  keep `overrides/` committed.

### Ask first

- Changing the publish gate beyond `進度 == Done` + has-notes (e.g. a `Published`
  checkbox, or `內容` / `UMPIRE`-based rules).
- Adding a Notion column for SEO (e.g. a hand-written `摘要/Description`) — v2
  deliberately auto-derives description instead.
- Adding the Material `social` plugin (auto preview images) — it pulls in
  `libcairo`/`pango` system deps in CI.
- Storing anything beyond `last_edited_time` in `.notion_cache.json`.
- Adding new committed dependencies, a JS framework/bundler, or a test framework.
- Anything that would commit generated content or secrets to the repo.

### Never

- Commit the Notion token, generated Markdown, `site/`, or the cache.
- Put the Notion token in front-end JavaScript.
- Print full Notion page content in logs / GitHub Actions output.
- Read or embed the repo's `.cpp` / `.py` solution files into pages.
- Reproduce full LeetCode problem statements verbatim — only my own notes.
- Delete `generated_docs/` at the **start** of a run (breaks crash-safety).
- Introduce a server-side component for filtering/search (must stay static).

---

## 7. Later roadmap (out of scope for v2)

1. `patterns/` section with real content (currently a placeholder).
2. Auto-generated social **preview images** (Material `social` plugin + CI system deps).
3. Richer Notion blocks: images, toggles, equations, callouts, Mermaid.
4. JSON-LD structured data (schema.org `TechArticle` / `BreadcrumbList`).
5. A `Published` flag in Notion to gate publishing explicitly.
6. Per-tag / per-difficulty static landing pages (additional SEO surface), if the
   client-side filter proves insufficient for indexing.
```