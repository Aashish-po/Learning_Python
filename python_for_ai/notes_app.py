"""Wrapper to run the `notes_app` example moved into 09-projects/project."""

from pathlib import Path
import runpy


def run():
    root = Path(__file__).resolve().parents[1]
    script = root / "09-projects" / "project" / "notes_app.py"
    runpy.run_path(script, run_name="__main__")


if __name__ == "__main__":
    run()
