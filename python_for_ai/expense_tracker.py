"""Wrapper to run the `expense_tracker` example moved into 09-projects/project."""

from pathlib import Path
import runpy


def run():
    root = Path(__file__).resolve().parents[1]
    script = root / "09-projects" / "project" / "expense_tracker.py"
    runpy.run_path(script, run_name="__main__")


if __name__ == "__main__":
    run()
