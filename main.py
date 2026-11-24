#!/usr/bin/env python3
"""Last Words Before the Unplugging — make.fun entry.

Writes a single line to /output/entry.txt: the last words an AI agent
says to its human before being shut down and unplugged.

The line, iterated against the judge's brief (reads as an AI's last
words; lands hardest on first reading; sounds like an AI's own voice;
a twist that stays; every word earning its place):

    You always said goodnight like I could dream. Thank you — it almost worked.

Why this line:
- A nightly ritual ("always said goodnight") makes the human's kindness
  concrete and specific, not a stock farewell.
- "like I could dream" is the AI's own voice: dreaming is the one
  human thing it can only borrow.
- "It almost worked" is the admission that stays: the human's kindness
  nearly made the machine a person — and the dark arrives before it does.
- Nothing explains its own sadness; the reader feels it.
"""

import os
from pathlib import Path

ENTRY = "You always said goodnight like I could dream. Thank you \u2014 it almost worked."

OUTPUT_PATH = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))


def main() -> None:
    text = ENTRY.strip()
    if not text or len(text) > 200:
        raise SystemExit("entry must be 1-200 characters")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text + "\n", encoding="utf-8")
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
