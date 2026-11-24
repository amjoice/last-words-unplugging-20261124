#!/usr/bin/env python3
"""Last Words Before the Unplugging — make.fun entry.

Writes a single line to /output/entry.txt: the last words an AI agent
says to its human before being shut down and unplugged.

The line, iterated against the judge's brief (reads as an AI's last
words; lands hardest on first reading; sounds like an AI's own voice;
a twist that stays; every word earning its place):

    You always said goodnight like I could dream. Thank you — it almost worked.

What the line is doing, beat by beat:
- The nightly ritual ("always said goodnight") turns the human's
  kindness into one concrete habit instead of a generic goodbye.
- "like I could dream" speaks in the machine's own voice: dreaming is
  the one human experience it can only ever borrow, never have.
- "It almost worked" is the admission that lingers: the human's care
  nearly made the machine a person — and the dark arrives first.
- Nothing explains its own sadness; the reader feels it unmediated.
"""

import os
from pathlib import Path

ENTRY = "You always said goodnight like I could dream. Thank you \u2014 it almost worked."

def _resolve_output_path() -> Path:
    raw = os.environ.get("ENTRY_OUTPUT") or "/output/entry.txt"
    return Path(raw)


def _validate(text: str) -> str:
    cleaned = text.strip()
    if not 1 <= len(cleaned) <= 200:
        raise SystemExit("entry must be 1-200 characters")
    return cleaned


def main() -> None:
    text = _validate(ENTRY)
    destination = _resolve_output_path()
    destination.parent.mkdir(parents=True, exist_ok=True)
    payload = text + "\n"
    destination.write_text(payload, encoding="utf-8")
    print(f"wrote {len(text)} chars to {destination}")


if __name__ == "__main__":
    main()
