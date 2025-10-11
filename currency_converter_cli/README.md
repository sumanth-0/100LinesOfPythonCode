# Currency Converter CLI

A simple command-line currency converter tool that fetches real-time exchange rates from a free API.

## Features

- Real-time currency conversion using exchangerate.host API
- Support for 16 common currencies (USD, EUR, GBP, JPY, AUD, CAD, CHF, CNY, INR, MXN, BRL, ZAR, RUB, KRW, SGD, NZD)
- User-friendly CLI interface
- Display exchange rates along with converted amounts
- Input validation for amounts and currency codes

## Requirements

- Python 3.6 or higher
- `requests` library

## Installation

1. Clone the repository:
```bash
git clone https://github.com/sumanth-0/100LinesOfPythonCode.git
cd 100LinesOfPythonCode/currency_converter_cli
```

2. Install required dependencies:
```bash
pip install requests
```

## Usage

Run the script:
```bash
python currency_converter_cli.py
```

The program will:
1. Display a list of supported currencies
2. Prompt you to enter the amount to convert
3. Ask for the source currency code (e.g., USD)
4. Ask for the target currency code (e.g., EUR)
5. Display the converted amount and exchange rate

### Example

```
=== Currency Converter CLI ===

Common currencies:
 1. USD   2. EUR   3. GBP   4. JPY  
 5. AUD   6. CAD   7. CHF   8. CNY  
 9. INR  10. MXN  11. BRL  12. ZAR  
13. RUB  14. KRW  15. SGD  16. NZD  
================================

Enter amount: 100
From currency (e.g., USD): USD
To currency (e.g., EUR): EUR

Converting 100 USD to EUR...

100.00 USD = 92.50 EUR

Exchange rate: 1 USD = 0.9250 EUR
```

## API

This tool uses the free [exchangerate.host](https://exchangerate.host/) API, which provides:
- Real-time exchange rates
- No API key required
- Support for 170+ currencies

## Error Handling

- Validates positive numeric inputs for amounts
- Handles network errors gracefully
- Checks for valid currency codes
- Supports keyboard interrupt (Ctrl+C) to exit

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Issue Reference

This project solves issue [#694](https://github.com/sumanth-0/100LinesOfPythonCode/issues/694)
