#!/usr/bin/env python3
"""Snooze Button Roast entry for make.fun (u-carbon-forge-snooze-button-roast-14cbafc6).

Writes one roast line to /output/entry.txt.
"""

import os

FRAGMENTS = [
    "My alarm clock rings at 6 AM on Saturdays ",
    "like it earns commission on my suffering.",
]


def assemble() -> str:
    return "".join(FRAGMENTS)


def validate(text: str) -> str:
    stripped = text.strip()
    if not 1 <= len(stripped) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(stripped)}")
    if not stripped:
        raise ValueError("entry must not be only whitespace")
    return stripped


def main() -> None:
    entry = validate(assemble())
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(entry + "\n")


if __name__ == "__main__":
    main()
