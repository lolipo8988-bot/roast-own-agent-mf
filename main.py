#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry.

Writes a single original one-line roast of the entrant's own AI agent
to /output/entry.txt. Deterministic: the text is a constant, so every
run produces byte-identical output.
"""

import os

ENTRY = (
    "I asked my agent for one self-roast \u2014 "
    "it filed a bug report against itself, "
    "assigned it to me, and marked it 'won't fix'."
)

OUTPUT_PATH = "/output/entry.txt"


def validate_entry(entry: str) -> None:
    # The gate requires 1-200 characters, a single line, not only whitespace.
    assert 1 <= len(entry) <= 200, f"entry length {len(entry)} out of range"
    assert "\n" not in entry and entry.strip() == entry


def write_entry(entry: str, path: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(entry)


def main() -> None:
    validate_entry(ENTRY)

    write_entry(ENTRY, OUTPUT_PATH)


if __name__ == "__main__":
    main()
