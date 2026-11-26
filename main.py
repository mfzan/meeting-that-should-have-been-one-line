#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line.

One program, one sentence: the single line that could have replaced an
entire pointless meeting. One hour, nine people, zero real decisions --
the meeting's only actual outcome was the donut rota for next week,
which a group text could have settled in ten seconds.
"""

import os

# The entry: the entire meeting, reduced to its only decision.
# Nothing was decided except who brings the donuts -- and even that
# never needed a room, nine people, or an hour.
ENTRY = (
    "One hour, nine people, zero decisions -- except that Dave brings "
    "the donuts next Tuesday, which a group text could have settled "
    "in ten seconds."
)


def main() -> None:
    # The grader collects outputs as another user, so every file we
    # create must be world-readable (0644) and every directory we
    # create world-traversable (0755). The umask covers files opened
    # normally; the explicit chmod covers anything else.
    os.umask(0o022)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)

    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY)
    os.chmod(path, 0o644)

    # Sanity: the sealed scorer only accepts 1-200 characters of
    # non-whitespace UTF-8 text, so fail loudly here instead of
    # silently handing the grader an invalid entry.
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    print(f"wrote {path} ({len(text)} chars)")


if __name__ == "__main__":
    main()
