#!/usr/bin/env python3
"""
Crypto Ticker Terminal - A simple CLI tool to fetch cryptocurrency prices
Author: Comet Assistant
Issue: #653
"""

import requests
import sys
import json
from typing import Dict, Optional

# ANSI color codes
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def get_crypto_price(crypto_id: str, currency: str = 'usd') -> Optional[Dict]:
    """Fetch cryptocurrency price from CoinGecko API."""
    base_url = 'https://api.coingecko.com/api/v3/simple/price'
    params = {
        'ids': crypto_id,
        'vs_currencies': currency,
        'include_24hr_change': 'true',
        'include_market_cap': 'true',
        'include_24hr_vol': 'true'
    }
    
    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get(crypto_id)
    except requests.exceptions.RequestException as e:
        print(f"{Colors.RED}Error fetching data: {e}{Colors.RESET}")
        return None

def format_price(value: float) -> str:
    """Format price with proper decimal places."""
    if value >= 1:
        return f"${value:,.2f}"
    return f"${value:.6f}"

def format_change(change: float) -> str:
    """Format 24h change with color coding."""
    color = Colors.GREEN if change >= 0 else Colors.RED
    symbol = '▲' if change >= 0 else '▼'
    return f"{color}{symbol} {abs(change):.2f}%{Colors.RESET}"

def display_crypto_info(crypto_name: str, data: Dict, currency: str):
    """Display cryptocurrency information with colors."""
    price = data.get(currency, 0)
    change_24h = data.get(f'{currency}_24h_change', 0)
    market_cap = data.get(f'{currency}_market_cap', 0)
    volume_24h = data.get(f'{currency}_24h_vol', 0)
    
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*50}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.MAGENTA}{crypto_name.upper()} Price Information{Colors.RESET}")
    print(f"{Colors.CYAN}{'='*50}{Colors.RESET}\n")
    print(f"{Colors.BOLD}Price:{Colors.RESET} {Colors.YELLOW}{format_price(price)}{Colors.RESET}")
    print(f"{Colors.BOLD}24h Change:{Colors.RESET} {format_change(change_24h)}")
    print(f"{Colors.BOLD}Market Cap:{Colors.RESET} ${market_cap:,.0f}")
    print(f"{Colors.BOLD}24h Volume:{Colors.RESET} ${volume_24h:,.0f}")
    print(f"\n{Colors.CYAN}{'='*50}{Colors.RESET}\n")

def main():
    """Main function to run the crypto ticker."""
    # Popular cryptocurrencies mapping
    crypto_map = {
        'btc': 'bitcoin', 'bitcoin': 'bitcoin',
        'eth': 'ethereum', 'ethereum': 'ethereum',
        'ada': 'cardano', 'cardano': 'cardano',
        'sol': 'solana', 'solana': 'solana',
        'xrp': 'ripple', 'ripple': 'ripple',
        'doge': 'dogecoin', 'dogecoin': 'dogecoin',
        'dot': 'polkadot', 'polkadot': 'polkadot',
        'matic': 'matic-network', 'polygon': 'matic-network'
    }
    
    if len(sys.argv) < 2:
        print(f"{Colors.YELLOW}Usage: python crypto_ticker_terminal.py <crypto> [currency]{Colors.RESET}")
        print(f"\nSupported cryptos: {', '.join(set(crypto_map.values()))}")
        print(f"Example: python crypto_ticker_terminal.py btc")
        sys.exit(1)
    
    crypto_input = sys.argv[1].lower()
    currency = sys.argv[2].lower() if len(sys.argv) > 2 else 'usd'
    crypto_id = crypto_map.get(crypto_input, crypto_input)
    data = get_crypto_price(crypto_id, currency)
    
    if data:
        display_crypto_info(crypto_input, data, currency)
    else:
        print(f"{Colors.RED}Failed to fetch data for {crypto_input}{Colors.RESET}")
        sys.exit(1)

if __name__ == '__main__':
    main()
