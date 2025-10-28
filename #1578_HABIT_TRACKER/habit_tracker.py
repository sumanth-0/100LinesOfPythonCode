import pandas as pd
from datetime import datetime
import os

date_format = "%d-%m-%Y"
month_format = "%b-%Y"
data_file = "HabitTracker.xlsx"
timestamp_file = "last_run.txt"

if not os.path.exists(data_file):
    df = pd.DataFrame({
        "SrNo": range(1, 11),
        "Habit": [
            "Exercise", "Read Books", "Meditation", "Wake Up Early", "Drink Water",
            "Journal Writing", "Avoid Social Media", "Study", "Sleep Early", "Walk 10k Steps"
        ]
    })
    df.to_excel(data_file, index=False)
else:
    df = pd.read_excel(data_file)

formatted_date = datetime.now().strftime(month_format)
if formatted_date not in df.columns:
    df[formatted_date] = 0
    df.to_excel(data_file, index=False)

def get_last_run_time():
    return open(timestamp_file).read().strip() if os.path.exists(timestamp_file) else "First run."

def update_last_run_time():
    open(timestamp_file, "w").write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def showHabits():
    print("\nYour Habits:")
    for i, h in enumerate(df["Habit"], 1):
        print(f"{i}) {h}")

def getHabit():
    while True:
        try:
            n = int(input("Enter Habit Number (1–10): "))
            if 1 <= n <= 10:
                return n
            
            else:
                print("Invalid. Enter between 1–10.")
        except ValueError:
            print("Enter a valid number.")

def markHabit():
    showHabits()
    n = getHabit()
    df.loc[df["SrNo"] == n, formatted_date] += 1
    df.to_excel(data_file, index=False)
    print(f"Habit '{df.loc[df['SrNo']==n,'Habit'].values[0]}' marked for today!")

def viewMonthlyReport():
    print(f"\nHabit Report for {formatted_date}:")
    print(df[["Habit", formatted_date]])
    print(f"\nTotal Habits Tracked: {len(df)}")

def resetMonth():
    confirm = input(f"Are you sure you want to reset {formatted_date}? (y/n): ").lower()
    if confirm == "y":
        df[formatted_date] = 0
        df.to_excel(data_file, index=False)
        print(f"Data for {formatted_date} reset successfully.")
        
if __name__ == "__main__":
    print("Last run:", get_last_run_time())
    while True:
        print("\n1. Mark Habit  2. View Monthly Report  3. Reset Month  4. Exit")
        update_last_run_time()
        choice = input("Enter (1–4): ").strip()

        if choice == "1":
            markHabit()
        elif choice == "2":
            viewMonthlyReport()
        elif choice == "3":
            resetMonth()
        elif choice == "4":
            exit()
        else:
            print("Invalid choice.")
