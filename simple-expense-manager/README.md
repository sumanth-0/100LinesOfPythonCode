# Simple Expense Manager

A lightweight CLI tool for tracking and analyzing personal expenses with category-wise summaries, statistics, and data export capabilities.

## Features

- Add daily expenses with categories and descriptions
- View expense summaries by category
- Export data to CSV format (automatic .csv extension handling)
- View expense statistics including:
  - Average daily spending
  - Most expensive category
  - Total expenses
- Automatic date tracking
- Data persistence using JSON storage
- Pre-defined expense categories
- Under 100 lines of well-documented code

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
   - View Summary (2): See expenses by category
   - Export to CSV (3): Save expenses to a CSV file
   - View Stats (4): See spending statistics
   - Exit (5): Close the application

## Examples

### Adding an Expense
```
Categories: ['Food', 'Transport', 'Bills', 'Entertainment', 'Other']
Amount: 25.50
Category: Food
Description: Lunch at cafe
Expense added successfully!
```

### Viewing Statistics
```
Statistics:
Avg/day: $27.83
Most spent: Food
Total: $195.50
```

### Exporting Data
```
Export filename (with or without .csv): march_expenses
Export complete! Available in the current directory.
```

## Data Storage

- Expenses are stored in `expenses.json` (automatic creation)
- Export to CSV available for spreadsheet analysis
- CSV files include: date, amount, category, and description

## File Structure

```
simple-expense-manager/
├── expense_manager.py  # Main program with docstrings
├── expenses.json      # Data storage
└── README.md         # Documentation
```

## Requirements

- Python 3.x
- No additional dependencies required
- Works on all major operating systems