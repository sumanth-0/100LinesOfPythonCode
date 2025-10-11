# Command-Line Budget Tracker

A simple Python-based command-line tool for tracking income and expenses by category with aggregation and reporting features.

## Description

This budget tracker allows you to:
- Log income transactions with categories and descriptions
- Log expense transactions with categories and descriptions
- View all transactions with timestamps
- Get summary reports showing income and expenses by category
- Calculate net balance
- Persist all data in a JSON file for future sessions

## Features

- **Add Income**: Record income with amount, category, and optional description
- **Add Expense**: Record expenses with amount, category, and optional description
- **View Transactions**: Display all logged transactions in a formatted table
- **Show Summary**: View aggregated income and expenses by category with totals and net balance
- **Data Persistence**: All data is automatically saved to `budget_data.json`

## Installation

No additional dependencies required! Just Python 3.6+

## Usage

Run the script:

```bash
python command_line_budget_tracker.py
```

You'll be presented with a menu:

```
=== Command-Line Budget Tracker ===
1. Add Income
2. Add Expense
3. View All Transactions
4. Show Summary
5. Exit

Enter your choice (1-5):
```

### Example Workflow

1. **Add Income**:
   - Select option 1
   - Enter amount: `3000`
   - Enter category: `Salary`
   - Enter description: `Monthly salary`

2. **Add Expense**:
   - Select option 2
   - Enter amount: `500`
   - Enter category: `Groceries`
   - Enter description: `Weekly shopping`

3. **View Summary**:
   - Select option 4 to see income and expenses by category with net balance

## Data Storage

All transactions are stored in `budget_data.json` in the same directory as the script. The file is created automatically on first use.

## Sample Output

```
INCOME BY CATEGORY
========================================
Salary                    $   3000.00
----------------------------------------
Total Income              $   3000.00

EXPENSES BY CATEGORY
========================================
Groceries                 $    500.00
Rent                      $   1200.00
----------------------------------------
Total Expenses            $   1700.00

========================================
NET BALANCE               $   1300.00
========================================
```

## Contributing

This project is part of the [100 Lines of Python Code](https://github.com/sumanth-0/100LinesOfPythonCode) repository. Contributions are welcome!

## License

Feel free to use and modify this code for your personal projects.

---

**Closes #661**
