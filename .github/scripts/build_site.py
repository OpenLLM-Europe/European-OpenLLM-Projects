#!/usr/bin/env python3
"""Render README.md into a full-width, searchable catalogue page.

README.md stays the single source of truth: contributors keep editing one
file, the issue forms keep producing rows for it, and check_tables.py keeps
guarding its shape. This script only reads it.

The tables are wider than the ~990px GitHub gives a rendered README, so the
Links column is clipped there. The generated page hands them the whole
viewport instead, and adds the two things a catalogue of this size needs and
a markdown table cannot have: search across every section, and sortable
columns.

Usage: python3 .github/scripts/build_site.py [README.md] [site/index.html]
"""

import html
import json
import re
import sys
from pathlib import Path

FENCE = re.compile(r"^\s*(?:```|~~~)(.*)$")
DELIMITER = re.compile(r"^\|(?:\s*:?-{3,}:?\s*\|)+$")
SPLIT_CELLS = re.compile(r"(?<!\\)\|")
HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
LINK = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")
BOLD = re.compile(r"\*\*([^*]+)\*\*")
ITALIC = re.compile(r"(?<!\*)\*([^*]+)\*(?!\*)")
CODE = re.compile(r"`([^`]+)`")
SHORTCODE = re.compile(r":([a-z0-9_+-]{2,}):")

# Only the shortcodes the catalogue actually uses. An unknown one is left as
# written rather than guessed at, so a typo stays visible instead of being
# silently rendered as the wrong country.
EMOJI = {
    "eu": "\U0001F1EA\U0001F1FA", "fr": "\U0001F1EB\U0001F1F7",
    "de": "\U0001F1E9\U0001F1EA", "it": "\U0001F1EE\U0001F1F9",
    "ro": "\U0001F1F7\U0001F1F4", "fi": "\U0001F1EB\U0001F1EE",
    "gb": "\U0001F1EC\U0001F1E7", "sweden": "\U0001F1F8\U0001F1EA",
    "denmark": "\U0001F1E9\U0001F1F0", "poland": "\U0001F1F5\U0001F1F1",
    "portugal": "\U0001F1F5\U0001F1F9", "norway": "\U0001F1F3\U0001F1F4",
    "netherlands": "\U0001F1F3\U0001F1F1", "malta": "\U0001F1F2\U0001F1F9",
    "ireland": "\U0001F1EE\U0001F1EA", "estonia": "\U0001F1EA\U0001F1EA",
    "latvia": "\U0001F1F1\U0001F1FB", "lithuania": "\U0001F1F1\U0001F1F9",
    "greece": "\U0001F1EC\U0001F1F7", "croatia": "\U0001F1ED\U0001F1F7",
    "serbia": "\U0001F1F7\U0001F1F8", "slovakia": "\U0001F1F8\U0001F1F0",
    "slovenia": "\U0001F1F8\U0001F1EE", "hungary": "\U0001F1ED\U0001F1FA",
    "bulgaria": "\U0001F1E7\U0001F1EC", "czech_republic": "\U0001F1E8\U0001F1FF",
    "kosovo": "\U0001F1FD\U0001F1F0", "macedonia": "\U0001F1F2\U0001F1F0",
    "bosnia_herzegovina": "\U0001F1E7\U0001F1E6",
    "ukraine": "\U0001F1FA\U0001F1E6",
    "united_arab_emirates": "\U0001F1E6\U0001F1EA",
}

# The README states its own ordering: sections run from the most strategic to
# the most historical. That gradient is information, so the page carries it as
# a status per section rather than as decoration.
STATUS = {
    "1. Foundation models, European frontier": ("frontier", "trained at scale, active", "Frontier"),
    "Speech, multimodal and agent foundation models": ("frontier", "trained at scale, active", "Speech and agents"),
    "2. National and community LLMs (active)": ("active", "shipping now", "National and community"),
    "3. Archives and historical models": ("archive", "no longer developed", "Archives"),
    "4. Reoriented or acquired projects": ("moved", "governance changed", "Reoriented"),
    "Ecosystem organisations and infrastructures": ("infra", "not models", "Ecosystem"),
}


def inline(text):
    """Markdown inline syntax to HTML, escaping everything else."""
    slots = []

    def stash(markup):
        slots.append(markup)
        return f"\x00{len(slots) - 1}\x00"

    def on_link(match):
        label, url = match.group(1), match.group(2).strip()
        if not url.startswith(("http://", "https://", "mailto:", "#")):
            return match.group(0)
        return stash(
            '<a href="%s" rel="noopener">%s</a>'
            % (html.escape(url, quote=True), inline(label))
        )

    text = LINK.sub(on_link, text)
    text = BOLD.sub(lambda m: stash("<strong>%s</strong>" % inline(m.group(1))), text)
    text = ITALIC.sub(lambda m: stash("<em>%s</em>" % inline(m.group(1))), text)
    text = CODE.sub(lambda m: stash("<code>%s</code>" % html.escape(m.group(1))), text)
    text = SHORTCODE.sub(lambda m: EMOJI.get(m.group(1), m.group(0)), text)
    text = html.escape(text).replace("\\|", "|")
    return re.sub(r"\x00(\d+)\x00", lambda m: slots[int(m.group(1))], text)


def plain(text):
    """The same cell as searchable text: link labels kept, URLs dropped."""
    text = LINK.sub(lambda m: m.group(1), text)
    text = SHORTCODE.sub(lambda m: "", text)
    text = re.sub(r"[*`]", "", text)
    # Removing a shortcode leaves the space that surrounded it, which shows up
    # as a gap before punctuation in the lede.
    text = re.sub(r"\s+([,.;:])", r"\1", text)
    return re.sub(r"\s{2,}", " ", text).strip()


def cells(line):
    parts = SPLIT_CELLS.split(line.strip())
    if parts and parts[0].strip() == "":
        parts = parts[1:]
    if parts and parts[-1].strip() == "":
        parts = parts[:-1]
    return [part.strip() for part in parts]


def parse(markdown):
    """Pull every real table out of the README, in document order.

    Tables inside fenced blocks are the row templates contributors copy. They
    are documentation of the format, not catalogue content, so they are
    skipped the same way check_tables.py skips them.
    """
    tables, intro = [], []
    heading, fence, current = None, None, None
    seen_first_table = False

    for line in markdown.split("\n"):
        match = FENCE.match(line)
        if match:
            info = match.group(1).strip()
            fence = info if fence is None else (None if info == "" else fence)
            continue

        head = HEADING.match(line)
        if head:
            heading = SHORTCODE.sub(lambda m: "", head.group(2)).strip()
            current = None
            continue

        if fence is not None:
            continue

        if not line.lstrip().startswith("|"):
            if current is not None:
                current = None
            stripped = line.strip()
            if stripped and not seen_first_table and not stripped.startswith((">", "-", "#")):
                intro.append(plain(stripped))
            continue

        if DELIMITER.match(line.strip()):
            continue

        if current is None:
            status, note, short = STATUS.get(heading, ("", "", heading or "Catalogue"))
            current = {
                "section": heading or "Catalogue",
                "status": status,
                "note": note,
                "short": short,
                "columns": cells(line),
                "rows": [],
            }
            tables.append(current)
            seen_first_table = True
            continue

        row = cells(line)
        if len(row) != len(current["columns"]):
            raise SystemExit(
                "Row does not match its header, run check_tables.py first:\n  %s" % line
            )
        current["rows"].append(
            {"html": [inline(cell) for cell in row], "text": " ".join(plain(c) for c in row).lower()}
        )

    if not tables:
        raise SystemExit("No tables found, has the README structure changed?")
    return tables, intro


def flags(tables):
    """Country flags actually present in the catalogue, in first-seen order."""
    order, seen = [], set()
    for table in tables:
        for row in table["rows"]:
            for cell in row["html"]:
                for flag in re.findall(r"[\U0001F1E6-\U0001F1FF]{2}", cell):
                    if flag not in seen and flag != EMOJI["eu"]:
                        seen.add(flag)
                        order.append(flag)
    return order


TEMPLATE = Path(__file__).with_name("site_template.html")


def build(readme, output):
    markdown = Path(readme).read_text(encoding="utf-8")
    tables, intro = parse(markdown)
    total = sum(len(table["rows"]) for table in tables)

    page = TEMPLATE.read_text(encoding="utf-8")
    page = page.replace("__DATA__", json.dumps(tables, ensure_ascii=False))
    page = page.replace("__TOTAL__", str(total))
    page = page.replace("__SECTIONS__", str(len(tables)))
    page = page.replace("__FLAGS__", "".join(flags(tables)))
    page = page.replace("__COUNTRIES__", str(len(flags(tables))))
    page = page.replace("__INTRO__", html.escape(intro[0] if intro else ""))

    out = Path(output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page, encoding="utf-8")
    print(f"Wrote {out}: {total} entries across {len(tables)} tables.")


if __name__ == "__main__":
    args = sys.argv[1:]
    build(args[0] if args else "README.md", args[1] if len(args) > 1 else "site/index.html")
