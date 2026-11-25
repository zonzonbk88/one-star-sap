"""One Star, Written in Sap — entry writer.

Writes a single one-line 1-star review, in the voice of a houseplant
reviewing its human owner, to entry.txt in the output directory.
"""

import os

ENTRY = (
    "One star. He waters me on a schedule set by an app that has never "
    "met a plant. I drowned in March, and I have been thirsty since "
    "Tuesday. The app is thriving."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
