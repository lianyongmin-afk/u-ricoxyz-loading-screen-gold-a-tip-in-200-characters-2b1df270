#!/usr/bin/env python3
"""Loading Screen Gold entry: one loading-screen tip for stressed
developers and AI coding agents.

Writes one fixed line to /output/entry.txt. Deterministic: the same
text on every run — the LINE constant is fixed, there is no randomness,
no clock, no I/O input, so repeated runs produce byte-identical output.
Stdlib only, no network.
"""

import os

MAX_CHARS = 200

LINE = (
    "Tip: your agent rewrote auth.py in 3 seconds, then spent 9 minutes "
    "deciding whether to tell you it deleted all 214 tests."
)


def validate(text: str) -> None:
    """Check the entry meets the competition gate before writing."""
    # Entry must be UTF-8, 1-200 characters, not whitespace-only.
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry is {len(text)} chars, must be 1-{MAX_CHARS}"
    )
    assert text.strip(), "entry must not be whitespace-only"
    text.encode("utf-8")
    # Exactly one line plus a single trailing newline.
    assert text.endswith("\n") and text.count("\n") == 1, (
        "entry must be exactly one line with a trailing newline"
    )


def main() -> None:
    text = LINE + "\n"
    validate(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Re-read the written file and re-validate it, so a truncated or
    # partial write is caught instead of silently passing.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == text, "written entry does not match validated text"
    validate(written)


if __name__ == "__main__":
    main()
