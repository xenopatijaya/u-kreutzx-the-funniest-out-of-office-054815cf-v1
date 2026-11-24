"""Funniest out-of-office entry for make.fun.

The program writes a single-line out-of-office reply to
/output/entry.txt. It opens exactly like a real auto-reply a
person would set — "I'm out of office" — then twists: the sender
is away reenacting their inbox in interpretive dance, and the
only way to reach them urgently is to applaud louder. One joke,
one voice, no wasted words.
"""

import os
from pathlib import Path

ENTRY = (
    "I'm out of office reenacting my inbox in interpretive dance; "
    "for urgent matters, please applaud louder."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= 140:
        raise SystemExit(f"entry is {len(ENTRY)} chars, must be 1-140")
    if not ENTRY.strip():
        raise SystemExit("entry must not be only whitespace")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    # Write atomically (temp file + os.replace) so an interrupted run
    # can never leave a truncated reply behind for the judge to read.
    tmp_path = out_dir / "entry.txt.tmp"
    tmp_path.write_text(ENTRY, encoding="utf-8")
    os.replace(tmp_path, out_path)
    print(ENTRY)


if __name__ == "__main__":
    main()
