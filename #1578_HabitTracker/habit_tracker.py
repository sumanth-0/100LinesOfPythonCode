
import csv
from datetime import datetime

FILE = "HabitTracker.csv"

def init_file():
    try:
        open(FILE, "r").close()
    except FileNotFoundError:
        with open(FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Habit", "Status"])

def mark_habit(habit):
    today = datetime.now().strftime("%Y-%m-%d")
    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([today, habit, "Done"])
    print(f" {habit} marked as done for {today}")

def show_report():
    try:
        with open(FILE, "r") as f:
            reader = csv.DictReader(f)
            data = list(reader)
    except FileNotFoundError:
        print("No records found.")
        return

    if not data:
        print("No records found.")
        return

    month = datetime.now().strftime("%Y-%m")
    habits = {}
    for row in data:
        if row["Date"].startswith(month):
            habits[row["Habit"]] = habits.get(row["Habit"], 0) + 1

    if not habits:
        print("No entries for this month yet.")
        return

    print("\n Monthly Report:")
    for habit, count in habits.items():
        print(f"{habit}: {count} days completed")

def reset_data():
    with open(FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "Habit", "Status"])
    print(" All data reset successfully!")

# Main menu
def main():
    init_file()
    print("\n🌱 Welcome to the Habit Tracker!\n")

    while True:
        print("\n--- MENU ---")
        print("1. Mark a habit as done")
        print("2. View monthly report")
        print("3. Reset data")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            habit = input("Enter habit name: ").strip()
            mark_habit(habit)
        elif choice == "2":
            show_report()
        elif choice == "3":
            reset_data()
        elif choice == "4":
            print(" Goodbye! Keep building good habits.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
