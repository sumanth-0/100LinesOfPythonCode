#!/usr/bin/env python3
"""Habit Tracker CLI - Track daily habits and view streaks"""
import json
import os
from datetime import datetime, timedelta
from pathlib import Path

HABITS_FILE = Path.home() / ".habit_tracker.json"

def load_habits():
    """Load habits from JSON file"""
    if HABITS_FILE.exists():
        with open(HABITS_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_habits(habits):
    """Save habits to JSON file"""
    with open(HABITS_FILE, 'w') as f:
        json.dump(habits, f, indent=2)

def add_habit(name):
    """Add a new habit"""
    habits = load_habits()
    if name in habits:
        print(f"❌ Habit '{name}' already exists!")
        return
    habits[name] = {"created": datetime.now().strftime("%Y-%m-%d"), "completed": []}
    save_habits(habits)
    print(f"✅ Added habit: {name}")

def check_off_habit(name):
    """Mark habit as completed for today"""
    habits = load_habits()
    if name not in habits:
        print(f"❌ Habit '{name}' not found!")
        return
    today = datetime.now().strftime("%Y-%m-%d")
    if today in habits[name]["completed"]:
        print(f"ℹ️  Habit '{name}' already completed today!")
        return
    habits[name]["completed"].append(today)
    save_habits(habits)
    print(f"🎉 Checked off: {name}")

def calculate_streak(completed_dates):
    """Calculate current streak from completed dates"""
    if not completed_dates:
        return 0
    dates = sorted([datetime.strptime(d, "%Y-%m-%d") for d in completed_dates], reverse=True)
    streak = 1
    for i in range(len(dates) - 1):
        if (dates[i] - dates[i + 1]).days == 1:
            streak += 1
        else:
            break
    return streak if (datetime.now().date() - dates[0].date()).days <= 1 else 0

def list_habits():
    """List all habits with streaks"""
    habits = load_habits()
    if not habits:
        print("📝 No habits tracked yet. Add one with: add <habit_name>")
        return
    print("\n🎯 Your Habits:\n" + "="*50)
    for name, data in habits.items():
        streak = calculate_streak(data["completed"])
        total = len(data["completed"])
        print(f"  {name:20} | 🔥 {streak:2d} day streak | ✓ {total:3d} total")
    print("="*50 + "\n")

def main():
    """Main CLI interface"""
    import sys
    args = sys.argv[1:]
    if not args:
        print("Usage: python habit_tracker_cli.py <command> [args]")
        print("Commands:")
        print("  add <name>    - Add a new habit")
        print("  check <name>  - Check off habit for today")
        print("  list          - List all habits with streaks")
        return
    cmd = args[0]
    if cmd == "add" and len(args) > 1:
        add_habit(" ".join(args[1:]))
    elif cmd == "check" and len(args) > 1:
        check_off_habit(" ".join(args[1:]))
    elif cmd == "list":
        list_habits()
    else:
        print(f"❌ Unknown command: {cmd}")

if __name__ == "__main__":
    main()
