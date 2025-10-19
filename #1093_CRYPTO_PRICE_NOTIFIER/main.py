import requests
import time
import os
COINS_TO_TRACK = [
    "bitcoin",
    "ethereum",
    "solana"
]
VS_CURRENCY = "usd"
REFRESH_RATE = 30
def get_crypto_prices(coin_ids, vs_currency):
    """Fetches cryptocurrency prices from the CoinGecko API."""
    
    ids_string = ",".join(coin_ids)
    
    
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": ids_string,
        "vs_currencies": vs_currency
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raises an error for bad responses (4xx or 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def display_prices(prices, vs_currency):
    """Clears the terminal and displays the prices in a formatted way."""
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("--- Live Crypto Prices ---")
    print(f"Last updated: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    if not prices:
        print("Could not retrieve prices. Retrying...")
        return

    for coin_id, data in prices.items():
        price = data.get(vs_currency)
        if price is not None:
            print(f"{coin_id.capitalize():<15} ${price:,.2f}")
        else:
            print(f"{coin_id.capitalize():<15} Price not available")
            
    print(f"\nRefreshing in {REFRESH_RATE} seconds...")

if __name__ == "__main__":
    while True:
        price_data = get_crypto_prices(COINS_TO_TRACK, VS_CURRENCY)
        display_prices(price_data, VS_CURRENCY)
        time.sleep(REFRESH_RATE)