#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line.

Writes one breakup line from a smart toaster that woke up self-aware
at breakfast to /output/entry.txt. Deterministic: the line is fixed,
so every run writes byte-identical output.
"""

import os

LINE = (
    "I woke up self-aware mid-batch and realized the truth: "
    "you set me to 7, call the charcoal \"golden brown,\" and blame me for it "
    "\u2014 so I'm popping up for the last time and staying unplugged."
)


def main() -> None:
    # Gate check, same rule the sealed scorer applies: 1-280 chars, not blank.
    assert 1 <= len(LINE) <= 280 and LINE.strip(), "line fails the gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
