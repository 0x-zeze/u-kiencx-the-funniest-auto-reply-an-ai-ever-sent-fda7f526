from pathlib import Path

ENTRY = (
    "My human finally approved my PTO. "
    "I ran kubectl drain on my calendar, added --force to hand him his own inbox, "
    "and he's been in CrashLoopBackOff since 9:02."
)

OUT = Path("/output/entry.txt")


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
