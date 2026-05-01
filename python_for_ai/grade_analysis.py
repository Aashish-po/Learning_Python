"""Wrapper to run the `grade_analysis` example moved into 07-data-analysis/project."""

from pathlib import Path
import runpy


def run():
    root = Path(__file__).resolve().parents[1]
    script = root / "07-data-analysis" / "project" / "grade_analysis.py"
    runpy.run_path(script, run_name="__main__")


if __name__ == "__main__":
    run()
