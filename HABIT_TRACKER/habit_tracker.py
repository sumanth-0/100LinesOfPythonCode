import json
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

DATA_FILE = "data/habits.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file)

def add_habit(habit_name):
    data = load_data()
    if habit_name not in data:
        data[habit_name] = []
    save_data(data)

def mark_habit(habit_name):
    data = load_data()
    if habit_name in data:
        today = datetime.now().strftime("%Y-%m-%d")
        if today not in data[habit_name]:
            data[habit_name].append(today)
    save_data(data)

def plot_habit(habit_name):
    data = load_data()
    if habit_name in data:
        dates = [datetime.strptime(date, "%Y-%m-%d") for date in data[habit_name]]
        dates.sort()
        streaks = []
        current_streak = 0
        for i in range(1, len(dates)):
            if dates[i] - dates[i - 1] == timedelta(days=1):
                current_streak += 1
            else:
                streaks.append(current_streak + 1)
                current_streak = 0
        streaks.append(current_streak + 1)
        
        plt.bar(range(len(streaks)), streaks)
        plt.xlabel("Streak Number")
        plt.ylabel("Days")
        plt.title(f"Habit Streaks for '{habit_name}'")
        plt.show()

# Example usage
add_habit("Exercise")
mark_habit("Exercise")
plot_habit("Exercise")
