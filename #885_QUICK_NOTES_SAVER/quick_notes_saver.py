"""
Quick Notes Saver
Author: Diya Satish Kumar
Description: Save terminal input into timestamped text files automatically.
"""

import os
from datetime import datetime

def create_notes_folder():
    """Create a folder named 'notes' if it doesn't exist."""
    folder = "notes"
    if not os.path.exists(folder):
        os.makedirs(folder)
    return folder

def get_filename():
    """Generate a timestamped filename."""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return f"note_{timestamp}.txt"

def save_note_to_file(content, folder):
    """Save content into a timestamped text file."""
    filename = get_filename()
    filepath = os.path.join(folder, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"\n✅ Note saved successfully as '{filename}' in '{folder}/'")

def main():
    print("📝 QUICK NOTES SAVER")
    print("Type your notes below. Press Enter twice to save and exit.\n")

    folder = create_notes_folder()
    lines = []

    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)

    if lines:
        content = "\n".join(lines)
        save_note_to_file(content, folder)
    else:
        print("⚠️ No note entered. Nothing saved.")

if __name__ == "__main__":
    main()