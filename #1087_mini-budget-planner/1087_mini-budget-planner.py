def main():
    print(" Mini Budget Planner ")
    print("Enter your expenses by category.")
    print("Type 'done' when finished.\n")

    expenses = {}

    while True:
        category = input("Enter category (e.g., Food, Travel, Bills or 'done' to finish): ").strip().capitalize()
        if category.lower() == "done":
            break

        try:
            amount = float(input(f"Enter amount for {category}: ₹"))
        except ValueError:
            print(" Invalid amount, please enter a number.\n")
            continue

        expenses[category] = expenses.get(category, 0) + amount
        print(f" Added ₹{amount:.2f} to {category}.\n")

    print("\n Expense Summary:")
    total = 0
    for cat, amt in expenses.items():
        print(f" - {cat}: ₹{amt:.2f}")
        total += amt

    print(f"\n Total Spent: ₹{total:.2f}")
    print(" Budget tracking complete!")

if __name__ == "__main__":
    main()
