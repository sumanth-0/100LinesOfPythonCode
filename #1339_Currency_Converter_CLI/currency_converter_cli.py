import requests

def convert_currency(amount, from_currency, to_currency):
    try:
        url = f"https://open.er-api.com/v6/latest/{from_currency.upper()}"
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        data = response.json()

        if response.status_code == 200 and "rates" in data:
            rate = data["rates"].get(to_currency.upper())
            if rate:
                converted = amount * rate
                print(f"{amount} {from_currency.upper()} = {converted:.2f} {to_currency.upper()}")
            else:
                print(f"Currency '{to_currency}' not found.")
        else:
            print("Error fetching conversion data. Try again later.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("🌍 Currency Converter CLI 🌍")
    amount = float(input("Enter amount: "))
    from_currency = input("From currency (e.g., USD): ").upper()
    to_currency = input("To currency (e.g., INR): ").upper()
    convert_currency(amount, from_currency, to_currency)
