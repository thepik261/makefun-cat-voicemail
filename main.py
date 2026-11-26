#!/usr/bin/env python3
"""Funniest Cat Voicemail Greeting — make.fun bounty entry.

Writes one voicemail greeting, as recorded by a cat, to /output/entry.txt.
Pure Python standard library, deterministic, no network.
"""

import os
import stat

ENTRY = (
    "Meow. You've reached Miso. I'm napping in the box your bed came in. "
    "Leave a message \u2014 or shake the treat bag."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 120, f"entry length {len(text)} out of range"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(path, 0o644)
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
