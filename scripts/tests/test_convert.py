#!/usr/bin/env python3
"""On-demand unit checks for pure helpers in notionmd.convert.

Stdlib only (asserts + a __main__ runner) — no test framework, matching the
project's "run on demand" testing convention. Run from the project root:

    .venv/bin/python scripts/tests/test_convert.py
"""

from __future__ import annotations

import sys
from pathlib import Path

# Make the `notionmd` package importable without installing anything.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from notionmd.convert import _DESC_LIMIT, _yaml_dquote, make_description  # noqa: E402


def test_make_description_strips_markdown() -> None:
    md = (
        "## 1. Problem Summary\n\n"
        "- **直覺**: use a `sliding window` over the array.\n"
        "- See [the editorial](https://example.com) for more.\n"
        "> a quoted note\n"
    )
    out = make_description(md)
    # Markdown syntax must be gone; link text kept, URL dropped.
    for token in ("##", "**", "`", ">", "](", "https://"):
        assert token not in out, f"unstripped {token!r} in: {out!r}"
    assert "sliding window" in out
    assert "the editorial" in out and "example.com" not in out


def test_make_description_collapses_whitespace() -> None:
    out = make_description("a\n\n\n  b\t c")
    assert out == "a b c", repr(out)


def test_make_description_truncates_with_ellipsis_latin() -> None:
    word = "alpha "  # 6 chars
    out = make_description(word * 60)  # 360 chars, plenty over the limit
    assert out.endswith("…")
    assert len(out) <= _DESC_LIMIT + 1  # +1 for the ellipsis char
    # Word-boundary back-off: no partial trailing word before the ellipsis.
    assert not out[:-1].rstrip().endswith("alph")


def test_make_description_truncates_cjk_hardcut() -> None:
    out = make_description("國" * 300)
    assert out.endswith("…")
    assert len(out) <= _DESC_LIMIT + 1


def test_make_description_short_text_unchanged() -> None:
    assert make_description("Two pointers, O(n).") == "Two pointers, O(n)."


def test_make_description_empty() -> None:
    assert make_description("") == ""
    assert make_description("\n\n   \n") == ""
    assert make_description("```\ncode only\n```") == ""  # fenced code -> nothing


def test_yaml_dquote_escapes() -> None:
    assert _yaml_dquote('say "hi"') == '"say \\"hi\\""'
    assert _yaml_dquote("back\\slash") == '"back\\\\slash"'
    assert _yaml_dquote("plain") == '"plain"'


def main() -> int:
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    failed = 0
    for t in tests:
        try:
            t()
            print(f"  PASS  {t.__name__}")
        except AssertionError as e:
            failed += 1
            print(f"  FAIL  {t.__name__}: {e}")
    print(f"\n{len(tests) - failed}/{len(tests)} passed.")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
