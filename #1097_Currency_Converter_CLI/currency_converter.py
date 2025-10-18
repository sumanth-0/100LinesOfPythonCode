#!/usr/bin/env python3
"""
Currency Converter CLI
Convert amounts between currencies using the Free Currency API.
"""

import requests
import sys
from datetime import datetime


class CurrencyConverter:
    """Currency converter using Free Currency API."""
    
    def __init__(self):
        self.api_url = "https://api.freecurrencyapi.com/v1/latest"
        self.api_key = "fca_live_YOUR_API_KEY_HERE"  # Free API key
        self.currencies = {}
        
    def get_exchange_rates(self, base_currency="USD"):
        """Fetch exchange rates from the API."""
        try:
            params = {
                "apikey": self.api_key,
                "base_currency": base_currency
            }
            response = requests.get(self.api_url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            return data.get("data", {})
        except requests.exceptions.RequestException as e:
            print(f"Error fetching exchange rates: {e}")
            return None
            
    def convert_currency(self, amount, from_currency, to_currency):
        """Convert amount from one currency to another."""
        # Get rates with from_currency as base
        rates = self.get_exchange_rates(from_currency)
        
        if not rates:
            return None
            
        if to_currency not in rates:
            print(f"Currency '{to_currency}' not found.")
            return None
            
        exchange_rate = rates[to_currency]
        converted_amount = amount * exchange_rate
        return converted_amount, exchange_rate
        
    def display_result(self, amount, from_currency, to_currency, converted_amount, rate):
        """Display conversion result."""
        print("\n" + "="*50)
        print("Currency Conversion Result")
        print("="*50)
        print(f"Amount: {amount:.2f} {from_currency}")
        print(f"Converted: {converted_amount:.2f} {to_currency}")
        print(f"Exchange Rate: 1 {from_currency} = {rate:.6f} {to_currency}")
        print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*50)
        
    def run(self):
        """Run the CLI interface."""
        print("\n" + "="*50)
        print("Currency Converter CLI")
        print("="*50)
        print("Convert amounts between different currencies.")
        print("Note: Using Free Currency API (limited features in demo)")
        print("="*50 + "\n")
        
        try:
            # Get amount
            amount_str = input("Enter amount to convert: ")
            amount = float(amount_str)
            
            if amount <= 0:
                print("Error: Amount must be positive.")
                return
                
            # Get source currency
            from_currency = input("From currency (e.g., USD): ").upper().strip()
            
            if len(from_currency) != 3:
                print("Error: Currency code must be 3 letters.")
                return
                
            # Get target currency
            to_currency = input("To currency (e.g., EUR): ").upper().strip()
            
            if len(to_currency) != 3:
                print("Error: Currency code must be 3 letters.")
                return
                
            print("\nFetching exchange rates...")
            result = self.convert_currency(amount, from_currency, to_currency)
            
            if result:
                converted_amount, rate = result
                self.display_result(amount, from_currency, to_currency, converted_amount, rate)
            else:
                print("Conversion failed. Please try again.")
                
        except ValueError:
            print("Error: Invalid amount. Please enter a number.")
        except KeyboardInterrupt:
            print("\n\nOperation cancelled by user.")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    converter = CurrencyConverter()
    converter.run()
