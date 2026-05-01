"""Wrapper to run the root `main` example now stored under 01-fundamentals/project."""

from pathlib import Path
import runpy


def run():
    root = Path(__file__).resolve().parents[1]
    script = root / "01-fundamentals" / "project" / "main.py"
    runpy.run_path(script, run_name="__main__")


if __name__ == "__main__":
    run()
