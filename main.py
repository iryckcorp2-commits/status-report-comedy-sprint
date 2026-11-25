#!/usr/bin/env python3
"""Status Report Comedy Sprint — one-line status report entry.

The program writes a single funny status-report line (at most 200
characters) to entry.txt in the output directory.
"""

import os

ENTRY = (
    "Weekly status: I did exactly what you asked, in the exact order "
    "you asked it, including the thing you asked me to undo. Twice."
)


def main() -> None:
    # The gate only accepts 1 to 200 characters; fail loudly instead
    # of writing an entry the judge never sees.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
