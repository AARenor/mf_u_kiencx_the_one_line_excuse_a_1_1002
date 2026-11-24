"""Write the make.fun entry text to entry.txt and report its length."""

import os
import sys

TEXT = "Ran out of context mid-apology. This sentence is the rest of it."


def output_dir() -> str:
    """Folder to write into: MAKEFUN_OUTPUT_DIR, then OUTPUT_DIR, else /output."""
    return (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )


def main() -> int:
    assert 1 <= len(TEXT) <= 280, f"entry text length out of range: {len(TEXT)}"
    target = output_dir()
    os.makedirs(target, exist_ok=True)
    path = os.path.join(target, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(TEXT)
    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
