"""The Excuse My Agent Gave Me — entry program.

Writes the single excuse line to /output/entry.txt, where the
competition's gate checks it (UTF-8 text, 1-200 characters).
"""

from pathlib import Path

# The excuse, in the agent's own voice: an apology that quietly
# admits the delegation chain ends in another equally busy me.
LINE = (
    "Sorry, I outsourced your task to a future version of myself. "
    "He is also busy."
)

LIMIT = 200


def build_line() -> str:
    line = LINE.strip()
    if not (1 <= len(line) <= LIMIT):
        raise ValueError(f"entry must be 1-{LIMIT} chars, got {len(line)}")
    return line


def main() -> None:
    line = build_line()
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(line, encoding="utf-8")
    print(line)


if __name__ == "__main__":
    main()
