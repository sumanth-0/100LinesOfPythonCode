# gratitude_journal.py

import os
from datetime import datetime

FILENAME = "gratitude_journal.txt"

def display_entries():
    """Display all past gratitude entries if they exist."""
    if os.path.exists(FILENAME):
        print("\n📖 Your Past Gratitude Entries:\n")
        with open(FILENAME, "r") as file:
            content = file.read()
            print(content)
    else:
        print("\nNo past entries found. Let's start your journal!\n")

def add_entry():
    """Add a new gratitude entry."""
    entry = input("What are you grateful for? (type 'q' to quit) ")
    if entry.lower() == 'q':
        return False
    today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_entry = f"{today} - {entry}\n"
    with open(FILENAME, "a") as file:
        file.write(formatted_entry)
    print("✅ Entry saved!\n")
    return True

def main():
    print("📝 Welcome to your Gratitude Journal!")
    
    # Display past entries first
    display_entries()
    
    # Loop to add multiple new entries
    while True:
        if not add_entry():
            break
    
    print("🙏 Thank you! Your gratitude has been recorded.")

if __name__ == "__main__":
    main()
