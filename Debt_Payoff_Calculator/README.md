# Personal Finance Debt Payoff Calculator & Strategy Planner

## Description
A Python-based debt payoff calculator that helps you strategically plan your debt repayment. This tool compares two popular debt repayment strategies:
- **Debt Avalanche**: Pay off debts with the highest interest rate first (saves more money)
- **Debt Snowball**: Pay off debts with the lowest balance first (provides quick wins)

## Features
- Calculate payoff time for multiple debts
- Compare Avalanche vs Snowball strategies
- Track total interest paid
- Visualize debt payoff timeline
- Get personalized recommendations

## Usage
```bash
python debt_payoff_calculator.py
```

## Input Required
- Number of debts
- For each debt:
  - Name (e.g., "Credit Card", "Student Loan")
  - Current balance
  - Annual interest rate (%)
  - Minimum monthly payment
- Extra monthly payment amount (optional)

## Output
The calculator provides:
1. **Avalanche Strategy Results**: Total payoff time and order of debt elimination
2. **Snowball Strategy Results**: Total payoff time and order of debt elimination
3. **Recommendation**: Guidance on which strategy may work best for your situation

## Example
```
Personal Finance Debt Payoff Calculator
==================================================
Number of debts: 2

Debt #1:
  Name: Credit Card
  Balance: $5000
  Interest Rate (%): 18.5
  Minimum Payment: $150

Debt #2:
  Name: Student Loan
  Balance: $10000
  Interest Rate (%): 6.5
  Minimum Payment: $200

Extra monthly payment: $300

==================================================
AVALANCHE STRATEGY (Highest Interest First)
==================================================
Total payoff time: 24 months (2y 0m)
  Credit Card: Paid off in month 12
  Student Loan: Paid off in month 24

==================================================
SNOWBALL STRATEGY (Lowest Balance First)
==================================================
Total payoff time: 25 months (2y 1m)
  Credit Card: Paid off in month 11
  Student Loan: Paid off in month 25

==================================================
Recommendation: Avalanche saves more on interest, Snowball provides quick wins.
```

## Benefits
- **Avalanche Method**: Minimizes total interest paid, faster overall debt freedom
- **Snowball Method**: Provides psychological motivation through quick wins

## Requirements
- Python 3.6+
- No external dependencies required (uses only standard library)

## Related to Issue
Solves issue #630: Personal Finance Debt Payoff Calculator & Strategy Planner

## License
This project follows the repository's license.
