# Simple Expense Manager

A command-line tool to track and manage daily expenses with category-wise summaries.

## Features

- Add daily expenses with categories and descriptions
- View expense summaries by category
- Automatic date tracking for each expense
- Data persistence using JSON storage
- Pre-defined expense categories
- Total expense calculation

## Categories

- Food
- Transport
- Bills
- Entertainment
- Other

## Usage

1. Run the script:
```bash
python expense_manager.py
```

2. Choose from the following options:
   - Add Expense (1): Enter amount, category, and description
   - View Summary (2): See expenses by category and total
   - Exit (3): Close the application

## Example

```
1. Add Expense
2. View Summary
3. Exit
Select an option (1-3): 1

Categories: ['Food', 'Transport', 'Bills', 'Entertainment', 'Other']
Enter amount: 25.50
Enter category: Food
Enter description: Lunch at cafe
Expense added successfully!
```

## Data Storage

All expenses are stored in `expenses.json` in the same directory. The file is automatically created when you add your first expense.

## File Structure

```
simple-expense-manager/
├── expense_manager.py
├── expenses.json
└── README.md
```

## Requirements

- Python 3.x
- No additional dependencies required

## Extending the Project

Future improvements could include:
- Date range filtering
- Expense editing and deletion
- Monthly budgets
- Data visualization
- Export to CSV functionality