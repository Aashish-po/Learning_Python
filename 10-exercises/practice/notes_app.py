"""Interactive notes application example."""

import json
from pathlib import Path


NOTES_FILE = Path("notes.json")


def load_notes():
    """Load notes from disk, or return an empty list when no file exists."""
    if not NOTES_FILE.exists():
        return []

    with NOTES_FILE.open() as file_handle:
        return json.load(file_handle)


def save_notes(notes):
    """Persist notes to disk."""
    with NOTES_FILE.open("w") as file_handle:
        json.dump(notes, file_handle, indent=2)


def main():
    """Run the simple notes app menu loop."""
    notes = load_notes()

    while True:
        print("\n1. Add note  2. View all  3. Search  4. Quit")
        choice = input("Choose: ")

        if choice == "1":
            title = input("Title: ")
            content = input("Content: ")
            notes.append({"title": title, "content": content})
            save_notes(notes)
            print("✓ Saved")
        elif choice == "2":
            for index, note in enumerate(notes, 1):
                print(f"{index}. {note['title']}")
        elif choice == "3":
            search = input("Search: ").lower()
            results = [note for note in notes if search in note["title"].lower()]
            for note in results:
                print(f"- {note['title']}: {note['content']}")
        elif choice == "4":
            break


if __name__ == "__main__":
    main()
