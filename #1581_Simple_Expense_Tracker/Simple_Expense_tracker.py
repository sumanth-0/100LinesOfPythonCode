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
            if val <= 0: raise ValueError
            return val
        except ValueError:
            print("Enter a valid positive number.")

def get_date(prompt="Enter date (dd-mm-yyyy) or press Enter for today: "):
    date_str = input(prompt)
    if not date_str: return datetime.today().strftime("%d-%m-%Y")
    try:
        datetime.strptime(date_str, "%d-%m-%Y")
        return date_str
    except ValueError:
        print("Invalid date format. Use dd-mm-yyyy.")
        return get_date(prompt)

def add_expense():
    category = input("Enter category (e.g., Food, Travel): ").strip().title()
    amount = get_float("Enter amount (in Rs): Rs ")
    note = input("Enter an optional note: ").strip()
    date = get_date()
    expenses.append({"category": category, "amount": amount, "note": note, "date": date})
    save_data()
    print(f"Added Rs {amount:.2f} under {category} on {date}.")

def view_all_expenses():
    if not expenses:
        print("No expenses recorded yet!"); return
    print("\nAll Expenses:")
    total = sum(e["amount"] for e in expenses)
    for e in expenses:
        print(f"- {e['date']}: Rs {e['amount']:.2f} ({e['category']}) {e['note']}")
    print(f"Total Spent: Rs {total:.2f}")

def monthly_summary():
    if not expenses:
        print("No expenses recorded yet!"); return
    try:
        m, y = int(input("Enter month (1–12): ")), int(input("Enter year (e.g., 2025): "))
    except ValueError:
        print("Invalid input."); return monthly_summary()
    name, total = datetime(y, m, 1).strftime("%b-%Y"), 0
    print(f"\nExpense Summary for {name}:")
    for e in expenses:
        d = datetime.strptime(e["date"], "%d-%m-%Y")
        if d.month == m and d.year == y:
            print(f"- Rs {e['amount']:.2f} ({e['category']}) on {e['date']} {e['note']}")
            total += e["amount"]
    print(f"Total for {name}: Rs {total:.2f}")

def category_summary():
    if not expenses:
        print("No expenses recorded yet!"); return
    summary = {}
    for e in expenses:
        summary[e["category"]] = summary.get(e["category"], 0) + e["amount"]
    print("\nCategory-wise Summary:")
    for cat, amt in summary.items():
        print(f"- {cat}: Rs {amt:.2f}")
    print(f"Total: Rs {sum(summary.values()):.2f}")

def main():
    while True:
        print("\nSimple Expense Tracker")
        print("1. Add Expense\n2. View All Expenses\n3. Monthly Summary\n4. Category Summary\n5. Exit")
        ch = input("Enter choice (1–5): ").strip()
        if ch == "1": add_expense()
        elif ch == "2": view_all_expenses()
        elif ch == "3": monthly_summary()
        elif ch == "4": category_summary()
        elif ch == "5":
            save_data(); print("Thank you! Data saved successfully."); break
        else: print("Invalid choice. Try again.")
        
if __name__ == "__main__":
    main()