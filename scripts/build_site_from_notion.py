#!/usr/bin/env python3
"""Build a MkDocs source tree (generated_docs/) from a Notion database.

Pipeline:
    Notion data source -> publishable pages -> page body blocks -> Markdown
    -> generated_docs/problems/<slug>/index.md (+ index pages)

Design constraints (v1):
  * Never reads or embeds .cpp / .py solution files from the repo.
  * Never prints full page content — only the title and slug are logged.
  * Token is read from the environment (.env locally, Secrets in CI); never hard-coded.
  * Publish gate (v1): 進度 == "Done" AND the page has real note content
    (page body blocks, or the 筆記 property as a fallback). Empty pages are skipped.

This file is just the orchestration. The pieces live in the notionmd package:
  config   — paths, column names, env knobs, logging
  client   — Notion I/O, the global rate limiter, retries, queries
  convert  — Notion data -> Markdown / index pages
  cache    — the {page_id: last_edited_time} edit-time index
"""

from __future__ import annotations

import os
import shutil
from concurrent.futures import ThreadPoolExecutor, as_completed

from dotenv import load_dotenv

from notionmd import client as nclient
from notionmd import config, convert
from notionmd.cache import load_cache, save_cache
from notionmd.config import (
    COL_PROGRESS, MAX_WORKERS, PROBLEMS_DIR, PRUNE, PUBLISH_PROGRESS_VALUE,
    ROOT, SAVE_EVERY, log, warn,
)


def main() -> int:
    load_dotenv(ROOT / ".env")

    token = os.environ.get("NOTION_TOKEN")
    data_source_id = os.environ.get("NOTION_DATA_SOURCE_ID")
    database_id = os.environ.get("NOTION_DATABASE_ID")

    if not token:
        warn("NOTION_TOKEN is not set (use .env locally or GitHub Secrets in CI).")
        return 1
    if not data_source_id and not database_id:
        warn("Set NOTION_DATA_SOURCE_ID (preferred) or NOTION_DATABASE_ID.")
        return 1

    client = nclient.build_client(token)

    log(f"Querying Notion ({'data source' if data_source_id else 'database'}) "
        f"for {COL_PROGRESS} = {PUBLISH_PROGRESS_VALUE} ...")
    pages = nclient.query_pages(client, data_source_id, database_id)
    log(f"Fetched {len(pages)} page(s) matching the publish filter.")

    PROBLEMS_DIR.mkdir(parents=True, exist_ok=True)  # never rmtree'd at start

    # Precompute slug/num/props once per page (avoids double make_slug warnings).
    meta: dict[str, dict] = {}
    for page in pages:
        props = page.get("properties", {})
        title = convert.get_title(props, config.COL_TITLE)
        if not title:
            warn("Skipping a page with an empty 題目 (title).")
            continue
        num_str, slug = convert.make_slug(title)
        meta[page["id"]] = {"page": page, "props": props, "title": title,
                            "num_str": num_str, "slug": slug}

    # The edit-time index only decides what to (re)fetch. Content lives in the folder.
    cache = load_cache()  # {page_id: last_edited_time} — NOT deleted at start
    miss_ids = [pid for pid, mi in meta.items()
                if cache.get(pid) != mi["page"].get("last_edited_time", "")]
    log(f"Cache: {len(meta) - len(miss_ids)} unchanged, {len(miss_ids)} to (re)fetch "
        f"(workers={MAX_WORKERS}, rate={config.NOTION_RATE}/s, flush every {SAVE_EVERY}).")

    # Fetch changed pages concurrently. Write each result straight to the folder as
    # it arrives, and flush the edit-time index every SAVE_EVERY pages (+ on exit),
    # so an interruption keeps both the written files and the progress markers.
    processed = 0
    try:
        if miss_ids:
            with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
                futures = {pool.submit(convert.process_page, client, meta[pid]["page"],
                                       meta[pid]["num_str"], meta[pid]["props"]): pid
                           for pid in miss_ids}
                for fut in as_completed(futures):
                    pid = futures[fut]
                    mi = meta[pid]
                    out_dir = PROBLEMS_DIR / mi["slug"]
                    result = fut.result()
                    if result["status"] == "ok":
                        out_dir.mkdir(parents=True, exist_ok=True)
                        (out_dir / "index.md").write_text(result["page_md"], encoding="utf-8")
                        log(f"  fetched: {mi['title']}  [{mi['slug']}]")
                    else:  # became empty -> drop any stale file
                        if out_dir.exists():
                            shutil.rmtree(out_dir)
                        log(f"  skip ({result['reason']}): {mi['title']}  [{mi['slug']}]")
                    cache[pid] = mi["page"].get("last_edited_time", "")
                    processed += 1
                    if processed % SAVE_EVERY == 0:
                        save_cache(cache)
                        log(f"  ...{processed}/{len(miss_ids)} processed (index saved)")
    finally:
        save_cache(cache)

    # Drop edit-time entries for pages no longer in the query (deleted / unpublished).
    if PRUNE and pages:
        current_ids = set(meta)
        for pid in [pid for pid in cache if pid not in current_ids]:
            del cache[pid]
        save_cache(cache)

    # Build the problems index from the LIVE query metadata, for every page that
    # actually has a file on disk (so the folder stays the source of truth).
    rows: list[dict] = []
    valid_slugs: set[str] = set()
    for mi in meta.values():
        if (PROBLEMS_DIR / mi["slug"] / "index.md").exists():
            rows.append(convert.make_index_row(mi["props"], mi["num_str"], mi["slug"]))
            valid_slugs.add(mi["slug"])

    # Remove orphan problem dirs (renamed slug, or a page dropped from the query).
    if PRUNE and pages:
        for child in PROBLEMS_DIR.iterdir():
            if child.is_dir() and child.name not in valid_slugs:
                shutil.rmtree(child)

    convert.write_home_index()
    convert.write_patterns_index()
    convert.write_problems_index(rows)

    log(f"Done. Published {len(rows)}, skipped {len(meta) - len(rows)}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
