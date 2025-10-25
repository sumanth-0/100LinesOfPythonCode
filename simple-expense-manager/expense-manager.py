from datetime import datetime
import json
from pathlib import Path
import os

class ExpenseManager:
    def __init__(self):
        self.expenses = []
        self.categories = ['Food', 'Transport', 'Bills', 'Entertainment', 'Other']
        self.data_file = 'expenses.json'
        self.load_expenses()

    def load_expenses(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                self.expenses = json.load(f)

    def save_expenses(self):
        with open(self.data_file, 'w') as f:
            json.dump(self.expenses, f, indent=4)

    def add_expense(self, amount, category, description):
        if category not in self.categories:
            raise ValueError(f"Category must be one of {self.categories}")
        
        expense = {
            'date': datetime.now().strftime('%Y-%m-%d'),
            'amount': float(amount),
            'category': category,
            'description': description
        }
        self.expenses.append(expense)
        self.save_expenses()

    def get_summary(self):
        totals = {category: 0 for category in self.categories}
        for expense in self.expenses:
            totals[expense['category']] += expense['amount']
        return totals

def main():
    manager = ExpenseManager()
    
    while True:
        print("\n1. Add Expense")
        print("2. View Summary")
        print("3. Exit")
        
        choice = input("Select an option (1-3): ")
        
        if choice == '1':
            print("\nCategories:", manager.categories)
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            description = input("Enter description: ")
            
            try:
                manager.add_expense(amount, category, description)
                print("Expense added successfully!")
            except ValueError as e:
                print(f"Error: {e}")
                
        elif choice == '2':
            summary = manager.get_summary()
            print("\nExpense Summary:")
            total = 0
            for category, amount in summary.items():
                print(f"{category}: ${amount:.2f}")
                total += amount
            print(f"\nTotal Expenses: ${total:.2f}")
            
        elif choice == '3':
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()