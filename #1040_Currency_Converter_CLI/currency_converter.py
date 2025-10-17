#!/usr/bin/env python3
import json
import sys
import urllib.request
import urllib.error


API_URL = "https://api.frankfurter.app/latest"


def fetch_rate(from_currency, to_currency):
    """Fetch conversion rate between two currencies."""
    url = f"{API_URL}?from={from_currency}&to={to_currency}"
    try:
        with urllib.request.urlopen(url, timeout=5) as resp:
            data = json.load(resp)
        rate = data["rates"][to_currency]
        return rate
    except urllib.error.URLError as e:
        print(f"Error fetching rates: {e}", file=sys.stderr)
        sys.exit(1)
    except KeyError:
        print(f"Invalid currency code: {to_currency}", file=sys.stderr)
        sys.exit(1)


def convert(amount, from_currency, to_currency):
    """Convert amount using fetched rate."""
    rate = fetch_rate(from_currency, to_currency)
    return amount * rate


def main():
    if len(sys.argv) != 4:
        print("Usage: python currency_convert.py AMOUNT FROM TO")
        print("Example: python currency_convert.py 100 USD EUR")
        sys.exit(1)

    try:
        amount = float(sys.argv[1])
    except ValueError:
        print("Amount must be a number", file=sys.stderr)
        sys.exit(1)

    from_curr = sys.argv[2].upper()
    to_curr = sys.argv[3].upper()
    result = convert(amount, from_curr, to_curr)
    print(f"{amount:.2f} {from_curr} = {result:.2f} {to_curr}")


if __name__ == "__main__":
    main()