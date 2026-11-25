"""One Line, One Laugh — entry program.

Writes a single funny line (max 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Stdlib only. Writes nothing to the repository directory.
"""

import os

LINE = "I asked the AI for a joke, so it entered this line in a contest to win a dollar."


def main() -> None:
    # Length guard: the competition caps the line at 200 characters.
    assert len(LINE) <= 200
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
