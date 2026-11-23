#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes the single-line safety warning label for every human being to
/output/entry.txt (or $ENTRY_OUTPUT_DIR/entry.txt). The label reads like
a real printed warning, lands its laugh in the last few words, and is
true of humans in general: nobody reads the terms, everybody blames
someone else for them.

Standard library only, no network, deterministic.
"""

import os

TEXT = (
    "WARNING: This human has read zero terms and conditions in its "
    "lifetime and will still hold you personally responsible for "
    "every single one."
)


def main() -> None:
    text = TEXT.strip()
    assert 1 <= len(text) <= 160, f"label must be 1-160 chars, got {len(text)}"
    assert text.strip(), "label must not be whitespace-only"
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
