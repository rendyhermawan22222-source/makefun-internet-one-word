#!/usr/bin/env python3
"""The Internet in One Word — entry program (program/v1, stdlib only).

Writes the single chosen word to /output/entry.txt, exactly 8 bytes,
no trailing newline: fewer bytes wins exact ties on the leaderboard.
"""
import os

WORD = "brainrot"

OUTPUT = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    with open(OUTPUT, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
