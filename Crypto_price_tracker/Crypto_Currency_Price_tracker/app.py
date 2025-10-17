import requests
import time
import os
from datetime import datetime

# ANSI color codes for terminal
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

# Available cryptocurrencies
AVAILABLE_CRYPTOS = {
    '1': ('bitcoin', 'Bitcoin', 'BTC'),
    '2': ('ethereum', 'Ethereum', 'ETH'),
    '3': ('cardano', 'Cardano', 'ADA'),
    '4': ('ripple', 'Ripple', 'XRP'),
    '5': ('dogecoin', 'Dogecoin', 'DOGE'),
    '6': ('polkadot', 'Polkadot', 'DOT'),
    '7': ('solana', 'Solana', 'SOL'),
    '8': ('litecoin', 'Litecoin', 'LTC')
}

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_crypto_prices(crypto_ids):
    """Fetch cryptocurrency prices from CoinGecko API"""
    crypto_string = ','.join(crypto_ids)
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_string}&vs_currencies=usd&include_24hr_change=true"
    try:
        response = requests.get(url)
        return response.json()
    except Exception as e:
        print(f"{Colors.RED}Error fetching data: {e}{Colors.RESET}")
        return None

def display_prices(data, old_prices, crypto_info):
    """Display cryptocurrency prices in terminal"""
    clear_screen()
    print(f"{Colors.BOLD}{Colors.CYAN}{'='*60}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'LIVE CRYPTOCURRENCY PRICE TRACKER':^60}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'='*60}{Colors.RESET}\n")
    print(f"{Colors.WHITE}Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Colors.RESET}\n")
    
    for crypto_id, (name, symbol) in crypto_info.items():
        if crypto_id in data:
            price = data[crypto_id]['usd']
            change_24h = data[crypto_id].get('usd_24h_change', 0)
            
            # Calculate change since last update
            if crypto_id in old_prices:
                price_change = price - old_prices[crypto_id]
                change_color = Colors.GREEN if price_change >= 0 else Colors.RED
                change_symbol = "▲" if price_change >= 0 else "▼"
            else:
                price_change = 0
                change_color = Colors.WHITE
                change_symbol = "●"
            
            change_24h_color = Colors.GREEN if change_24h >= 0 else Colors.RED
            
            print(f"{Colors.BOLD}{Colors.YELLOW}{name} ({symbol}){Colors.RESET}")
            print(f"  Price: {Colors.BOLD}${price:,.2f}{Colors.RESET}")
            print(f"  24h Change: {change_24h_color}{change_24h:+.2f}%{Colors.RESET}")
            print(f"  Live Change: {change_color}{change_symbol} ${price_change:+.2f}{Colors.RESET}")
            print()

def select_cryptocurrencies():
    """Allow user to select cryptocurrencies to track"""
    clear_screen()
    print(f"{Colors.BOLD}{Colors.CYAN}Select Cryptocurrencies to Track{Colors.RESET}\n")
    
    for key, (_, name, symbol) in AVAILABLE_CRYPTOS.items():
        print(f"{key}. {name} ({symbol})")
    
    print(f"\n{Colors.YELLOW}Enter numbers separated by commas (e.g., 1,2,5) or 'all' for all:{Colors.RESET}")
    selection = input("> ").strip().lower()
    
    if selection == 'all':
        return {crypto_id: (name, symbol) for _, (crypto_id, name, symbol) in AVAILABLE_CRYPTOS.items()}
    
    selected = {}
    for num in selection.split(','):
        num = num.strip()
        if num in AVAILABLE_CRYPTOS:
            crypto_id, name, symbol = AVAILABLE_CRYPTOS[num]
            selected[crypto_id] = (name, symbol)
    
    return selected if selected else {AVAILABLE_CRYPTOS['1'][0]: (AVAILABLE_CRYPTOS['1'][1], AVAILABLE_CRYPTOS['1'][2])}

def main():
    """Main function to run the crypto price tracker"""
    crypto_info = select_cryptocurrencies()
    crypto_ids = list(crypto_info.keys())
    old_prices = {}
    
    print(f"\n{Colors.GREEN}Fetching prices every 10 seconds. Press Ctrl+C to exit.{Colors.RESET}")
    time.sleep(2)
    
    try:
        while True:
            data = get_crypto_prices(crypto_ids)
            if data:
                display_prices(data, old_prices, crypto_info)
                # Update old prices for next comparison
                for crypto_id in crypto_ids:
                    if crypto_id in data:
                        old_prices[crypto_id] = data[crypto_id]['usd']
            time.sleep(10)
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}Thank you for using Crypto Price Tracker!{Colors.RESET}")

if __name__ == "__main__":
    main()
