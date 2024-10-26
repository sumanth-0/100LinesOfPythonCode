import requests

def get_exchange_rate(from_currency, to_currency):
    api_key = "your_exchange_api_key"  # Replace with your API key
    url = f"https://open.er-api.com/v6/latest/{from_currency}?apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200 and "rates" in data:
        return data["rates"].get(to_currency)
    else:
        print("Error fetching exchange rate.")
        return None

def convert_currency(amount, from_currency, to_currency):
    rate = get_exchange_rate(from_currency, to_currency)
    if rate:
        converted_amount = amount * rate
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}.")
    else:
        print("Conversion failed.")

def main():
    from_currency = input("Enter the currency to convert from (e.g., USD): ").upper()
    to_currency = input("Enter the currency to convert to (e.g., EUR): ").upper()
    amount = float(input("Enter the amount to convert: "))
    convert_currency(amount, from_currency, to_currency)

if __name__ == "__main__":
    main()
