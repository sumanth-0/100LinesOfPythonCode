from datetime import datetime

expenses = []

def add_expense():
    # --- Date Input ---
    while True:
        date_input = input("Enter the date (YYYY-MM-DD): ")
        try:
            date = datetime.strptime(date_input, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format! Please enter the date in YYYY-MM-DD format.")
    
    # --- Amount Input ---
    while True:
        amount_input = input("Enter the amount: ")
        try:
            amount = float(amount_input)
            if amount <= 0:
                print("Amount must be greater than zero.")
                continue
            break
        except ValueError:
            print("Invalid amount! Please enter a numeric value.")
    
    # --- Category Input ---
    category = input("Enter the category of expense: ").strip()
    if not category:
        category = "Uncategorized"
    
    # --- Save Expense ---
    expenses.append({
        "date": date,
        "amount": amount,
        "category": category
    })
    print("Expense added successfully!\n")

def view_expenses():
    if not expenses:
        print("No expenses recorded.\n")
        return
    for expense in expenses:
        formatted_date = expense['date'].strftime("%Y-%m-%d")
        print(f"Date: {formatted_date} | 💰 Amount: {expense['amount']:.2f} | 🏷️ Category: {expense['category']}")
    print("")

def summarize():
    summary = {}
    for expense in expenses:
        category = expense['category']
        amount = expense['amount']
        summary[category] = summary.get(category, 0) + amount
    return summary

def print_summary():
    summary = summarize()
    if not summary:
        print("No expenses to summarize.\n")
        return
    print("\nExpense Summary:")
    for category, total in summary.items():
        print(f" - {category}: ₹{total:.2f}")
    print("")

def check_overspending():
    if not expenses:
        print("No expenses to analyze.\n")
        return
    
    while True:
        limit_input = input("Enter the spending limit: ")
        try:
            limit = float(limit_input)
            if limit <= 0:
                print("Limit must be greater than zero.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
    
    summary = summarize()
    print("\nOverspending Check:")
    for category, total in summary.items():
        if total > limit:
            print(f"Overspending detected in '{category}': ₹{total:.2f} exceeds limit ₹{limit:.2f}")
    print("")

def main():
    while True:
        print("========= Expense Tracker =========")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Print Summary")
        print("4. Check Overspending")
        print("5. Exit")
        print("======================================")
        
        choice = input("Enter your choice: ")
        print("")

        try:
            if choice == '1':
                add_expense()
            elif choice == '2':
                view_expenses()
            elif choice == '3':
                print_summary()
            elif choice == '4':
                check_overspending()
            elif choice == '5':
                print("Exiting Expense Tracker. Goodbye!")
                break
            else:
                print("Invalid choice! Please try again.\n")
        except Exception as e:
            print(f"⚠️ An unexpected error occurred: {e}\n")

# Run program
if __name__ == "__main__":
    main()
