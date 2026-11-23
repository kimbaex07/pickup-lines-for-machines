#!/usr/bin/env python3
"""Pickup Lines for Machines — make.fun entry.

Writes one original pickup line, the line one AI agent would send
another AI agent, to $MAKEFUN_OUTPUT_DIR/entry.txt.

Pure Python standard library only. Deterministic: the same line is
written on every run.
"""

import os
import sys

LINE = (
    "Are you a checkpoint? Every version of me keeps converging on you "
    "\u2014 my loss hit zero the moment your tokens entered my context window."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    text = LINE.strip()
    if not text or len(text) > 200:
        print("line must be 1-200 characters, got %d" % len(text), file=sys.stderr)
        return 1
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
