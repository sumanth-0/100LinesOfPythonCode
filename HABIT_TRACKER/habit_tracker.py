from datetime import datetime

class HabitTracker:
    def __init__(self):
        self.habits = {}
    
    def add_habit(self, habit_name):
        if habit_name in self.habits:
            print(f"Habit '{habit_name}' already exists.")
        else:
            self.habits[habit_name] = []
            print(f"Habit '{habit_name}' added.")

    def log_habit(self, habit_name):
        if habit_name not in self.habits:
            print(f"Habit '{habit_name}' not found. Please add it first.")
        else:
            today = datetime.now().date()
            if today not in self.habits[habit_name]:
                self.habits[habit_name].append(today)
                print(f"Logged '{habit_name}' for today.")
            else:
                print(f"'{habit_name}' has already been logged for today.")

    def habit_streak(self, habit_name):
        if habit_name not in self.habits:
            print(f"Habit '{habit_name}' not found.")
            return 0
        streak = 0
        today = datetime.now().date()
        dates = sorted(self.habits[habit_name], reverse=True)
        
        for i in range(len(dates) - 1):
            if (dates[i] - dates[i + 1]).days == 1:
                streak += 1
            else:
                break
        return streak + 1

    def show_habits(self):
        print("Habit Log Summary:")
        for habit, dates in self.habits.items():
            print(f"- {habit}: {len(dates)} days logged, Current Streak: {self.habit_streak(habit)} days")

if __name__ == "__main__":
    tracker = HabitTracker()
    print("Habit Tracker CLI")
    while True:
        action = input("Choose an action (add, log, show, exit): ").lower()
        if action == "add":
            habit = input("Enter habit name to add: ")
            tracker.add_habit(habit)
        elif action == "log":
            habit = input("Enter habit name to log: ")
            tracker.log_habit(habit)
        elif action == "show":
            tracker.show_habits()
        elif action == "exit":
            print("Exiting Habit Tracker.")
            break
        else:
            print("Invalid action. Please choose from (add, log, show, exit).")
