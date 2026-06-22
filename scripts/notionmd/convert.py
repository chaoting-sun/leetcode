"""Turn Notion data into Markdown and site files.

Property extraction, slug rules, Notion-block -> Markdown rendering, per-page
processing, and the index pages. Network access is delegated to client.get_children;
everything else here is plain data transformation.
"""

from __future__ import annotations

import re

from slugify import slugify

from .client import get_children
from .config import (
    COL_ATTEMPTS, COL_BLOCKERS, COL_DATE, COL_DIFFICULTY, COL_LINK, COL_NOTES,
    COL_PROFICIENCY, COL_SOURCE, COL_TAGS, COL_TITLE, DOCS_DIR, PATTERNS_DIR,
    PROBLEMS_DIR, warn,
)

# --------------------------------------------------------------------------- #
# Notion property helpers
# --------------------------------------------------------------------------- #

def _plain(rich: list) -> str:
    return "".join(r.get("plain_text", "") for r in (rich or []))


def get_title(props: dict, name: str) -> str:
    p = props.get(name) or {}
    return _plain(p.get("title", [])).strip()


def get_select(props: dict, name: str) -> str:
    p = props.get(name) or {}
    sel = p.get("select")
    return (sel or {}).get("name", "") if sel else ""


def get_multi(props: dict, name: str) -> list[str]:
    p = props.get(name) or {}
    return [o.get("name", "") for o in (p.get("multi_select") or [])]


def get_number(props: dict, name: str):
    p = props.get(name) or {}
    return p.get("number")


def get_date(props: dict, name: str) -> str:
    p = props.get(name) or {}
    d = p.get("date")
    return (d or {}).get("start", "") if d else ""


def get_url(props: dict, name: str) -> str:
    p = props.get(name) or {}
    return p.get("url") or ""


def get_rich_text_plain(props: dict, name: str) -> str:
    p = props.get(name) or {}
    return _plain(p.get("rich_text", [])).strip()


# --------------------------------------------------------------------------- #
# Slug
# --------------------------------------------------------------------------- #

_NUM_PREFIX = re.compile(r"^\s*\d+\s*[.):\-]*\s*")


def strip_number_prefix(title: str) -> str:
    """'0001. Two Sum' -> 'Two Sum' (returns the original if nothing strips)."""
    return _NUM_PREFIX.sub("", title).strip() or title


def make_slug(title: str) -> tuple[str | None, str]:
    """Return (zero-padded number string or None, slug).

    "1. Two Sum" / "0001 Two Sum" / "0001. Two Sum" -> ("0001", "0001-two-sum")
    Titles without a leading number get a warning so the number can be added later.
    """
    m = re.match(r"^\s*(\d+)\s*[.):\-]*\s*(.+?)\s*$", title)
    if m:
        num_str = f"{int(m.group(1)):04d}"
        rest = slugify(m.group(2))
        slug = f"{num_str}-{rest}" if rest else num_str
        return num_str, slug
    warn(f"No leading number in title '{title}' — please add a problem number later.")
    return None, slugify(title) or "untitled"


# --------------------------------------------------------------------------- #
# Notion blocks -> Markdown
# --------------------------------------------------------------------------- #

# Block types rendered to Markdown. `table` is built from its `table_row` children;
# `table_row`/`child_page` are handled (row content / silent skip) without a warning.
SUPPORTED = {
    "paragraph", "heading_1", "heading_2", "heading_3",
    "bulleted_list_item", "numbered_list_item", "to_do",
    "code", "quote", "divider", "table",
}


def rich_to_md(rich: list) -> str:
    out = []
    for r in rich or []:
        t = r.get("plain_text", "")
        if not t:
            continue
        ann = r.get("annotations", {})
        if ann.get("code"):
            t = f"`{t}`"
        if ann.get("bold"):
            t = f"**{t}**"
        if ann.get("italic"):
            t = f"*{t}*"
        if ann.get("strikethrough"):
            t = f"~~{t}~~"
        href = r.get("href")
        if href:
            t = f"[{t}]({href})"
        out.append(t)
    return "".join(out)


def _cell_to_md(cell: list) -> str:
    # Pipes and newlines would break a Markdown table cell.
    return rich_to_md(cell).replace("|", "\\|").replace("\n", "<br>")


def render_table(client, block: dict) -> str:
    """Convert a Notion `table` block (+ its `table_row` children) to a Markdown table."""
    data = block.get("table", {})
    has_col_header = data.get("has_column_header", False)

    matrix = []
    for row in get_children(client, block["id"]):
        if row.get("type") != "table_row":
            continue
        matrix.append([_cell_to_md(c) for c in row["table_row"].get("cells", [])])
    if not matrix:
        return ""

    width = max((len(r) for r in matrix), default=0)
    for r in matrix:
        r.extend([""] * (width - len(r)))  # pad ragged rows

    if has_col_header:
        header, body = matrix[0], matrix[1:]
    else:
        header, body = [""] * width, matrix

    lines = ["| " + " | ".join(header) + " |",
             "| " + " | ".join(["---"] * width) + " |"]
    lines += ["| " + " | ".join(r) + " |" for r in body]
    return "\n".join(lines)


def render_block(client, block: dict, depth: int, number: int) -> str:
    btype = block["type"]
    data = block.get(btype, {})
    indent = "    " * depth

    if btype == "paragraph":
        line = indent + rich_to_md(data.get("rich_text", []))
    elif btype in ("heading_1", "heading_2", "heading_3"):
        hashes = {"heading_1": "#", "heading_2": "##", "heading_3": "###"}[btype]
        line = f"{hashes} {rich_to_md(data.get('rich_text', []))}"
    elif btype == "bulleted_list_item":
        line = f"{indent}- {rich_to_md(data.get('rich_text', []))}"
    elif btype == "numbered_list_item":
        line = f"{indent}{number}. {rich_to_md(data.get('rich_text', []))}"
    elif btype == "to_do":
        mark = "x" if data.get("checked") else " "
        line = f"{indent}- [{mark}] {rich_to_md(data.get('rich_text', []))}"
    elif btype == "quote":
        line = f"{indent}> {rich_to_md(data.get('rich_text', []))}"
    elif btype == "code":
        lang = data.get("language", "") or ""
        code = "".join(r.get("plain_text", "") for r in data.get("rich_text", []))
        fence = f"```{lang}\n{code}\n```"
        return fence  # code blocks never recurse into children
    elif btype == "table":
        return render_table(client, block)  # rows handled here, no generic recursion
    elif btype == "table_row":
        return ""  # only meaningful inside a table (handled by render_table)
    elif btype == "child_page":
        return ""  # silently skip nested sub-pages
    elif btype == "divider":
        line = "---"
    else:
        warn(f"Unsupported block type: {btype}")
        line = f"> Unsupported block type: {btype}"

    # Recurse into nested children (nested lists, toggles, etc.).
    if block.get("has_children"):
        children = get_children(client, block["id"])
        child_md = render_blocks(client, children, depth + 1)
        if child_md:
            line = f"{line}\n{child_md}"
    return line


def render_blocks(client, blocks: list, depth: int = 0) -> str:
    parts: list[str] = []
    number = 0
    for block in blocks:
        if block["type"] == "numbered_list_item":
            number += 1
        else:
            number = 0
        parts.append(render_block(client, block, depth, number))
    return "\n\n".join(p for p in parts if p.strip())


# --------------------------------------------------------------------------- #
# Page + index rendering
# --------------------------------------------------------------------------- #

def build_page_markdown(num_str: str | None, props: dict, body_md: str) -> str:
    title = get_title(props, COL_TITLE)
    heading = f"{num_str}. {strip_number_prefix(title)}" if num_str else title

    lines = [f"# {heading}", ""]

    meta = []
    if (v := get_select(props, COL_DIFFICULTY)):
        meta.append(f"- Difficulty: {v}")
    if (v := get_multi(props, COL_TAGS)):
        meta.append(f"- Tags: {', '.join(v)}")
    if (v := get_multi(props, COL_SOURCE)):
        meta.append(f"- Source: {', '.join(v)}")
    if (v := get_select(props, COL_PROFICIENCY)):
        meta.append(f"- Proficiency: {v}")
    if (v := get_multi(props, COL_BLOCKERS)):
        meta.append(f"- Blockers: {', '.join(v)}")
    if (v := get_number(props, COL_ATTEMPTS)) is not None:
        meta.append(f"- Attempts: {int(v) if float(v).is_integer() else v}")
    if (v := get_date(props, COL_DATE)):
        meta.append(f"- Date: {v}")
    if (v := get_url(props, COL_LINK)):
        meta.append(f"- LeetCode: {v}")

    lines.extend(meta)
    lines += ["", "---", "", "## Notes", "", body_md, ""]
    return "\n".join(lines)


def process_page(client, page: dict, num_str: str | None, props: dict) -> dict:
    """Fetch a page's body and render it to Markdown.

    Returns {"status": "ok", "page_md": ...} or {"status": "skip", "reason": ...}.
    The caller already knows the slug/title; this only does the network + render.
    """
    body_blocks = get_children(client, page["id"])
    body_md = render_blocks(client, body_blocks).strip()
    if not body_md:  # fall back to the 筆記 property when the page body is empty
        body_md = get_rich_text_plain(props, COL_NOTES).strip()
    if not body_md:
        return {"status": "skip", "reason": "no-notes"}
    return {"status": "ok", "page_md": build_page_markdown(num_str, props, body_md)}


def make_index_row(props: dict, num_str: str | None, slug: str) -> dict:
    """Build one row of the problems index table from live query properties."""
    title = get_title(props, COL_TITLE)
    return {
        "num_str": num_str or "",
        "sort_key": int(num_str) if num_str else 10**9,
        "slug": slug,
        "display_title": strip_number_prefix(title),
        "difficulty": get_select(props, COL_DIFFICULTY),
        "tags": get_multi(props, COL_TAGS),
        "proficiency": get_select(props, COL_PROFICIENCY),
    }


def write_home_index() -> None:
    content = (
        "# LeetCode Notes\n\n"
        "This site contains my LeetCode problem notes and pattern notes.\n\n"
        "- [Problems](problems/index.md)\n"
        "- [Patterns](patterns/index.md)\n"
    )
    (DOCS_DIR / "index.md").write_text(content, encoding="utf-8")


def write_patterns_index() -> None:
    PATTERNS_DIR.mkdir(parents=True, exist_ok=True)
    (PATTERNS_DIR / "index.md").write_text("# Patterns\n\nComing soon.\n", encoding="utf-8")


def write_problems_index(rows: list[dict]) -> None:
    # rows sorted; numberless entries (sort key 10**9) fall to the end.
    rows = sorted(rows, key=lambda r: r["sort_key"])
    lines = [
        "# Problems",
        "",
        "| # | Title | Difficulty | Tags | Proficiency | Notes |",
        "|---|-------|------------|------|-------------|-------|",
    ]
    for r in rows:
        num = r["num_str"].lstrip("0") if r["num_str"] else "—"
        tags = ", ".join(r["tags"]) if r["tags"] else ""
        lines.append(
            f"| {num} | [{r['display_title']}]({r['slug']}/index.md) | "
            f"{r['difficulty']} | {tags} | {r['proficiency']} | [Notes]({r['slug']}/index.md) |"
        )
    lines.append("")
    PROBLEMS_DIR.mkdir(parents=True, exist_ok=True)
    (PROBLEMS_DIR / "index.md").write_text("\n".join(lines), encoding="utf-8")
