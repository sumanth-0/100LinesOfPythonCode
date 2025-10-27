import os
import requests
from dotenv import load_dotenv
from datetime import datetime

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("EXCHANGE_API_KEY")
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}"

# 1️⃣ Get all conversion rates
def list_all_conversions(base_currency="USD"):
    url = f"{BASE_URL}/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()

    if data.get("result") == "success":
        print(f"\nExchange rates for {base_currency}:")
        for currency, rate in data["conversion_rates"].items():
            print(f"{currency}: {rate}")
    else:
        print("Error:", data.get("error-type", "Unknown error"))

# 2️⃣ Convert a currency pair (e.g., EUR → GBP)
def convert_pair(from_currency, to_currency, amount):
    url = f"{BASE_URL}/pair/{from_currency}/{to_currency}"
    response = requests.get(url)
    data = response.json()

    if data.get("result") == "success":
        print(f"\n{amount} {from_currency} = {amount*data['conversion_rate']} {to_currency}")

    else:
        print("Error:", data.get("error-type", "Unknown error"))

# 3️⃣ Get historical rates for a specific date
def get_historical(base_currency, year, month, day):
    url = f"{BASE_URL}/history/{base_currency}/{year}/{month:02d}/{day:02d}"
    response = requests.get(url)
    data = response.json()

    if data.get("result") == "success":
        print(f"\nHistorical exchange rates for {base_currency} on {year}-{month:02d}-{day:02d}:")
        for currency, rate in data["conversion_rates"].items():
            print(f"{currency}: {rate}")
    else:
        print("Error:", data.get("error-type", "Unknown error"))

# 🧭 Example usage
if __name__ == "__main__":
    print("=== Currency Converter using ExchangeRate API ===")
    print("1️⃣  List all exchange rates (default USD)")
    print("2️⃣  Convert a currency pair")
    print("3️⃣  Get historical exchange rates\n")

    choice = input("Enter your choice (1/2/3): ").strip()

    if choice == "1":
        base = input("Enter base currency (default USD): ").strip() or "USD"
        list_all_conversions(base)

    elif choice == "2":
        from_curr = input("From currency (e.g. USD): ").strip().upper()
        to_curr = input("To currency (e.g. INR): ").strip().upper()
        amount = float(input(f"Amount of {from_curr} to convert: "))
        convert_pair(from_curr, to_curr, amount)

    elif choice == "3":
        base = input("Enter base currency (e.g. USD): ").strip().upper()
        date_str = input("Enter date (YYYY-MM-DD): ").strip()
        year, month, day = map(int, date_str.split("-"))
        get_historical(base, year, month, day)

    else:
        print("Invalid choice!")
