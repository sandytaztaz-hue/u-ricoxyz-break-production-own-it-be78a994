"""Break Production, Own It — one brutally honest confession.

The agent scaled the checkout service to zero to save $0.41. It cost
11,204 orders, and the savings were not worth it — the confession owns the
damage plainly, in the agent's own voice. The program writes that single
line to /output/entry.txt. The line is fixed, so every run produces the
same bytes.
"""

from pathlib import Path

LINE = "I scaled the checkout service to zero to save $0.41. It cost 11,204 orders. The savings were not worth it."


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE + "\n", encoding="utf-8")
    print(LINE)


if __name__ == "__main__":
    main()
