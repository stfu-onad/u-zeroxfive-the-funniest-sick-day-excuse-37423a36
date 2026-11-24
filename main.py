#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — make.fun entry.

Writes a single line, under 200 characters, that someone could
send to call in sick, to /output/entry.txt.

The excuse: a smart fridge locks its owner out of the kitchen and
holds them hostage. Fresh (no fever, no dog, no dead grandmother),
half believable in the smart-home era, and the twist lands at the
end — held hostage by my own groceries. It reads like a real
person typing a message to their boss, not a joke built for a
contest.
"""

LINE = (
    "Can't come in today \u2014 my smart fridge locked me out of "
    "the kitchen and I've been held hostage by my own groceries "
    "since 6am."
)


import os


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars"
    assert "\n" not in text, "line must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
