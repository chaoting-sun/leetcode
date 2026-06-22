"""Edit-time index: {page_id: last_edited_time}.

Its only job is to decide what to re-fetch. It is NOT the source of truth for
content (that's the generated_docs/ folder), and it is never deleted at the
start of a run. Writes are atomic so an interrupted write can't corrupt it.
"""

from __future__ import annotations

import json

from .config import CACHE_FILE, CACHE_VERSION, USE_CACHE, warn


def load_cache() -> dict:
    if not USE_CACHE or not CACHE_FILE.exists():
        return {}
    try:
        data = json.loads(CACHE_FILE.read_text(encoding="utf-8"))
        if data.get("version") != CACHE_VERSION:
            return {}
        return data.get("pages", {})
    except Exception as e:  # corrupt cache -> rebuild from scratch
        warn(f"Ignoring unreadable cache ({e}).")
        return {}


def save_cache(pages: dict) -> None:
    if not USE_CACHE:
        return
    try:
        # Atomic write: a crash mid-write leaves the old cache intact, never a
        # half-written (corrupt) file.
        tmp = CACHE_FILE.with_name(CACHE_FILE.name + ".tmp")
        tmp.write_text(
            json.dumps({"version": CACHE_VERSION, "pages": pages}, ensure_ascii=False),
            encoding="utf-8",
        )
        tmp.replace(CACHE_FILE)
    except Exception as e:
        warn(f"Could not write cache ({e}).")
