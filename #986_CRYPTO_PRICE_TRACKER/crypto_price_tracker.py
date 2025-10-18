import requests
import argparse
import sys

API_URL = "https://api.coingecko.com/api/v3/simple/price"

def get_crypto_price(coin: str, currency: str) -> bool:
    params = {
        'ids': coin.lower(),
        'vs_currencies': currency.lower()
    }

    try:
        response = requests.get(API_URL, params=params, timeout=10)
        data = response.json()

        if coin.lower() not in data:
            print(f"❌ Coin not found: {coin}")
            return False

        price = data[coin.lower()][currency.lower()]
        print(f"✅ {coin.upper()} Price in {currency.upper()}: {price:,.2f}")
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Fetch cryptocurrency prices.")
    
    # If no arguments provided, show interactive help
    if len(sys.argv) == 1:
        print("🔮 Crypto Price Checker")
        print("Usage examples:")
        print("  python crypto_price_tracker.py bitcoin")
        print("  python crypto_price_tracker.py ethereum --currency eur")
        print("\nOr provide arguments:")
    
    parser.add_argument("coin", nargs="?", help="Cryptocurrency name")
    parser.add_argument("--currency", default="usd", help="Fiat currency")
    
    args = parser.parse_args()
    
    # Interactive mode if no coin provided
    if not args.coin:
        args.coin = input("Enter cryptocurrency (e.g. bitcoin): ").strip()
        if not args.coin:
            print("❌ No cryptocurrency provided")
            return
    
    get_crypto_price(args.coin, args.currency)

if __name__ == "__main__":
    main()