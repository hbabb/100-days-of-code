"""Update the progress tracker in each round's README from its log.

For every round-* folder that has both a log.md and a README.md, count
the "## Day " headings in log.md and rewrite the text between these two
markers in README.md:

    <!-- progress:start -->
    <!-- progress:end -->
"""

import re
from pathlib import Path

TOTAL_DAYS = 100
BAR_WIDTH = 20
START = "<!-- progress:start -->"
END = "<!-- progress:end -->"


def count_days(log_text):
    """Count the lines that start with '## Day '."""
    return sum(1 for line in log_text.splitlines() if line.startswith("## Day "))


def build_tracker(days):
    """Build the tracker text: the day count and a 20-block bar."""
    days = min(days, TOTAL_DAYS)
    percent = days * 100 // TOTAL_DAYS
    filled = days * BAR_WIDTH // TOTAL_DAYS
    bar = "█" * filled + "░" * (BAR_WIDTH - filled)
    return (
        f'<text color="secondary">{days} / {TOTAL_DAYS} Days Completed</text>\n'
        "\n"
        "```text\n"
        f"{bar} {percent}%\n"
        "```"
    )


def update_readme(readme_text, tracker):
    """Replace everything between the markers with the new tracker."""
    pattern = re.compile(re.escape(START) + ".*?" + re.escape(END), re.DOTALL)
    if not pattern.search(readme_text):
        raise ValueError(f"README is missing the {START} and {END} markers")
    replacement = f"{START}\n{tracker}\n{END}"
    return pattern.sub(lambda _: replacement, readme_text)


def main():
    for round_dir in sorted(Path(".").glob("round-*")):
        log = round_dir / "log.md"
        readme = round_dir / "README.md"
        if not (log.is_file() and readme.is_file()):
            continue

        days = count_days(log.read_text(encoding="utf-8"))
        old = readme.read_text(encoding="utf-8")
        new = update_readme(old, build_tracker(days))

        if new != old:
            readme.write_text(new, encoding="utf-8")
            print(f"{round_dir}: updated to {days} days")
        else:
            print(f"{round_dir}: already up to date ({days} days)")


if __name__ == "__main__":
    main()
