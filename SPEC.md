# SPEC — LeetCode Notes Site

> Static site that publishes my LeetCode notes from a Notion database to
> `https://chaoting.tw/leetcode/`. Notion is the single source of authoring;
> Markdown and HTML are disposable build artifacts.

---

## 1. Objective

Turn a Notion database (`LeetCode - Problems`) into a published, public-facing
notes site without manually copying content.

- **Pipeline:** `Notion data source → generated_docs/ (Markdown) → MkDocs → site/ (HTML) → GitHub Pages`.
- **Authoring stays in Notion.** No Markdown is hand-written or committed.
- **Target users:** public portfolio — readable by interviewers / peers, indexed
  by search engines (SEO and sitemap are explicit v2 goals).
- **Deploy targets:**
  - Site root → `https://chaoting.tw/leetcode/`
  - Problems index → `https://chaoting.tw/leetcode/problems/`
  - Per problem → `https://chaoting.tw/leetcode/problems/0001-two-sum/`
  - Patterns (v2) → `https://chaoting.tw/leetcode/patterns/`

### Publish gate (v1)

A problem is published only when **both** hold:

1. `進度 (進度/Progress) == Done`, and
2. it has real note content — page body blocks, or a non-empty `筆記` property
   as fallback.

Pages that are `Todo`, `ToNote`, empty, or metadata-only are skipped.

---

## 2. Commands

Run from the project root (`leetcode/`).

| Command | Purpose |
|---|---|
| `python -m venv .venv && source .venv/bin/activate` | Create / enter the virtualenv |
| `pip install -r requirements.txt` | Install deps (mkdocs, notion-client, python-dotenv, python-slugify) |
| `cp .env.example .env` then edit | Provide `NOTION_TOKEN` locally |
| `python scripts/build_site_from_notion.py` | Fetch from Notion → write `generated_docs/` |
| `mkdocs build` | Render `generated_docs/` → `site/` |
| `mkdocs serve` → http://127.0.0.1:8000 | Local preview |

### Environment variables

| Var | Required | Default | Meaning |
|---|---|---|---|
| `NOTION_TOKEN` | yes | — | Internal integration token (local `.env` / CI secret only) |
| `NOTION_DATA_SOURCE_ID` | preferred | — | Notion 2025-09-03 data source id |
| `NOTION_DATABASE_ID` | fallback | — | Used when no data source id is set |
| `SITE_URL` | no | `https://chaoting.tw/leetcode/` | Public base URL |
| `NOTION_MAX_WORKERS` | no | `8` | Concurrent page fetches |
| `NOTION_SAVE_EVERY` | no | `5` | Flush the edit-time index every N processed pages |
| `NOTION_NO_CACHE` | no | (off) | Set `1` to force a full re-fetch |
| `NOTION_NO_PRUNE` | no | (off) | Set `1` to disable removing unpublished pages |

---

## 3. Project structure

```
leetcode/
├── SPEC.md                          # this file
├── .gitignore
├── .env.example                     # template; real .env is gitignored
├── requirements.txt
├── mkdocs.yml                       # site_url=/leetcode/, use_directory_urls, nav
├── scripts/
│   └── build_site_from_notion.py    # Notion → generated_docs/ builder
├── .github/workflows/
│   └── pages.yml                    # Notion → MkDocs → Pages (with cache step)
│
│  # ---- build artifacts, all gitignored, never committed ----
├── generated_docs/                  # Markdown produced from Notion (source of truth for content)
│   ├── index.md
│   ├── problems/
│   │   ├── index.md                 # table of all published problems
│   │   └── 0001-two-sum/index.md    # one dir per problem
│   └── patterns/index.md            # "Coming soon" placeholder (v2)
├── site/                            # MkDocs HTML output
└── .notion_cache.json               # edit-time index: {page_id: last_edited_time}
```

### Key architectural decisions

- **`generated_docs/` is the source of truth for content.** Notes are written
  straight to disk; the build never re-derives content from the cache.
- **`.notion_cache.json` stores only `{page_id: last_edited_time}`.** Its sole
  job is deciding what to re-fetch. It is never deleted at the start of a run.
- **Incremental & crash-safe:** changed pages are fetched concurrently; the
  edit-time index is flushed every `NOTION_SAVE_EVERY` pages and in a `finally`
  block; writes are atomic (temp file + rename). An interrupted run keeps both
  written files and progress markers, then resumes on the next run.
- **Pruning at end of a successful, non-empty run:** problems removed from the
  query (deleted / progress ≠ Done / renamed slug) have their dirs removed.
- **Slugs are stable and zero-padded:** `1. Two Sum` / `0001 Two Sum` /
  `0001. Two Sum` → `0001-two-sum`. Titles without a number get a warning.
- **Subpath-safe links:** all generated links are relative so they resolve under
  `/leetcode/` (never absolute `/problems/...`).

---

## 4. Code style

- **Python 3.12**, standard library + the four pinned deps. No framework.
- Match the existing `scripts/build_site_from_notion.py` conventions:
  - Small pure helpers for Notion property extraction (`get_select`, `get_multi`, …).
  - Block→Markdown rendering kept as pure functions where possible; network calls
    isolated and wrapped in `with_retry` (429 / 5xx backoff, honors `Retry-After`).
  - English comments, concise; explain *why*, not *what*.
  - Constants (column names, publish value, cache config) grouped near the top.
- **Notion column names live in one place** (the `COL_*` constants). Chinese
  column names are referenced only through those constants.
- Per-page heading + metadata format (one bullet per non-empty field):

  ```markdown
  # 0001. Two Sum

  - Difficulty: Easy
  - Tags: Array, Hash Table
  - Source: Grind 169
  - Proficiency: Struggle
  - Blockers: Edge Case, 想不到
  - Attempts: 2
  - Date: 2026-06-21
  - LeetCode: https://leetcode.com/problems/two-sum/

  ---

  ## Notes

  <Notion page body, or 筆記 fallback>
  ```

### Supported Notion block types (v1)

`paragraph`, `heading_1/2/3`, `bulleted_list_item`, `numbered_list_item`,
`to_do`, `code`, `quote`, `divider`, `table` (+ `table_row`).
`child_page` is silently skipped. Any other type emits a warning and a
`> Unsupported block type: X` placeholder — report it to add support.

---

## 5. Testing strategy

Lightweight verification (no committed test suite). Before pushing, confirm:

1. `python scripts/build_site_from_notion.py` runs clean against real Notion.
2. `mkdocs build` produces **zero** build/link warnings.
3. URL structure exists: `/`, `/problems/`, `/problems/0001-two-sum/`.
4. A problem page shows the Notion body (or `筆記` fallback) — **no** embedded
   `.cpp` / `.py` solution code.
5. No `Todo` / `ToNote` / empty pages were published.
6. `git status` shows none of: `.env`, `generated_docs/`, `site/`, `.notion_cache.json`.
7. Incremental behavior: a second run reports `0 to (re)fetch`; editing one
   Notion page re-fetches exactly one.

Ad-hoc verification uses a mock Notion client (in-memory pages/blocks) to check
slug rules, block→Markdown conversion, table rendering, cache hit/miss, prune,
and interruption survival. These checks are run on demand, not committed.

---

## 6. Boundaries

### Always

- Keep Notion as the only authoring surface; treat Markdown/HTML as disposable.
- Read secrets from the environment (`.env` locally, GitHub Secrets in CI).
- Log only the problem **title + slug** — never page body content.
- Generate relative links so the site works under the `/leetcode/` subpath.
- Keep `generated_docs/`, `site/`, `.notion_cache.json`, `.env` in `.gitignore`.

### Ask first

- Changing the publish gate (e.g. adding a `Published` checkbox, or `內容` /
  `UMPIRE`-based rules) beyond the current `進度 == Done` + has-notes.
- Storing anything beyond `last_edited_time` in `.notion_cache.json`
  (e.g. an `ok/skip` status flag) — it changes the trade-offs we discussed.
- Adding new committed dependencies or a test framework.
- Anything that would commit generated content or secrets to the repo.

### Never

- Commit the Notion token, generated Markdown, `site/`, or the cache.
- Put the Notion token in front-end JavaScript.
- Print full Notion page content in logs / GitHub Actions output.
- Read or embed the repo's `.cpp` / `.py` solution files into pages.
- Reproduce full LeetCode problem statements verbatim — only my own notes.
- Delete `generated_docs/` at the **start** of a run (breaks crash-safety).

---

## 7. v2 roadmap (Non-Goals for v1)

Explicitly out of scope for v1; planned for later:

1. `patterns/` section with real content (currently a placeholder).
2. Tag filtering and difficulty filtering.
3. Full-text search.
4. Richer Notion blocks: images, toggles, equations, callouts, Mermaid.
5. SEO metadata + `sitemap.xml`.
6. Custom theme / branding.
7. A `Published` flag in Notion to gate publishing explicitly (instead of
   inferring from `進度 == Done`).
