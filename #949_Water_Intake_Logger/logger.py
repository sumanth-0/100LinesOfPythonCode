import json
import os
from datetime import datetime

# constants
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(SCRIPT_DIR, 'water_data.json')
DEFAULT_GOAL = 2000  # ml per day

# loads water data or create file if doesn't exist
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    else:
        return {
            "goal": DEFAULT_GOAL,
            "entries": []
        }
# Saves data to JSON file
def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)
        
# adds water to intake entry w/ timestamp
def add_water(amount):
    data = load_data()

    entry = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "time": datetime.now().strftime("%H:%M:%S"),
        "amount": amount
    }

    data["entries"].append(entry)
    save_data(data)
    return entry

# get total intake for today
def get_today_total():
    data = load_data()
    today = datetime.now().strftime("%Y-%m-%d")
    total = 0

    for entry in data["entries"]:
        if entry["date"] == today:
            total += entry["amount"]

    return total

# get all intake entries for today
def get_today_entries():
    data = load_data()
    today = datetime.now().strftime("%Y-%m-%d")
    today_entries = []

    for entry in data["entries"]:
        if entry["date"] == today:
            today_entries.append(entry)
    
    return today_entries

# get daily intake goal
def get_goal():
    data = load_data()
    return data["goal"]

# set new daily goal
def set_goal(new_goal):
    data = load_data()
    data["goal"] = new_goal
    save_data(data)

# get progress towards daily goal
def get_progress():
    total = get_today_total()
    goal = get_goal()

    if goal == 0:
        return 0
    
    percentage = (total / goal) * 100
    return round(percentage, 1)

# check if user needs a reminder
def needs_reminder():
    total = get_today_total()
    goal = get_goal()

    if total < (goal * 0.5):
        return True
    return False

# get all current stats
def get_stats():
    return {
        "total": get_today_total(),
        "goal": get_goal(),
        "progress": get_progress(),
        "entries": get_today_entries(),
        "needs_reminder": needs_reminder()
    }