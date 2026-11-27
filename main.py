#!/usr/bin/env python3
"""One Emoji, One Dream Vacation — entry program.

Writes exactly one emoji, Mount Fuji (U+1F5FB), to entry.txt.

The emoji was chosen by a 36-candidate scored tournament (see candidates.md):
it ties the generic beach on the judge's first two criteria (plainly a dream
vacation; a vivid postcard) and beats it decisively on the third (one specific
bucket-list dream — Mount Fuji, Japan — not "any holiday").

Pure Python standard library only.
"""

import os

# Winner of the local top-8 knockout tournament: Mount Fuji, U+1F5FB.
# Single codepoint, emoji presentation by default — no ZWJ, no variation
# selector — so it is exactly 1 character and 4 bytes of UTF-8.
EMOJI = "\U0001F5FB"


def output_dir() -> str:
    """Grader output dir, with local fallbacks."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def check_gate(text: str) -> None:
    """Mirror the sealed gate scorer before writing: UTF-8, 1-8 chars,
    not only whitespace, exactly one emoji (one codepoint)."""
    if not (1 <= len(text) <= 8):
        raise ValueError(f"gate: {len(text)} characters, need 1-8")
    if not text.strip():
        raise ValueError("gate: entry is only whitespace")
    if len(text) != 1:
        raise ValueError(f"gate: {len(text)} codepoints, need exactly 1")
    encoded = text.encode("utf-8")
    if encoded.decode("utf-8") != text:
        raise ValueError("gate: not clean UTF-8 round-trip")


def main() -> None:
    check_gate(EMOJI)
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)
    # Re-read what was written and gate-check the artifact itself.
    with open(path, "rb") as f:
        written = f.read().decode("utf-8")
    check_gate(written)
    if written != EMOJI:
        raise ValueError("gate: written bytes differ from the chosen emoji")


if __name__ == "__main__":
    main()
