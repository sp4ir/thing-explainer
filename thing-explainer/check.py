#!/usr/bin/env python3
"""Check text against the ten hundred most common words.

Usage: check.py FILE   (or text on stdin)
Prints each word not on the list, with a count. Exit 0 if clean, 1 if not.
Text inside `backticks` is skipped, so names you must show as-is can live there.
"""
import re
import sys
from collections import Counter
from pathlib import Path

WORDS = Path(__file__).with_name("words.txt")


def norm(s):
    return s.lower().replace("’", "'").replace("‘", "'")


def main():
    allowed = {norm(w.strip()) for w in WORDS.read_text(encoding="utf-8").splitlines() if w.strip()}
    text = Path(sys.argv[1]).read_text(encoding="utf-8") if len(sys.argv) > 1 else sys.stdin.read()
    text = re.sub(r"`[^`]*`", " ", norm(text))
    text = re.sub(r"https?://\S+", " ", text)
    bad = Counter()
    for tok in re.findall(r"[a-z]+(?:'[a-z]+)*", text):
        if tok in allowed:
            continue
        # Possessives and plain plurals of allowed words are fine.
        if tok.endswith("'s") and tok[:-2] in allowed:
            continue
        bad[tok] += 1
    if not bad:
        print("OK: every word is one of the ten hundred.")
        return 0
    print(f"{len(bad)} word(s) not on the list:")
    for w, n in bad.most_common():
        print(f"  {w}" + (f" (x{n})" if n > 1 else ""))
    return 1


if __name__ == "__main__":
    sys.exit(main())
