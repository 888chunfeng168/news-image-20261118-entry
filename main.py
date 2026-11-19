#!/usr/bin/env python3
"""news-image-20261118 entry (Python 3.13, standard library only).

The poster image is drawn by draw.py (Pillow, run at build time) and shipped
in this repository as entry.png. This program copies it to the output
directory as entry.png. It is deterministic: the same repository always
writes the same bytes.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main() -> int:
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "entry.png"),
                    os.path.join(OUT_DIR, "entry.png"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
