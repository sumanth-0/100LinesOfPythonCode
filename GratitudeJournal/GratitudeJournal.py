"""Gratitude Journal CLI - Track daily gratitude with timestamps."""

import os, json
from datetime import datetime
from pathlib import Path


def get_journal_path():
    p = Path.home() / ".gratitude_journal"
    p.mkdir(exist_ok=True)
    return p / "entries.json"


def load_entries():
    try:
        return json.load(open(get_journal_path())) if get_journal_path().exists() else []
    except (json.JSONDecodeError, IOError):
        print("Warning: Could not read journal file.")
        return []


def save_entries(entries):
    try:
        json.dump(entries, open(get_journal_path(), "w"), indent=2)
    except IOError as e:
        print(f"Error: Could not save entry. {e}")


def add_entry():
    print("\n📝 What are you grateful for today?\n(Enter multiple lines. Press Enter twice when done)\n")
    lines, empty = [], 0
    while True:
        try:
            line = input()
            empty = (empty + 1) if line == "" else 0
            if empty >= 2:
                lines = lines[:-1] if lines else lines
                break
            lines.append(line)
        except EOFError:
            break

    text = "\n".join(lines).strip()
    if not text:
        print("❌ Entry cannot be empty.")
        return

    entries = load_entries()
    entries.append(
        {"date": datetime.now().strftime("%Y-%m-%d"), "timestamp": datetime.now().isoformat(), "content": text})
    save_entries(entries)
    print("✅ Gratitude entry saved!")


def view_entries():
    entries = load_entries()
    if not entries:
        print("\n📖 No entries yet.")
        return
    print("\n📖 Your Gratitude Journal\n" + "=" * 50)
    for i, e in enumerate(entries, 1):
        t = datetime.fromisoformat(e.get("timestamp", "")).strftime("%H:%M:%S") if e.get("timestamp") else ""
        print(f"\n[{i}] {e.get('date')} at {t}\n{'-' * 50}\n{e.get('content')}")
    print("\n" + "=" * 50)


def view_today():
    entries = load_entries()
    today = datetime.now().strftime("%Y-%m-%d")
    e = next((x for x in reversed(entries) if x.get("date") == today), None)
    if not e:
        print("\n📖 No entry for today yet.")
        return
    t = datetime.fromisoformat(e.get("timestamp", "")).strftime("%H:%M:%S") if e.get("timestamp") else ""
    print(f"\n📖 Today's Gratitude\n{'=' * 50}\n{today} at {t}\n{'-' * 50}\n{e.get('content')}\n{'=' * 50}")


def delete_entry(idx):
    entries = load_entries()
    if not entries or idx < 1 or idx > len(entries):
        print("❌ Invalid entry number.")
        return
    entries.pop(idx - 1)
    save_entries(entries)
    print("✅ Entry deleted.")


def export_to_markdown():
    entries = load_entries()
    if not entries:
        print("\n❌ No entries to export.")
        return
    p = get_journal_path().parent / "gratitude_journal_export.md"
    try:
        with open(p, "w", encoding="utf-8") as f:
            f.write(f"# 🙏 Gratitude Journal\n\n*Exported on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n\n---\n\n")
            for e in entries:
                t = datetime.fromisoformat(e.get("timestamp", "")).strftime("%H:%M:%S") if e.get("timestamp") else ""
                f.write(f"## {e.get('date')} at {t}\n\n{e.get('content')}\n\n---\n\n")
        print(f"✅ Journal exported to: {p}")
    except IOError as e:
        print(f"❌ Export error: {e}")


def main():
    while True:
        print("\n🙏 Gratitude Journal\n" + "=" * 50)
        print(
            "1. Add today's gratitude\n2. View today's entry\n3. View all entries\n4. Delete an entry\n5. Export to markdown\n6. Exit\n" + "=" * 50)
        choice = input("\nEnter choice (1-6): ").strip()

        if choice == "1":
            add_entry()
        elif choice == "2":
            view_today()
        elif choice == "3":
            view_entries()
        elif choice == "4":
            view_entries()
            try:
                delete_entry(int(input("\nEntry number to delete: ").strip()))
            except ValueError:
                print("❌ Invalid number.")
        elif choice == "5":
            export_to_markdown()
        elif choice == "6":
            print("\n✨ Thank you for reflecting on gratitude. Goodbye!")
            break
        else:
            print("❌ Invalid choice.")


if __name__ == "__main__":
    main()