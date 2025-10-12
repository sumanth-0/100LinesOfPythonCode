#!/usr/bin/env python3
"""
Currency Converter CLI
Converts between currencies using exchange rates from an API.
"""

import requests
import sys

# Free API endpoint (no key required)
API_URL = "https://api.exchangerate.host/latest"

# Common currency codes
CURRENCIES = [
    'USD', 'EUR', 'GBP', 'JPY', 'AUD', 'CAD', 'CHF', 'CNY', 
    'INR', 'MXN', 'BRL', 'ZAR', 'RUB', 'KRW', 'SGD', 'NZD'
]

def get_exchange_rates(base_currency='USD'):
    """Fetch exchange rates from API."""
    try:
        params = {'base': base_currency}
        response = requests.get(API_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if data.get('success', True):
            return data.get('rates', {})
        else:
            print(f"Error: {data.get('error', 'Unknown error')}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return None

def convert_currency(amount, from_curr, to_curr):
    """Convert amount from one currency to another."""
    if from_curr == to_curr:
        return amount
    
    # Get rates with from_currency as base
    rates = get_exchange_rates(from_curr)
    
    if rates and to_curr in rates:
        converted = amount * rates[to_curr]
        return converted
    else:
        print(f"Error: Could not convert {from_curr} to {to_curr}")
        return None

def display_menu():
    """Display available currencies."""
    print("\n=== Currency Converter CLI ===")
    print("\nCommon currencies:")
    for i, curr in enumerate(CURRENCIES, 1):
        print(f"{i:2d}. {curr}", end="  ")
        if i % 4 == 0:
            print()
    print("\n" + "="*32)

def main():
    """Main CLI interface."""
    display_menu()
    
    try:
        # Get amount
        while True:
            try:
                amount = float(input("\nEnter amount: "))
                if amount < 0:
                    print("Amount must be positive!")
                    continue
                break
            except ValueError:
                print("Invalid amount. Please enter a number.")
        
        # Get from currency
        from_curr = input("From currency (e.g., USD): ").upper().strip()
        if not from_curr:
            print("Currency code cannot be empty.")
            return
        
        # Get to currency
        to_curr = input("To currency (e.g., EUR): ").upper().strip()
        if not to_curr:
            print("Currency code cannot be empty.")
            return
        
        # Perform conversion
        print(f"\nConverting {amount} {from_curr} to {to_curr}...")
        result = convert_currency(amount, from_curr, to_curr)
        
        if result is not None:
            print(f"\n{amount:.2f} {from_curr} = {result:.2f} {to_curr}")
            print(f"\nExchange rate: 1 {from_curr} = {result/amount:.4f} {to_curr}")
    
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
        sys.exit(0)

if __name__ == "__main__":
    main()
