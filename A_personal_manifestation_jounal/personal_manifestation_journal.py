# personal_manifestation_journal.py

import os
from datetime import datetime

JOURNAL_FILE = "manifestation_journal.txt"

def write_entry(entry):
    """Save a new journal entry with the current date and time."""
    with open(JOURNAL_FILE, "a") as file:
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {entry}\n")
    print("Your entry has been saved!")

def read_journal():
    """Read and display all journal entries."""
    if os.path.exists(JOURNAL_FILE):
        print("\n--- Your Manifestation Journal ---\n")
        with open(JOURNAL_FILE, "r") as file:
            print(file.read())
    else:
        print("Your journal is empty. Start writing your dreams today!")

def set_reminder(goal):
    """Set a reminder to revisit a specific goal."""
    print(f"Reminder set! Revisit your goal: '{goal}' regularly to stay motivated.")

def main():
    print("Welcome to Your Personal Manifestation Journal!")
    while True:
        print("\nOptions: [1] Write a new entry  [2] Read journal  [3] Set goal reminder  [4] Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            entry = input("Write your daily affirmation or manifestation: ")
            write_entry(entry)
        elif choice == "2":
            read_journal()
        elif choice == "3":
            goal = input("Enter a goal or affirmation for a reminder: ")
            set_reminder(goal)
        elif choice == "4":
            print("Goodbye! Keep manifesting your dreams!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
