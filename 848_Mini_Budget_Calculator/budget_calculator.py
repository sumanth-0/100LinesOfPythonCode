import json
import os
from datetime import datetime
from typing import Dict, List, Optional
import argparse

class BudgetCalculator:
    """A simple budget calculator to track expenses by category."""
    
    def __init__(self, data_file: str = 'budget_data.json'):
        self.data_file = data_file
        self.categories = [
            'Food', 'Transportation', 'Housing', 
            'Utilities', 'Entertainment', 'Shopping', 'Others'
        ]
        self.data = self._load_data()
    
    def _load_data(self) -> Dict:
        """Load existing budget data from file or initialize new data structure."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                print("Warning: Could not load existing data. Starting fresh.")
        
        # Initialize new data structure
        return {
            'expenses': [],
            'settings': {
                'current_period': 'monthly',  # or 'weekly'
                'currency': '₹'  # Default to Indian Rupee
            }
        }
    
    def _save_data(self):
        """Save budget data to file."""
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.data, f, indent=2)
        except IOError as e:
            print(f"Error saving data: {e}")
    
    def add_expense(self, amount: float, category: str, description: str = ''):
        """Add a new expense to the budget."""
        if amount <= 0:
            print("Error: Amount must be positive")
            return False
            
        if category not in self.categories:
            print(f"Error: Invalid category. Choose from: {', '.join(self.categories)}")
            return False
            
        expense = {
            'id': len(self.data['expenses']) + 1,
            'amount': amount,
            'category': category,
            'description': description,
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        self.data['expenses'].append(expense)
        self._save_data()
        print(f"Added expense of {self.data['settings']['currency']}{amount:.2f} to {category}")
        return True
    
    def get_summary(self, period: str = None) -> Dict[str, float]:
        """Get expense summary by category for the specified period."""
        period = period or self.data['settings']['current_period']
        summary = {category: 0.0 for category in self.categories}
        
        for expense in self.data['expenses']:
            summary[expense['category']] += expense['amount']
        
        return summary
    
    def display_summary(self, period: str = None):
        """Display a formatted summary of expenses."""
        period = period or self.data['settings']['current_period']
        summary = self.get_summary(period)
        total = sum(summary.values())
        
        print(f"\n{'='*40}")
        print(f"{period.capitalize()} Expense Summary".center(40))
        print("="*40)
        
        for category, amount in summary.items():
            if amount > 0:
                print(f"{category + ':':<15} {self.data['settings']['currency']}{amount:>10.2f}")
        
        print("-"*40)
        print(f"{'TOTAL:':<15} {self.data['settings']['currency']}{total:>10.2f}")
        print("="*40 + "\n")
    
    def set_period(self, period: str):
        """Set the budget period (weekly/monthly)."""
        if period.lower() in ['weekly', 'monthly']:
            self.data['settings']['current_period'] = period.lower()
            self._save_data()
            print(f"Budget period set to {period.lower()}")
        else:
            print("Error: Period must be 'weekly' or 'monthly'")

def main():
    parser = argparse.ArgumentParser(description='Mini Budget Calculator')
    subparsers = parser.add_subparsers(dest='command', help='Command to execute')
    
    # Add expense command
    add_parser = subparsers.add_parser('add', help='Add a new expense')
    add_parser.add_argument('amount', type=float, help='Expense amount')
    add_parser.add_argument('category', help='Expense category')
    add_parser.add_argument('-d', '--description', default='', help='Expense description')
    
    # Show summary command
    summary_parser = subparsers.add_parser('summary', help='Show expense summary')
    summary_parser.add_argument('-p', '--period', choices=['weekly', 'monthly'], 
                              help='Time period for summary')
    
    # Set period command
    period_parser = subparsers.add_parser('set-period', help='Set budget period')
    period_parser.add_argument('period', choices=['weekly', 'monthly'], 
                             help='Budget period (weekly/monthly)')
    
    args = parser.parse_args()
    budget = BudgetCalculator()
    
    if args.command == 'add':
        budget.add_expense(args.amount, args.category, args.description)
    elif args.command == 'summary':
        budget.display_summary(args.period)
    elif args.command == 'set-period':
        budget.set_period(args.period)
    else:
        # Show help if no command provided
        parser.print_help()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")
