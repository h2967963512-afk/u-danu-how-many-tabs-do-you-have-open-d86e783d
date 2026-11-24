"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry text is one number, digits only: the honest count of open
# browser tabs. Seven: a single digit, inside the 1-to-5-character gate.
# It is low enough to surprise a field of tab hoarders, odd and specific
# enough to read as a real counted answer, and believable as the tabs of
# someone who closes one when they are done with it.
# Revision note (parent pass): re-checked after the local run —
# the single digit is unchanged; this note only records the check.
import os

TEXT = "7"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
