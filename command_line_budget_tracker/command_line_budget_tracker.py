#!/usr/bin/env python3
"""Command-Line Budget Tracker

A simple tool to log expenses and income by category with aggregation.
Data is saved to a JSON file for persistence.
"""
import json
import os
from datetime import datetime
from typing import Dict, List

BUDGET_FILE = "budget_data.json"

def load_data() -> Dict:
    """Load budget data from JSON file."""
    if os.path.exists(BUDGET_FILE):
        with open(BUDGET_FILE, 'r') as f:
            return json.load(f)
    return {"transactions": []}

def save_data(data: Dict) -> None:
    """Save budget data to JSON file."""
    with open(BUDGET_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def add_transaction(trans_type: str, amount: float, category: str, description: str = "") -> None:
    """Add a new transaction (income or expense)."""
    data = load_data()
    transaction = {
        "type": trans_type,
        "amount": amount,
        "category": category,
        "description": description,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    data["transactions"].append(transaction)
    save_data(data)
    print(f"✓ {trans_type.capitalize()} of ${amount:.2f} added to '{category}'")

def view_transactions() -> None:
    """Display all transactions."""
    data = load_data()
    if not data["transactions"]:
        print("No transactions found.")
        return
    print("\n" + "="*80)
    print(f"{'Date':<20} {'Type':<10} {'Category':<15} {'Amount':<10} {'Description'}")
    print("="*80)
    for t in data["transactions"]:
        print(f"{t['date']:<20} {t['type']:<10} {t['category']:<15} ${t['amount']:<9.2f} {t.get('description', '')}")
    print("="*80)

def show_summary() -> None:
    """Show summary of income and expenses by category."""
    data = load_data()
    if not data["transactions"]:
        print("No transactions to summarize.")
        return
    income_by_cat: Dict[str, float] = {}
    expense_by_cat: Dict[str, float] = {}
    for t in data["transactions"]:
        cat = t["category"]
        amt = t["amount"]
        if t["type"] == "income":
            income_by_cat[cat] = income_by_cat.get(cat, 0) + amt
        else:
            expense_by_cat[cat] = expense_by_cat.get(cat, 0) + amt
    print("\n" + "="*40)
    print("INCOME BY CATEGORY")
    print("="*40)
    total_income = 0
    for cat, amt in income_by_cat.items():
        print(f"{cat:<25} ${amt:>10.2f}")
        total_income += amt
    print("-"*40)
    print(f"{'Total Income':<25} ${total_income:>10.2f}")
    print("\n" + "="*40)
    print("EXPENSES BY CATEGORY")
    print("="*40)
    total_expense = 0
    for cat, amt in expense_by_cat.items():
        print(f"{cat:<25} ${amt:>10.2f}")
        total_expense += amt
    print("-"*40)
    print(f"{'Total Expenses':<25} ${total_expense:>10.2f}")
    print("\n" + "="*40)
    print(f"{'NET BALANCE':<25} ${total_income - total_expense:>10.2f}")
    print("="*40 + "\n")

def main():
    """Main menu loop."""
    while True:
        print("\n=== Command-Line Budget Tracker ===")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View All Transactions")
        print("4. Show Summary")
        print("5. Exit")
        choice = input("\nEnter your choice (1-5): ").strip()
        if choice == "1":
            amount = float(input("Enter amount: $"))
            category = input("Enter category: ").strip()
            description = input("Enter description (optional): ").strip()
            add_transaction("income", amount, category, description)
        elif choice == "2":
            amount = float(input("Enter amount: $"))
            category = input("Enter category: ").strip()
            description = input("Enter description (optional): ").strip()
            add_transaction("expense", amount, category, description)
        elif choice == "3":
            view_transactions()
        elif choice == "4":
            show_summary()
        elif choice == "5":
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
