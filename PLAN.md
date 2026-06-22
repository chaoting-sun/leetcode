# Implementation Plan: LeetCode Notes Site v2

> Companion to `SPEC.md` v2. Tasks are small and independently verifiable.
> Implement in order (Phase 1 → 4); run each task's Verification before the next.

## Overview

Add four features on top of the existing Notion → MkDocs (Material) pipeline:
F1 client-side tag/difficulty filtering, F2 full-text search verification,
F3 SEO metadata + sitemap, F4 per-page layout (trimmed metadata + TOC heading
demotion). Most changes live in `scripts/notionmd/convert.py` and `overrides/`.

## Architecture Decisions

- **F4 first** — smallest and most isolated (two functions in `convert.py`), and
  it reshapes the page structure that F3's description reads. Good foundation.
- **F1 data contract is produced by the build, consumed by JS** — the build
  pre-renders the toolbar (all tag chips + difficulty options) and an HTML table
  with `data-*` attributes; `filter.js` only wires events and toggles rows.
  Pre-rendering chips avoids FOUC and keeps the table readable without JS.
- **Bump `CACHE_VERSION`** — F3/F4 change per-page output, so the incremental
  cache must be invalidated once. Dev verification uses `NOTION_NO_CACHE=1`.
- **OG/Twitter via template override** — no social-image plugin (avoids
  `libcairo`/`pango` in CI), per SPEC decision.

## F1 data contract (shared by Task 5 ↔ 6)

```html
<div class="lc-filter">
  <div class="lc-chips">
    <button class="lc-chip" data-tag="array">Array</button> …
  </div>
  <select class="lc-diff">
    <option value="">All</option>
    <option value="easy">Easy</option> …
  </select>
  <input class="lc-search" placeholder="Filter by title…">
  <span class="lc-count"></span>
</div>
<table class="lc-table">
  …
  <tr data-difficulty="easy" data-tags="array hash-table"> … </tr>
</table>
```

- difficulty slug = lowercased difficulty (`easy`/`medium`/`hard`)
- tag slug = existing `slugify` rules, space-separated

---

## Task List

### Phase 1 — Per-page layout & data (build script)

#### Task 1 — F4: trim metadata + demote heading levels — ✅ DONE
**Description:** In `convert.py`: `build_page_markdown` renders only Difficulty /
Tags / LeetCode and drops the `## Notes` wrapper; `render_block` maps
`heading_1→##`, `heading_2→###`, `heading_3→####`.
**Acceptance:**
- [x] Page has exactly one `#` (the title); metadata block has 3 fields.
- [x] Notion body headings are demoted one level.
**Verification:**
- [x] `NOTION_NO_CACHE=1` full re-render (319 published); multi-heading page
      shows `##`/`###` body headings, 3-field metadata, no `## Notes`; every page
      has exactly one `# `.
- [x] `mkdocs build`; page HTML has one `<h1>` and the secondary TOC nav lists
      the nested note headings (no link/build warnings — only the unconditional
      Material "MkDocs 2.0" upstream notice).
**Dependencies:** None **| Files:** `scripts/notionmd/convert.py` **| Scope:** S

#### Task 2 — F3a: description extraction + front-matter
**Description:** Add a pure `make_description(body_md)` helper (strip Markdown,
collapse whitespace, truncate ~155 chars at a boundary, YAML-escape). Prepend
`---\ndescription: "…"\n---` to each page. Empty notes → no `description` key.
**Acceptance:**
- [ ] Each page `.md` starts with valid YAML front-matter; description ≤ ~155 chars.
- [ ] `mkdocs build` zero warnings; page emits `<meta name="description">`.
**Verification:**
- [ ] Inspect `.md` front-matter; `grep 'name="description"' site/problems/*/index.html`.
**Dependencies:** Task 1 **| Files:** `scripts/notionmd/convert.py` **| Scope:** S

#### Task 3 — bump CACHE_VERSION
**Description:** Increment `CACHE_VERSION` in `config.py` so the deploy re-fetches
and re-emits every page with the new format.
**Acceptance:**
- [ ] After the bump, one build re-fetches everything once; the next is incremental.
**Verification:**
- [ ] Run build twice: first re-fetches all, second reports `0 to (re)fetch`.
**Dependencies:** Task 1, 2 **| Files:** `scripts/notionmd/config.py` **| Scope:** XS

#### Checkpoint A (Tasks 1–3)
- [ ] `mkdocs build` zero warnings; single `<h1>`; nested TOC; 3-field metadata;
      every page has a description.

### Phase 2 — SEO template & sitemap

#### Task 4 — F3b: OG/Twitter template + canonical/sitemap verification
**Description:** Add `overrides/main.html` (extends `base.html`) injecting
`og:title/description/url/type` and `twitter:card/title/description` from
`page.meta.description` and `page.canonical_url`. Confirm `mkdocs.yml` `site_url`.
**Acceptance:**
- [ ] Problem page has all OG/Twitter tags + absolute `og:url`.
- [ ] `<link rel="canonical">` is absolute under `/leetcode/`.
- [ ] `site/sitemap.xml` lists absolute problem URLs.
**Verification:**
- [ ] view-source spot check; `grep problems site/sitemap.xml`.
**Dependencies:** Task 2 **| Files:** `overrides/main.html`, `mkdocs.yml` **| Scope:** S

### Phase 3 — Client-side filtering

#### Task 5 — F1a: Problems index emits toolbar + HTML table + data-*
**Description:** Change `write_problems_index` to emit the toolbar (pre-rendered
chips + difficulty options) and an HTML table with `data-difficulty`/`data-tags`
per row, following the F1 contract above.
**Acceptance:**
- [ ] `/problems/` contains `.lc-filter` and `data-*` rows.
- [ ] `mkdocs build` (with `md_in_html`) zero warnings; table keeps Material styling.
**Verification:**
- [ ] Inspect generated HTML; open `/problems/` in a browser.
**Dependencies:** Task 1 **| Files:** `scripts/notionmd/convert.py` **| Scope:** M

#### Task 6 — F1b: filter.js filtering logic
**Description:** Add `overrides/javascripts/filter.js`: multi-select tag chips
(AND), difficulty select, title search box (AND-combined), live row toggling,
"showing N of M" count; subscribe to Material `document$` for instant-nav.
**Acceptance:**
- [ ] Meets SPEC §5 items 8 & 9 (AND combos, clear restores, survives instant nav).
**Verification:**
- [ ] Manually exercise combinations on `/problems/` and instant-nav back and forth.
**Dependencies:** Task 5 **| Files:** `overrides/javascripts/filter.js`, `mkdocs.yml` **| Scope:** M

#### Task 7 — F1c: toolbar/chip styling
**Description:** Add toolbar, chip (incl. active state), and count styles to
`overrides/stylesheets/extra.css`; keep the light-only black/white look.
**Acceptance:**
- [ ] Chips/dropdown/search laid out cleanly; active state clear; wraps on narrow screens.
**Verification:**
- [ ] Visual check on desktop + narrow viewport.
**Dependencies:** Task 5 (do after 6) **| Files:** `overrides/stylesheets/extra.css` **| Scope:** S

#### Checkpoint B (Tasks 4–7)
- [ ] SEO tags complete; sitemap correct; `/problems/` filtering across four
      combinations + instant-nav all pass.

### Phase 4 — Search verification

#### Task 8 — F2: full-text search verification + CJK tuning
**Description:** Verify Material's built-in search finds note-body text; tune
`plugins.search.separator` (CJK) if needed. Mostly zero code.
**Acceptance:**
- [ ] Meets SPEC §5 item 10 (distinctive note phrase findable; Chinese term findable).
**Verification:**
- [ ] `mkdocs serve`; search an English phrase + a Chinese term from notes.
**Dependencies:** None (do last) **| Files:** `mkdocs.yml` (maybe) **| Scope:** S

#### Checkpoint C (Complete)
- [ ] All 14 SPEC §5 checks pass; `mkdocs build` zero warnings; `git status`
      free of forbidden artifacts.

---

## Risks and Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Raw HTML table loses Material table styling | Med | `class="lc-table"` + extra.css; or wrap via `md_in_html` so Material takes over |
| `navigation.instant` doesn't re-run JS | Med | Initialize filter.js via `document$.subscribe()`, not `DOMContentLoaded` |
| CACHE_VERSION bump → one slow full fetch (~300+ pages) | Low | Acceptable; dev uses `NOTION_NO_CACHE=1` |
| Material may not expose `page.meta.description` to the template | Low | Task 4 verifies the variable name on one page first; fallback `page.meta.get('description')` |
| Markdown stripping leaves stray symbols in description | Low | Pure helper + spot check; plain-text extraction only |

## Open Questions

- None blocking. F1 table styling and the `page.meta` variable name are each
  validated in a small first step of their task before the full change.
