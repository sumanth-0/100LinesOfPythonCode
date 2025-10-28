import json
from datetime import datetime

DATA_FILE = "expenses.json"

try:
    with open(DATA_FILE, "r") as f:
        expenses = json.load(f)
except FileNotFoundError:
    expenses = []
def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=4)

def get_float(prompt):
    while True:
        try:
            val = float(input(prompt))
            if val <= 0:
                raise ValueError
            return val
        except ValueError:
            print("Enter a valid positive number.")

def get_date(prompt="Enter date (dd-mm-yyyy) or press Enter for today: "):
    date_str = input(prompt)
    if not date_str:
        return datetime.today().strftime("%d-%m-%Y")
    try:
        datetime.strptime(date_str, "%d-%m-%Y")
        return date_str
    except ValueError:
        print(" This is an invalid date format. Use dd-mm-yyyy.")
        return get_date(prompt)
def add_expense():
    category = input("Enter a category (e.g., Food, Travel, Bills): ").strip().title()
    amount = get_float("Enter the amount(in rs): Rs ")
    note = input("Enter an optional note: ").strip()
    date = get_date()

    expense = {"category": category, "amount": amount, "note": note, "date": date}
    expenses.append(expense)
    save_data()
    print(f"Added Rs {amount:.2f} under {category} on {date}.")

def view_all_expenses():
    if not expenses:
        print("there's no expenses recorded yet!")
        return

    print("\nAll Expenses:")
    total = 0
    for e in expenses:
        print(f"- {e['date']}: Rs {e['amount']:.2f} ({e['category']}) {e['note']}")
        total += e["amount"]
    print(f"Total amount Spent: Rs {total:.2f}")

def monthly_summary():
    if not expenses:
        print("No expenses recorded yet!")
        return

    try:
        month = int(input("Enter a month number (1–12): "))
        year = int(input("Enter a year (e.g., 2025): "))
    except ValueError:
        print("Invalid input.")
        return monthly_summary()

    month_name = datetime(year, month, 1).strftime("%b-%Y")
    print(f"\nExpense Summary for {month_name}:")
    total = 0
    for e in expenses:
        d = datetime.strptime(e["date"], "%d-%m-%Y")
        if d.month == month and d.year == year:
            print(f"- Rs {e['amount']:.2f} ({e['category']}) on {e['date']} {e['note']}")
            total += e["amount"]
    print(f"Total for {month_name}: Rs {total:.2f}")

def category_summary():
    if not expenses:
        print("No expenses recorded yet!")
        return

    summary = {}
    for e in expenses:
        summary[e["category"]] = summary.get(e["category"], 0) + e["amount"]

    print("\nCategory-wise Summary:")
    for cat, amt in summary.items():
        print(f"- {cat}: Rs {amt:.2f}")
    print(f"Total: Rs {sum(summary.values()):.2f}")

def main():
    while True:
        print("\n-------------------")
        print("💰 Simple Expense Tracker")
        print("-------------------")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Monthly Summary")
        print("4. Category Summary")
        print("5. Exit")
        print("-------------------")

        choice = input("Enter choice (1–5): ").strip()
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_all_expenses()
        elif choice == "3":
            monthly_summary()
        elif choice == "4":
            category_summary()
        elif choice == "5":
            save_data()
            print("Thank you! Your Data is saved successfully.")
            break
        else:
            print("Invalid choice. Please Try again.")

if __name__ == "__main__":
    main()
