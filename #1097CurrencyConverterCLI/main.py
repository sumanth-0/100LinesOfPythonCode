import requests

API_BASE = "https://api.frankfurter.app"

def get_supported_currencies():
    """Fetch and return supported currencies."""
    response = requests.get(f"{API_BASE}/currencies")
    if response.status_code != 200:
        raise Exception(f"Failed to fetch currency list. HTTP {response.status_code}")
    return response.json()  # returns dict like {"USD":"US Dollar","EUR":"Euro"}

def convert_currency(amount, from_currency, to_currency):
    """Convert currency using Frankfurter API."""
    url = f"{API_BASE}/latest?amount={amount}&from={from_currency}&to={to_currency}"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to convert currency. HTTP {response.status_code}")
    
    data = response.json()
    rates = data.get("rates", {})
    if not rates:
        raise ValueError("Invalid currency code or no rate available.")
    
    return list(rates.values())[0]  # Only one target currency

def main():
    print("=== Currency Converter ===")

    try:
        symbols = get_supported_currencies()
    except Exception as e:
        print("Error fetching currency list:", e)
        return

    print("\nAvailable currencies:\n")
    for code, name in sorted(symbols.items()):
        print(f"{code} - {name}")

    print("\n------------------------------")
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount.")
        return

    from_currency = input("Convert from (currency code): ").upper()
    to_currency = input("Convert to (currency code): ").upper()

    if from_currency not in symbols or to_currency not in symbols:
        print("Invalid currency code.")
        return

    try:
        result = convert_currency(amount, from_currency, to_currency)
        print(f"\n{amount:.2f} {from_currency} = {result:.2f} {to_currency}\n")
    except Exception as e:
        print("Error during conversion:", e)

if __name__ == "__main__":
    main()
