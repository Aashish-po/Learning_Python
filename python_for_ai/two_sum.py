"""Wrapper to run the `two_sum` example moved into 10-exercises/project."""

from pathlib import Path
import runpy


def run():
    root = Path(__file__).resolve().parents[1]
    script = root / "10-exercises" / "project" / "two_sum.py"
    runpy.run_path(script, run_name="__main__")


if __name__ == "__main__":
    run()
