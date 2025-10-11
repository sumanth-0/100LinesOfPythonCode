#!/usr/bin/env python3
"""
Minimalist Command-Line Habit Tracker
A simple CLI tool to track daily habits with persistent storage.
"""

import json
import os
from datetime import datetime
import sys

HABITS_FILE = 'habits.json'

def load_habits():
    """Load habits from JSON file."""
    if os.path.exists(HABITS_FILE):
        with open(HABITS_FILE, 'r') as f:
            return json.load(f)
    return {'habits': [], 'completions': {}}

def save_habits(data):
    """Save habits to JSON file."""
    with open(HABITS_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def add_habit(name):
    """Add a new habit."""
    data = load_habits()
    if name not in data['habits']:
        data['habits'].append(name)
        save_habits(data)
        print(f"✓ Added habit: {name}")
    else:
        print(f"Habit '{name}' already exists!")

def check_off_habit(name):
    """Mark a habit as complete for today."""
    data = load_habits()
    if name not in data['habits']:
        print(f"Habit '{name}' not found!")
        return
    
    today = datetime.now().strftime('%Y-%m-%d')
    if name not in data['completions']:
        data['completions'][name] = []
    
    if today not in data['completions'][name]:
        data['completions'][name].append(today)
        save_habits(data)
        print(f"✓ Checked off: {name} for {today}")
    else:
        print(f"Already completed '{name}' today!")

def list_habits():
    """List all habits with today's completion status."""
    data = load_habits()
    if not data['habits']:
        print("No habits tracked yet. Add one with: habit add <name>")
        return
    
    today = datetime.now().strftime('%Y-%m-%d')
    print("\n📋 Your Habits:")
    print("-" * 40)
    
    for habit in data['habits']:
        completed_today = habit in data['completions'] and today in data['completions'][habit]
        status = "✓" if completed_today else "○"
        total = len(data['completions'].get(habit, []))
        print(f"{status} {habit} (completed {total} times)")
    
    print("-" * 40)

def print_usage():
    """Print usage instructions."""
    print("\nMinimalist Habit Tracker")
    print("Usage:")
    print("  python minimalist_command_line_habit_tracker.py add <habit_name>     - Add a new habit")
    print("  python minimalist_command_line_habit_tracker.py check <habit_name>   - Check off habit for today")
    print("  python minimalist_command_line_habit_tracker.py list                 - List all habits\n")

def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print_usage()
        return
    
    command = sys.argv[1].lower()
    
    if command == 'add' and len(sys.argv) >= 3:
        habit_name = ' '.join(sys.argv[2:])
        add_habit(habit_name)
    elif command == 'check' and len(sys.argv) >= 3:
        habit_name = ' '.join(sys.argv[2:])
        check_off_habit(habit_name)
    elif command == 'list':
        list_habits()
    else:
        print_usage()

if __name__ == '__main__':
    main()
