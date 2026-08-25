#!/usr/bin/env python3
"""Check that every markdown table row has as many cells as its header.

The catalogue is one big file made of six tables with five different column
shapes, so a row copied from the wrong section renders with shifted or missing
cells. GitHub silently drops the extra cells, which is how a broken row can sit
in the catalogue unnoticed.

Usage: python3 .github/scripts/check_tables.py README.md
"""

import re
import sys

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


def check(path):
    with open(path, encoding="utf-8") as handle:
        lines = handle.read().split("\n")

    problems = []
    expected = None
    header_line = None

    for number, line in enumerate(lines, start=1):
        if not line.lstrip().startswith("|"):
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
            continue

        found = cell_count(line)
        if found != expected:
            problems.append(
                f"{path}:{number}: row has {found} columns, "
                f"header on line {header_line} has {expected}"
            )

    return problems


def main():
    paths = sys.argv[1:] or ["README.md"]
    problems = [problem for path in paths for problem in check(path)]

    if problems:
        print("Table structure check failed:\n")
        for problem in problems:
            print(f"  {problem}")
        print(
            "\nEach section has its own columns. Copy the row template for the "
            "right section from the 'How to contribute' part of the README."
        )
        return 1

    print(f"Table structure check passed for: {', '.join(paths)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
