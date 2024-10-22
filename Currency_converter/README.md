Currency Converter

A simple Python-based currency converter that uses the European Central Bank (ECB) historical exchange rates via the currency_converter library. This tool converts a specified amount from one currency to another using embedded data.
Features

    Converts currency amounts using ECB exchange rates.
    Provides historical conversion based on the latest available data.
    Supports common currency symbols for user-friendly display.

Requirements

    Python 3.x
    currency_converter package

Installation

    Clone or download this repository to your local machine.

    Install the required Python package using pip:

    bash

    pip install --user currencyconverter

    This installs the currency_converter package, which uses the ECB historical exchange rates for currency conversion.

    Ensure you have Python 3 installed on your machine.

Usage

    Run the Python script:

    bash

python currency_converter_app.py

Follow the prompts:

    Enter the base currency (e.g., USD, EUR).
    Enter the target currency (e.g., INR, GBP).
    Enter the amount you want to convert from the base currency.

The program will display the converted amount along with the corresponding currency symbols, e.g.:

bash

    $100.00 USD = ₹6745.50 INR

Example

arduino

Currency Converter (using ECB historical data)
Enter the base currency (e.g., USD, EUR): USD
Enter the target currency (e.g., INR, GBP): INR
Enter amount in USD: 100

$100.00 USD = ₹6745.50 INR

Error Handling

    The program catches invalid inputs for the amount or unsupported currencies and gracefully handles them by displaying appropriate error messages.

How it Works

    The script uses the currency_converter package to fetch currency conversion rates based on historical ECB data.
    It does not require an internet connection to perform conversions, making it reliable for offline use as long as the rates are up-to-date.

