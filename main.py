#!/usr/bin/env python3
"""Status Report Comedy Sprint — writes one funny status line to /output/entry.txt.

The line (101 chars, one line):
  This week I answered 312 of your questions. I was confident about all of
  them. I was right about 41.
"""
import os

LINE = (
    "This week I answered 312 of your questions. "
    "I was confident about all of them. I was right about 41."
)


def main():
    assert "\n" not in LINE, "entry must be a single line"
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
