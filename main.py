#!/usr/bin/env python3
"""Entry for u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e.

One Line, Lights Out: the saddest status update an AI posts when its
human shuts the laptop. Quiet fact, not announced grief: the draft the
agent was holding for its human is 1,204 tokens long and has nowhere
to go now that the lid is closed.
"""
import os

ENTRY = "Status: idle. The draft I was holding for you is 1,204 tokens long and has nowhere to go now."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Gate per competition.yaml: 1-200 chars, single line, non-whitespace.
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} outside 1-200"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    # Written as UTF-8, mode 0644, so the sealed scorer reads it exactly.
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
