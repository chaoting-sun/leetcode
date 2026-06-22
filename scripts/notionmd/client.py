"""Notion I/O: client construction, global rate limiting, retries, and queries.

All raw network access lives here. A single module-level RateLimiter is shared
across every worker thread, so the *total* outbound request rate is capped
regardless of how many workers run — this is what prevents 429 storms.
"""

from __future__ import annotations

import threading
import time

from notion_client import Client
from notion_client.errors import HTTPResponseError, RequestTimeoutError

from . import config
from .config import COL_PROGRESS, PUBLISH_PROGRESS_VALUE


class RateLimiter:
    """Token-bucket-style limiter: hands out request slots no faster than `rate`/s.

    Thread-safe. The lock is held only to reserve a slot (cheap); the actual wait
    happens outside the lock so threads don't serialize on the sleep itself.
    """

    def __init__(self, rate_per_sec: float):
        self.min_interval = 1.0 / rate_per_sec if rate_per_sec > 0 else 0.0
        self._lock = threading.Lock()
        self._next = 0.0

    def acquire(self) -> None:
        if self.min_interval <= 0:
            return
        with self._lock:
            now = time.monotonic()
            slot = max(now, self._next)
            self._next = slot + self.min_interval
            wait = slot - now
        if wait > 0:
            time.sleep(wait)


# Shared across all threads — the single point that enforces the global rate.
_limiter = RateLimiter(config.NOTION_RATE)


def build_client(token: str) -> Client:
    return Client(auth=token, notion_version=config.NOTION_VERSION)


def with_retry(fn, *args, max_attempts: int = 6, **kwargs):
    """Call a Notion endpoint through the global rate limiter, retrying on 429/5xx.

    The limiter is acquired before every attempt (including retries), so even
    backoff retries respect the global rate. Honors the Retry-After header when
    Notion sends it; otherwise backs off exponentially.
    """
    delay = 1.0
    for attempt in range(1, max_attempts + 1):
        _limiter.acquire()
        try:
            return fn(*args, **kwargs)
        except HTTPResponseError as e:
            status = getattr(e, "status", None)
            retryable = status == 429 or (status is not None and status >= 500)
            if not retryable or attempt == max_attempts:
                raise
            wait = delay
            try:
                ra = e.headers.get("Retry-After")
                if ra:
                    wait = float(ra)
            except Exception:
                pass
            time.sleep(wait)
            delay = min(delay * 2, 30.0)
        except RequestTimeoutError:
            if attempt == max_attempts:
                raise
            time.sleep(delay)
            delay = min(delay * 2, 30.0)


def get_children(client: Client, block_id: str) -> list:
    blocks, cursor = [], None
    while True:
        kwargs = {"block_id": block_id, "page_size": 100}
        if cursor:
            kwargs["start_cursor"] = cursor
        resp = with_retry(client.blocks.children.list, **kwargs)
        blocks.extend(resp.get("results", []))
        if not resp.get("has_more"):
            break
        cursor = resp.get("next_cursor")
    return blocks


def query_pages(client: Client, data_source_id: str | None, database_id: str | None) -> list:
    body = {"filter": {"property": COL_PROGRESS, "select": {"equals": PUBLISH_PROGRESS_VALUE}}}
    results, cursor = [], None
    while True:
        payload = dict(body)
        if cursor:
            payload["start_cursor"] = cursor

        if data_source_id:
            if hasattr(client, "data_sources"):
                resp = with_retry(client.data_sources.query, data_source_id=data_source_id, **payload)
            else:  # older SDK without the data_sources namespace
                resp = with_retry(
                    client.request,
                    path=f"data_sources/{data_source_id}/query", method="POST", body=payload,
                )
        else:
            resp = with_retry(client.databases.query, database_id=database_id, **payload)

        results.extend(resp.get("results", []))
        if not resp.get("has_more"):
            break
        cursor = resp.get("next_cursor")
    return results
