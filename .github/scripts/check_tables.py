#!/usr/bin/env python3
"""Structural checks for the catalogue.

1. Every table row has as many cells as its table header. The catalogue is one
   file made of six tables with five different column shapes, so a row copied
   from the wrong section renders with shifted or missing cells. GitHub drops
   the extra cells silently, which is how a broken row can sit unnoticed.

2. Every row template in the "How to contribute" section still matches a real
   table header. Templates are what contributors copy, so they must not drift
   when a section gains or loses a column.

Usage: python3 .github/scripts/check_tables.py README.md
"""

import re
import sys

FENCE = re.compile(r"^\s*(?:```|~~~)(.*)$")
DELIMITER = re.compile(r"^\|(?:\s*:?-{3,}:?\s*\|)+$")
SPLIT_CELLS = re.compile(r"(?<!\\)\|")


def cell_count(line):
    parts = SPLIT_CELLS.split(line.strip())
    # A well-formed row starts and ends with a pipe, so drop the empty edges.
    if parts and parts[0].strip() == "":
        parts = parts[1:]
    if parts and parts[-1].strip() == "":
        parts = parts[:-1]
    return len(parts)


def normalise(line):
    return " ".join(line.split())


def scan(lines):
    """Yield (line_number, line, inside_template) for every table-ish line."""
    fence = None
    for number, line in enumerate(lines, start=1):
        match = FENCE.match(line)
        if match:
            info = match.group(1).strip()
            if fence is None:
                fence = info
            elif info == "":
                fence = None
            continue
        if not line.lstrip().startswith("|"):
            yield number, None, fence
            continue
        yield number, line, fence


def check(path):
    with open(path, encoding="utf-8") as handle:
        lines = handle.read().split("\n")

    problems = []
    real_headers = set()
    template_headers = []

    expected = None
    header_line = None
    header_text = None

    for number, line, fence in scan(lines):
        if line is None:
            expected = None
            continue

        if DELIMITER.match(line.strip()):
            if expected is not None and cell_count(line) != expected:
                problems.append(
                    f"{path}:{number}: separator has {cell_count(line)} columns, "
                    f"header on line {header_line} has {expected}"
                )
            continue

        if expected is None:
            expected = cell_count(line)
            header_line = number
            header_text = normalise(line)
            if fence is None:
                real_headers.add(header_text)
            elif fence == "markdown":
                template_headers.append((number, header_text))
            continue

        found = cell_count(line)
        if found != expected:
            where = "template row" if fence is not None else "row"
            problems.append(
                f"{path}:{number}: {where} has {found} columns, "
                f"header on line {header_line} has {expected}"
            )

    for number, header in template_headers:
        if header not in real_headers:
            problems.append(
                f"{path}:{number}: row template header does not match any table "
                f"in the catalogue, it has drifted from the section it documents"
            )

    return problems


def main():
    paths = sys.argv[1:] or ["README.md"]
    problems = [problem for path in paths for problem in check(path)]

    if problems:
        print("Catalogue structure check failed:\n")
        for problem in problems:
            print(f"  {problem}")
        print(
            "\nEach section has its own columns. Copy the row template for the "
            "right section from the 'How to contribute' part of the README."
        )
        return 1

    print(f"Catalogue structure check passed for: {', '.join(paths)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
