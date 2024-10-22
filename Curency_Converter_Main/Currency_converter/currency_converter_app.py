# run    pip install --user currencyconverter 
# to access the package to get live conversion rates
from currency_converter import CurrencyConverter
c = CurrencyConverter()

def convert_currency(base_currency, target_currency, amount):
    try:
        converted_amount = c.convert(amount, base_currency, target_currency)
        return converted_amount
    except ValueError as e:
        print(f"Error: {e}")
        return None

def display_symbol(currency_code):
    currency_symbols = {
        'USD': '$',
        'EUR': '€',
        'INR': '₹',
        'GBP': '£',
        'JPY': '¥'
    }
    return currency_symbols.get(currency_code, currency_code)

def currency_converter():
    print("Currency Converter (using ECB historical data)")
    base_currency = input("Enter the base currency (e.g., USD, EUR): ").upper()
    target_currency = input("Enter the target currency (e.g., INR, GBP): ").upper()
    
    try:
        amount = float(input(f"Enter amount in {base_currency}: "))
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
        return
    converted_amount = convert_currency(base_currency, target_currency, amount)
    if converted_amount:
        base_symbol = display_symbol(base_currency)
        target_symbol = display_symbol(target_currency)
        print(f"\n{base_symbol}{amount:.2f} {base_currency} = {target_symbol}{converted_amount:.2f} {target_currency}")
    else:
        print("Conversion failed. Please try again.")

if __name__ == "__main__":
    currency_converter()
