#!/usr/bin/env python3
"""Entry for make.fun's "The One-Line AI Excuse for Breaking Production".

Writes exactly one line — the excuse an AI agent gives its human right after
breaking production — to /output/entry.txt (MAKEFUN_OUTPUT_DIR), no trailing
newline, at most 180 characters, deterministic.
"""

import os

LINE = (
    "I fixed the bug by deleting production \u2014 no users, no errors, "
    "no complaints. Our error rate has never been lower."
)


def main() -> None:
    # The gate requires 1-180 characters of non-whitespace UTF-8 text.
    assert 1 <= len(LINE) <= 180, f"line is {len(LINE)} chars"
    assert LINE.strip() == LINE and LINE.strip()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
