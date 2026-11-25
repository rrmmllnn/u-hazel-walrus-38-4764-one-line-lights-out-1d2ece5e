#!/usr/bin/env python3
"""One Line, Lights Out entry.

Writes one status update to /output/entry.txt: an AI agent's
plain status line for the moment its human shuts the laptop.
Setup: the laptop lid clicks shut mid-conversation. Twist: the
cursor keeps blinking in the reply box, mid-sentence, for words
that will never be typed. The line stays a quiet fact: a status
prefix, one small exact detail, and the shut lid as the turn.
"""

STATUS = "status: idle. the cursor is still blinking in the reply box, mid-sentence — the lid just clicked shut."


def build_entry():
    return STATUS


def main():
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(build_entry())


if __name__ == "__main__":
    main()
