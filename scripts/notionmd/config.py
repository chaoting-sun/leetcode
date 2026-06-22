"""Configuration: paths, Notion column names, env-driven knobs, and logging.

This module imports nothing from the rest of the package, so everything else can
import it freely without circular-import risk.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

# Project root is two levels up from this file: leetcode/scripts/notionmd/config.py
ROOT = Path(__file__).resolve().parent.parent.parent
DOCS_DIR = ROOT / "generated_docs"
PROBLEMS_DIR = DOCS_DIR / "problems"
PATTERNS_DIR = DOCS_DIR / "patterns"

# Column names in the Notion database (see SPEC.md).
COL_TITLE = "題目"
COL_DIFFICULTY = "難度"
COL_TAGS = "分類"
COL_SOURCE = "來源"
COL_PROFICIENCY = "熟練度"
COL_BLOCKERS = "卡點"
COL_ATTEMPTS = "次數"
COL_DATE = "Date"
COL_PROGRESS = "進度"
COL_NOTES = "筆記"
COL_LINK = "連結"

PUBLISH_PROGRESS_VALUE = "Done"  # v1 minimum publish condition

# Notion API version that exposes the data-source endpoints.
NOTION_VERSION = "2025-09-03"

# Concurrency: page bodies are fetched in parallel. The global rate limiter (see
# client.py) caps total outbound rate, so extra workers simply queue on it.
MAX_WORKERS = int(os.environ.get("NOTION_MAX_WORKERS", "8"))

# Proactive global rate limit (requests/sec). Notion's documented average is ~3/s.
# Every Notion call passes through this before firing, which prevents 429 storms.
NOTION_RATE = float(os.environ.get("NOTION_RATE", "3"))

# Edit-time index: maps {page_id: last_edited_time}. Its ONLY job is to decide
# whether a page needs re-fetching. The generated_docs/ folder — not this file —
# is the source of truth for content. NEVER deleted at the start of a run.
# Bump CACHE_VERSION whenever the rendering logic changes, to force a re-fetch.
CACHE_VERSION = 5
CACHE_FILE = ROOT / ".notion_cache.json"
USE_CACHE = os.environ.get("NOTION_NO_CACHE", "") == ""

# Flush the edit-time index to disk every N freshly-processed pages (and on exit).
SAVE_EVERY = int(os.environ.get("NOTION_SAVE_EVERY", "5"))

# Remove pages/dirs that are no longer published (deleted, or progress != Done).
# Only ever runs at the END of a successful, non-empty run. Set NOTION_NO_PRUNE=1 to disable.
PRUNE = os.environ.get("NOTION_NO_PRUNE", "") == ""


def log(msg: str) -> None:
    print(msg, flush=True)


def warn(msg: str) -> None:
    print(f"WARNING: {msg}", file=sys.stderr, flush=True)
