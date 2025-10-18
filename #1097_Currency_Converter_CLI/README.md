# Currency Converter CLI

## Description
A command-line interface tool to convert amounts between different currencies using the Free Currency API.

## Features
- Real-time currency conversion
- Support for multiple currencies
- User-friendly CLI interface
- Exchange rate display
- Timestamp for each conversion

## Requirements
- Python 3.6 or higher
- `requests` library

## Installation

1. Install required dependencies:
```bash
pip install requests
```

2. Get a free API key from [Free Currency API](https://freecurrencyapi.com/)

3. Update the API key in the `currency_converter.py` file:
```python
self.api_key = "fca_live_YOUR_API_KEY_HERE"  # Replace with your API key
```

## Usage

Run the script:
```bash
python currency_converter.py
```

Follow the prompts:
1. Enter the amount to convert
2. Enter the source currency code (e.g., USD)
3. Enter the target currency code (e.g., EUR)

### Example
```
Currency Converter CLI
======================================
Enter amount to convert: 100
From currency (e.g., USD): USD
To currency (e.g., EUR): EUR

Fetching exchange rates...

======================================
Currency Conversion Result
======================================
Amount: 100.00 USD
Converted: 92.50 EUR
Exchange Rate: 1 USD = 0.925000 EUR
Date: 2025-10-18 14:05:00
======================================
```

## Supported Currency Codes
Common currency codes include:
- USD - US Dollar
- EUR - Euro
- GBP - British Pound
- JPY - Japanese Yen
- AUD - Australian Dollar
- CAD - Canadian Dollar
- CHF - Swiss Franc
- CNY - Chinese Yuan
- INR - Indian Rupee

## Error Handling
- Validates positive amounts
- Checks currency code format (3 letters)
- Handles API connection errors
- Provides clear error messages

## Issue Reference
This project addresses Issue #1097 - Currency Converter CLI

## Author
Contributed as part of the 100 Lines of Python Code project
