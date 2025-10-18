#!/usr/bin/env python3
"""
Water Intake Tracker - A CLI tool to track daily water intake
Helps users monitor their hydration goals throughout the day
"""

import json
import os
from datetime import datetime, date
from pathlib import Path

DATA_FILE = Path.home() / ".water_intake_tracker.json"
DEFAULT_GOAL = 2000  # Default daily goal in ml

def load_data():
    """Load water intake data from file"""
    if DATA_FILE.exists():
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {"goal": DEFAULT_GOAL, "records": {}}

def save_data(data):
    """Save water intake data to file"""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def get_today():
    """Get today's date as string"""
    return date.today().isoformat()

def add_intake(data, amount):
    """Add water intake for today"""
    today = get_today()
    if today not in data["records"]:
        data["records"][today] = []
    timestamp = datetime.now().strftime("%H:%M:%S")
    data["records"][today].append({"time": timestamp, "amount": amount})
    save_data(data)
    return sum(r["amount"] for r in data["records"][today])

def get_today_total(data):
    """Get total intake for today"""
    today = get_today()
    if today in data["records"]:
        return sum(r["amount"] for r in data["records"][today])
    return 0

def set_goal(data, goal):
    """Set daily water intake goal"""
    data["goal"] = goal
    save_data(data)

def show_history(data, days=7):
    """Show water intake history"""
    print(f"\n{'Date':<12} {'Total (ml)':<12} {'Goal':<10} {'Status'}")
    print("-" * 50)
    dates = sorted(data["records"].keys(), reverse=True)[:days]
    for d in dates:
        total = sum(r["amount"] for r in data["records"][d])
        goal = data["goal"]
        status = "✓" if total >= goal else "✗"
        print(f"{d:<12} {total:<12} {goal:<10} {status}")

def display_progress(current, goal):
    """Display progress bar"""
    percentage = min(int((current / goal) * 100), 100)
    bar_length = 30
    filled = int((percentage / 100) * bar_length)
    bar = "█" * filled + "░" * (bar_length - filled)
    print(f"\nProgress: [{bar}] {percentage}%")
    print(f"Current: {current}ml / Goal: {goal}ml")
    if current >= goal:
        print("🎉 Daily goal achieved!")
    else:
        print(f"Remaining: {goal - current}ml")

def main():
    """Main function"""
    data = load_data()
    print("\n=== Water Intake Tracker ===")
    print("Commands: add <ml>, status, goal <ml>, history, quit")
    
    while True:
        cmd = input("\n> ").strip().lower().split()
        if not cmd:
            continue
        
        if cmd[0] == "quit":
            print("Goodbye! Stay hydrated!")
            break
        elif cmd[0] == "add" and len(cmd) == 2:
            try:
                amount = int(cmd[1])
                total = add_intake(data, amount)
                print(f"Added {amount}ml. Total today: {total}ml")
                display_progress(total, data["goal"])
            except ValueError:
                print("Please enter a valid number")
        elif cmd[0] == "status":
            total = get_today_total(data)
            display_progress(total, data["goal"])
        elif cmd[0] == "goal" and len(cmd) == 2:
            try:
                goal = int(cmd[1])
                set_goal(data, goal)
                print(f"Daily goal set to {goal}ml")
            except ValueError:
                print("Please enter a valid number")
        elif cmd[0] == "history":
            show_history(data)
        else:
            print("Invalid command. Try: add <ml>, status, goal <ml>, history, quit")

if __name__ == "__main__":
    main()
