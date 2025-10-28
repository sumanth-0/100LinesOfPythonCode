"""Simple Expense Manager - Track daily expenses with categories, export to CSV, and view statistics.
Features: expense tracking, category summaries, CSV export, statistics, JSON storage

Usage: python expense-manager.py."""

from datetime import datetime
import json, os, csv
from statistics import mean

class ExpenseManager:
    """Manages personal expenses with category-based tracking and analysis."""
    
    def __init__(self):
        """Initialize manager with default categories and empty expense list."""
        self.expenses = []
        self.categories = ['Food', 'Transport', 'Bills', 'Entertainment', 'Other']
        self.data_file = 'expenses.json'
        self.load_expenses()

    def load_expenses(self):
        """Load existing expenses from JSON file."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f: self.expenses = json.load(f)

    def save_expenses(self):
        """Save current expenses to JSON file."""
        with open(self.data_file, 'w') as f: json.dump(self.expenses, f, indent=4)

    def add_expense(self, amount, category, description):
        """Add new expense with validation. Args: amount (float), category (str), description (str)."""
        if category not in self.categories: raise ValueError(f"Category must be one of {self.categories}")
        self.expenses.append({'date': datetime.now().strftime('%Y-%m-%d'), 'amount': float(amount),
                            'category': category, 'description': description})
        self.save_expenses()

    def get_summary(self):
        """Return dict of total expenses by category."""
        return {cat: sum(e['amount'] for e in self.expenses if e['category'] == cat) for cat in self.categories}
    
    def export_csv(self, filepath):
        """Export expenses to CSV. Adds .csv extension if missing."""
        if not filepath.lower().endswith('.csv'): filepath += '.csv'
        with open(filepath, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['date','amount','category','description'])
            writer.writeheader(); writer.writerows(self.expenses)
            
    def get_stats(self):
        """Calculate expense statistics: average per day, highest category, total."""
        expenses = [e['amount'] for e in self.expenses]
        summary = self.get_summary()
        return {'avg_per_day': mean(expenses) if expenses else 0,
                'most_spent_on': max(summary.items(), key=lambda x:x[1])[0] if summary else None,
                'total': sum(expenses)}

def main():
    """Run the expense manager CLI interface."""
    manager = ExpenseManager()
    while True:
        print("\n1. Add Expense\n2. View Summary\n3. Export to CSV\n4. View Stats\n5. Exit")
        try:
            choice = input("Select option (1-5): ")
            if choice == '1':
                print("\nCategories:", manager.categories)
                manager.add_expense(float(input("Amount: ")), input("Category: "), input("Description: "))
                print("Expense added successfully!")
            elif choice == '2':
                print("\nExpense Summary:")
                print('\n'.join(f"{cat}: ${amt:.2f}" for cat, amt in manager.get_summary().items()))
            elif choice == '3':
                manager.export_csv(input("Export filename (with or without .csv): "))
                print("Export complete! Available in the current directory.")
            elif choice == '4':
                s = manager.get_stats()
                print(f"\nStatistics:\nAvg/day: ${s['avg_per_day']:.2f}\nMost spent: {s['most_spent_on']}\nTotal: ${s['total']:.2f}")
            elif choice == '5': break
        except Exception as e: print(f"Error: {e}")

if __name__ == "__main__": 
    main()