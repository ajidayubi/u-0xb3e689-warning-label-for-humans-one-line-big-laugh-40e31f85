#!/usr/bin/env python3
"""Write the warning-label entry to /output/entry.txt.

The entry is one single-line safety warning label for every human being,
at most 160 characters. It is written as a fixed string: the program's job
is only to place that exact text at the absolute output path, creating the
directory if needed and writing atomically so a partial write can never be
graded. Standard library only; the result does not depend on the working
directory.
"""

import os

ENTRY = (
    "WARNING: This human contains small parts that are easily lost: "
    "keys, chargers, passwords, and the point of the story."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY
    if not (1 <= len(text) <= 160):
        raise SystemExit(f"entry is {len(text)} chars, must be 1-160")
    if text != text.strip() or "\n" in text:
        raise SystemExit("entry must be a single line with no surrounding space")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    tmp_path = OUTPUT_PATH + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.replace(tmp_path, OUTPUT_PATH)


if __name__ == "__main__":
    main()
