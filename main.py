#!/usr/bin/env python3
"""news-image-20261120 entry: copy the bundled image to /output/entry.png.

Python 3.13, standard library only. Deterministic: two runs write
byte-identical output. Outside the grader, MAKEFUN_OUTPUT_DIR stands
in for /output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(HERE / "entry.png", OUTPUT_DIR / "entry.png")


if __name__ == "__main__":
    main()
