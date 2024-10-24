import requests
import time

def fetch_crypto_data(crypto_id):
    """Fetch cryptocurrency data from CoinGecko API."""
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies=usd&include_24hr_change=true'
    response = requests.get(url)
    return response.json()

def display_prices(data):
    """Display cryptocurrency prices and price changes."""
    for crypto, info in data.items():
        price = info['usd']
        change = info['usd_24h_change']
        change_color = "\033[92m" if change >= 0 else "\033[91m"  # Green for positive, Red for negative
        reset_color = "\033[0m"
        print(f"{crypto.capitalize()}: ${price:.2f} | 24h Change: {change_color}{change:.2f}%{reset_color}")

def main():
    cryptos = ['bitcoin', 'ethereum']  # List of cryptocurrencies to track
    while True:
        try:
            data = fetch_crypto_data(','.join(cryptos))
            display_prices(data)
            print("\nFetching data again in 60 seconds...\n")
            time.sleep(60)  # Wait for 60 seconds before fetching data again
        except Exception as e:
            print(f"An error occurred: {e}")
            break

if __name__ == "__main__":
    main()
