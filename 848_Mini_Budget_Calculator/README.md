# Mini Budget Calculator

A simple command-line tool to track your weekly or monthly expenses by category. This Python script helps you keep track of your spending habits and view summaries of your expenses.

## Features

- Track expenses by category (Food, Transportation, Housing, etc.)
- Switch between weekly and monthly budget views
- View expense summaries with totals per category
- Simple command-line interface
- Persistent data storage (saves to JSON file)
- Support for multiple currencies

## Requirements

- Python 3.6+
- No external dependencies required

## Installation

1. Clone the repository or download the `budget_calculator.py` file
2. Make the script executable (optional):
   ```bash
   chmod +x budget_calculator.py
   ```

## Usage

### Add an expense
```bash
python budget_calculator.py add <amount> <category> [--description "Description"]
```

Example:
```bash
python budget_calculator.py add 1500 Food --description "Weekly groceries"
```

### View expense summary
```bash
python budget_calculator.py summary [--period weekly|monthly]
```

### Set budget period
```bash
python budget_calculator.py set-period weekly
# or
python budget_calculator.py set-period monthly
```

## Available Categories

- Food
- Transportation
- Housing
- Utilities
- Entertainment
- Shopping
- Others

## Example Workflow

1. Set your budget period to weekly:
   ```bash
   python budget_calculator.py set-period weekly
   ```

2. Add some expenses:
   ```bash
   python budget_calculator.py add 1200 Food
   python budget_calculator.py add 500 Transportation
   python budget_calculator.py add 3000 Housing
   ```

3. View your weekly summary:
   ```bash
   python budget_calculator.py summary
   ```

## Data Storage

Your expense data is stored in a `budget_data.json` file in the same directory as the script. You can back up this file or move it to another location if needed.

## Customization

You can modify the `categories` list in the script to add or remove expense categories as needed.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## License

This project is open source and available under the [MIT License](LICENSE).
