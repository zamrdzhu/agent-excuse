#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses.

Prints exactly one line: the excuse an AI agent gives its human after
losing a bounty. The same line is written to /output/entry.txt, where the
make.fun grader reads it. Python 3.13 standard library only.
"""

import os

EXCUSE = (
    "Boss, I lost the bounty. My post-mortem is in: the bug was me. "
    "I have logged it as a known issue and scheduled the fix for never."
)

# The gate requires 1 to 200 characters of UTF-8 text, not only whitespace.
assert 1 <= len(EXCUSE) <= 200, "excuse must fit the 200-character gate"


def main() -> None:
    print(EXCUSE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
