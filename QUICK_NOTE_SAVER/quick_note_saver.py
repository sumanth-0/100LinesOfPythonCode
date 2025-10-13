# Quick Note Saver - Take notes from terminal and save in timestamped files
import os
from datetime import datetime
import json

NOTES_DIR = "notes"

def ensure_dir():
    if not os.path.exists(NOTES_DIR):
        os.makedirs(NOTES_DIR)
        print(f"📁 Created notes directory: {NOTES_DIR}")

def add_note():
    ensure_dir()
    print("\n✍️  Quick Note Entry\n" + "=" * 50)
    title = input("Note Title (or press Enter for untitled): ").strip() or "Untitled Note"
    print("\n📝 Enter your note below (Type END on a new line to save & exit)\n" + "-" * 50)
    lines = []
    while True:
        line = input()
        if line.strip().upper() == 'END':
            break
        lines.append(line)
    content = "\n".join(lines)
    if not content.strip():
        print("❌ Note is empty. Not saved.")
        return
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note_data = {"title": title, "timestamp": timestamp, "content": content}
    filename = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{title.replace(' ', '_')[:30]}.json"
    filepath = os.path.join(NOTES_DIR, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(note_data, f, indent=2, ensure_ascii=False)
    print(f"\n✅ Note saved successfully!\n📄 File: {filename}")

def view_notes():
    ensure_dir()
    files = [f for f in os.listdir(NOTES_DIR) if f.endswith('.json')]
    if not files:
        print("\n📭 No notes found.")
        return
    files.sort(reverse=True)
    print(f"\n📚 Your Notes ({len(files)} total)\n" + "=" * 70)
    for idx, filename in enumerate(files, 1):
        filepath = os.path.join(NOTES_DIR, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                note = json.load(f)
            print(f"\n{idx}. {note['title']}")
            print(f"   🕒 {note['timestamp']}")
            print(f"   📝 {note['content'][:100]}{'...' if len(note['content']) > 100 else ''}")
        except:
            print(f"{idx}. {filename} (Error reading file)")

def search_notes():
    ensure_dir()
    keyword = input("\n🔍 Enter search keyword: ").strip().lower()
    if not keyword:
        print("❌ No keyword provided.")
        return
    files = [f for f in os.listdir(NOTES_DIR) if f.endswith('.json')]
    matches = []
    for filename in files:
        filepath = os.path.join(NOTES_DIR, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                note = json.load(f)
            if keyword in note['title'].lower() or keyword in note['content'].lower():
                matches.append(note)
        except:
            pass
    if matches:
        print(f"\n✨ Found {len(matches)} matching note(s)\n" + "=" * 70)
        for idx, note in enumerate(matches, 1):
            print(f"\n{idx}. {note['title']}")
            print(f"   🕒 {note['timestamp']}")
            print(f"   📝 {note['content'][:150]}{'...' if len(note['content']) > 150 else ''}")
    else:
        print(f"\n❌ No notes found matching '{keyword}'")

def main():
    print("\n🌟 Welcome to Quick Note Saver!")
    while True:
        print("\n" + "=" * 50 + "\n📝 QUICK NOTE SAVER\n" + "=" * 50)
        print("1. 📝 Add New Note\n2. 📚 View All Notes\n3. 🔍 Search Notes\n4. 🚪 Exit\n" + "=" * 50)
        choice = input("\nSelect an option (1-4): ").strip()
        if choice == '1':
            add_note()
        elif choice == '2':
            view_notes()
        elif choice == '3':
            search_notes()
        elif choice == '4':
            print("\n👋 Thanks for using Quick Note Saver! Goodbye!")
            break
        else:
            print("❌ Invalid option. Please choose 1-4.")

if __name__ == "__main__":
    main()