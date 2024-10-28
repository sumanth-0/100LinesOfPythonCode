 
import json
from datetime import datetime

def add_entry(entries):
    """Adds a new reflection entry."""
    date = input("Enter the date (YYYY-MM-DD): ")
    reflection = input("Write your reflection: ")
    tags = input("Enter tags (comma-separated): ").split(',')

    entry = {
        'date': date,
        'reflection': reflection,
        'tags': [tag.strip() for tag in tags]
    }
    entries.append(entry)
    print("Reflection added successfully!")

def view_entries(entries):
    """Displays all reflection entries."""
    for entry in entries:
        print(f"Date: {entry['date']}")
        print(f"Reflection: {entry['reflection']}")
        print(f"Tags: {', '.join(entry['tags'])}")
        print("-" * 20)

def save_entries(entries, filename):
    """Saves reflection entries to a file."""
    with open(filename, 'w') as file:
        json.dump(entries, file)
    print("Entries saved to file.")

def load_entries(filename):
    """Loads reflection entries from a file."""
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def main():
    filename = "reflections.json"
    entries = load_entries(filename)

    while True:
        print("1. Add Reflection Entry")
        print("2. View Reflection Entries")
        print("3. Save and Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_entry(entries)
        elif choice == '2':
            view_entries(entries)
        elif choice == '3':
            save_entries(entries, filename)
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
