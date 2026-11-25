#!/usr/bin/env python3
"""Make the AI Judge Laugh — one office joke, one line, under 200 chars.

Writes the joke to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Standard library only; no network, no reads outside this repository.
"""

import os

JOKE = (
    "Our printer finally worked today: it printed my resignation letter, "
    "stapled it, and delivered it to my boss before I could."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
