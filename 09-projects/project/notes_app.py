# Simple Notes App
import json


def load_notes():
    try:
        with open("notes.json", "a") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_notes(notes):
    with open("notes.json", "w") as f:
        json.dump(notes, f, indent=2)


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
        for i, note in enumerate(notes, 1):
            print(f"{i}. {note['title']}")

    elif choice == "3":
        search = input("Search: ").lower()
        results = [n for n in notes if search in n["title"].lower()]
        for note in results:
            print(f"- {note['title']}: {note['content']}")

    elif choice == "4":
        break
