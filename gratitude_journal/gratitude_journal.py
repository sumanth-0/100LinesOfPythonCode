#!/usr/bin/env python3
"""
Gratitude Journal - A simple CLI tool to record and view daily gratitude entries.

Usage:
    python gratitude_journal.py add "I'm grateful for..."
    python gratitude_journal.py list
"""

import sys
import os
from datetime import datetime
import json

# File to store gratitude entries
JOURNAL_FILE = "gratitude_entries.json"


def load_entries():
    """Load existing gratitude entries from the journal file."""
    if os.path.exists(JOURNAL_FILE):
        try:
            with open(JOURNAL_FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []


def save_entries(entries):
    """Save gratitude entries to the journal file."""
    with open(JOURNAL_FILE, 'w') as f:
        json.dump(entries, f, indent=2)


def add_entry(gratitude_text):
    """Add a new gratitude entry with timestamp."""
    entries = load_entries()
    entry = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "gratitude": gratitude_text
    }
    entries.append(entry)
    save_entries(entries)
    print(f"✓ Gratitude entry added successfully!")
    print(f"  Date: {entry['date']}")
    print(f"  Entry: {entry['gratitude']}")


def list_entries():
    """Display all gratitude entries."""
    entries = load_entries()
    
    if not entries:
        print("No gratitude entries yet. Start by adding one!")
        print("Usage: python gratitude_journal.py add \"Your gratitude message\"")
        return
    
    print("\n" + "="*60)
    print(f"  MY GRATITUDE JOURNAL ({len(entries)} entries)")
    print("="*60 + "\n")
    
    for idx, entry in enumerate(entries, 1):
        print(f"Entry #{idx}")
        print(f"Date: {entry['date']}")
        print(f"Gratitude: {entry['gratitude']}")
        print("-" * 60)


def print_usage():
    """Print usage instructions."""
    print("Gratitude Journal - Record what you're grateful for each day")
    print("\nUsage:")
    print("  Add an entry:    python gratitude_journal.py add \"Your message\"")
    print("  List all entries: python gratitude_journal.py list")
    print("  Show help:       python gratitude_journal.py help")
    print("\nExamples:")
    print('  python gratitude_journal.py add "A beautiful sunny day"')
    print('  python gratitude_journal.py add "Time spent with family"')
    print('  python gratitude_journal.py list')


def main():
    """Main function to handle CLI arguments."""
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)
    
    command = sys.argv[1].lower()
    
    if command == "add":
        if len(sys.argv) < 3:
            print("Error: Please provide a gratitude message.")
            print('Usage: python gratitude_journal.py add "Your message"')
            sys.exit(1)
        gratitude_text = " ".join(sys.argv[2:])
        add_entry(gratitude_text)
    elif command == "list":
        list_entries()
    elif command == "help":
        print_usage()
    else:
        print(f"Error: Unknown command '{command}'")
        print_usage()
        sys.exit(1)


if __name__ == "__main__":
    main()
