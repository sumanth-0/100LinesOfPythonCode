import requests
import datetime
class CurrencyConverter:
    def __init__(self):
        self.api_key = 'YOUR_API_KEY'  # Replace with your API key
        self.base_url = "https://api.exchangerate-api.com/v4/latest/"
        self.history_url = "https://api.exchangerate-api.com/v4/history/"
    
    def get_latest_rates(self, base_currency):
        response = requests.get(self.base_url + base_currency)
        return response.json()

    def convert_currency(self, amount, from_currency, to_currency):
        latest_rates = self.get_latest_rates(from_currency)
        rate = latest_rates['rates'].get(to_currency)
        if rate:
            return amount * rate
        return None

    def get_historical_rates(self, base_currency, target_currency, start_date, end_date):
        response = requests.get(f"{self.history_url}{base_currency}?start_at={start_date}&end_at={end_date}")
        return response.json()

def main():
    converter = CurrencyConverter()
    
    base_currency = input("Enter base currency (e.g., USD): ").upper()
    amount = float(input("Enter amount to convert: "))
    target_currency = input("Enter target currency (e.g., EUR): ").upper()

    converted_amount = converter.convert_currency(amount, base_currency, target_currency)
    if converted_amount:
        print(f"{amount} {base_currency} is {converted_amount:.2f} {target_currency}")

    # Historical rates
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    historical_data = converter.get_historical_rates(base_currency, target_currency, start_date, end_date)
    print("Historical Rates:", historical_data)

if __name__ == "__main__":
    main()
