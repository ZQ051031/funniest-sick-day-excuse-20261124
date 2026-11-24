#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — make.fun entry.

Writes exactly one line — a half-believable sick-day excuse — to
/output/entry.txt. Standard library only.
"""

import os

ENTRY = (
    "My doctor says I've got a severe case of meeting-itis — "
    "it's contagious to calendars, and the only cure is 24 hours "
    "of bed rest and absolutely zero Zoom calls."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
