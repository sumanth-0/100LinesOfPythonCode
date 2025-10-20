#!/usr/bin/env python3
"""
Crypto Price Notifier CLI

A command-line tool to monitor cryptocurrency prices and send notifications
when price thresholds are reached. Uses the CoinGecko API (free, no API key required).

Author: Comet Assistant
Issue: #1036
"""

import requests
import time
import json
import os
import sys
from datetime import datetime
import argparse


class CryptoPriceNotifier:
    """Monitor cryptocurrency prices and send notifications."""
    
    def __init__(self, crypto_id='bitcoin', target_price=None, condition='above'):
        """
        Initialize the notifier.
        
        Args:
            crypto_id: CoinGecko cryptocurrency ID (default: bitcoin)
            target_price: Price threshold for notification
            condition: 'above' or 'below' (default: above)
        """
        self.crypto_id = crypto_id
        self.target_price = target_price
        self.condition = condition
        self.base_url = 'https://api.coingecko.com/api/v3'
        self.currency = 'usd'
        self.history_file = 'crypto_price_history.json'
        
    def get_current_price(self):
        """Fetch current cryptocurrency price from CoinGecko API."""
        try:
            url = f"{self.base_url}/simple/price"
            params = {
                'ids': self.crypto_id,
                'vs_currencies': self.currency,
                'include_24hr_change': 'true',
                'include_market_cap': 'true'
            }
            
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            if self.crypto_id not in data:
                print(f"Error: '{self.crypto_id}' not found. Check the crypto ID.")
                return None
                
            price = data[self.crypto_id].get(self.currency)
            change_24h = data[self.crypto_id].get(f'{self.currency}_24h_change', 0)
            market_cap = data[self.crypto_id].get(f'{self.currency}_market_cap', 0)
            
            return {
                'price': price,
                'change_24h': change_24h,
                'market_cap': market_cap,
                'timestamp': datetime.now().isoformat()
            }
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching price: {e}")
            return None
            
    def display_price_info(self, price_data):
        """Display formatted price information."""
        if not price_data:
            return
            
        price = price_data['price']
        change = price_data['change_24h']
        market_cap = price_data['market_cap']
        timestamp = price_data['timestamp']
        
        # Format output with colors (if terminal supports it)
        change_symbol = '▲' if change >= 0 else '▼'
        change_color = '\033[92m' if change >= 0 else '\033[91m'
        reset_color = '\033[0m'
        
        print("\n" + "="*60)
        print(f"Cryptocurrency: {self.crypto_id.upper()}")
        print(f"Current Price: ${price:,.2f} {self.currency.upper()}")
        print(f"24h Change: {change_color}{change_symbol} {change:.2f}%{reset_color}")
        print(f"Market Cap: ${market_cap:,.0f}")
        print(f"Last Updated: {datetime.fromisoformat(timestamp).strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*60 + "\n")
        
    def save_to_history(self, price_data):
        """Save price data to history file."""
        try:
            history = []
            if os.path.exists(self.history_file):
                with open(self.history_file, 'r') as f:
                    history = json.load(f)
                    
            history.append({
                'crypto': self.crypto_id,
                **price_data
            })
            
            # Keep only last 100 entries
            history = history[-100:]
            
            with open(self.history_file, 'w') as f:
                json.dump(history, f, indent=2)
                
        except Exception as e:
            print(f"Error saving history: {e}")
            
    def check_threshold(self, current_price):
        """Check if price has crossed the threshold."""
        if not self.target_price:
            return False
            
        if self.condition == 'above':
            return current_price >= self.target_price
        else:
            return current_price <= self.target_price
            
    def send_notification(self, price_data):
        """Send notification when threshold is reached."""
        price = price_data['price']
        message = f"\n{'*' * 60}\n"
        message += f"🔔 PRICE ALERT! 🔔\n"
        message += f"{self.crypto_id.upper()} is now ${price:,.2f}\n"
        message += f"Target: ${self.target_price:,.2f} ({self.condition})\n"
        message += f"{'*' * 60}\n"
        
        print(message)
        
        # You can extend this to send email, SMS, or desktop notifications
        # For now, we'll just print to console
        
    def monitor(self, interval=60, duration=None):
        """Monitor cryptocurrency price at regular intervals."""
        print(f"Starting monitor for {self.crypto_id.upper()}...")
        if self.target_price:
            print(f"Alert threshold: ${self.target_price:,.2f} ({self.condition})")
        print(f"Checking every {interval} seconds...\n")
        
        start_time = time.time()
        
        try:
            while True:
                price_data = self.get_current_price()
                
                if price_data:
                    self.display_price_info(price_data)
                    self.save_to_history(price_data)
                    
                    if self.check_threshold(price_data['price']):
                        self.send_notification(price_data)
                        break
                        
                # Check if duration limit reached
                if duration and (time.time() - start_time) >= duration:
                    print("Monitor duration reached. Exiting...")
                    break
                    
                time.sleep(interval)
                
        except KeyboardInterrupt:
            print("\nMonitoring stopped by user.")
            sys.exit(0)


def main():
    """Main function to parse arguments and run the notifier."""
    parser = argparse.ArgumentParser(
        description='Monitor cryptocurrency prices and get notified',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Monitor Bitcoin price (one-time check)
  python crypto_price_notifier.py --crypto bitcoin
  
  # Monitor Ethereum and alert when price goes above $3000
  python crypto_price_notifier.py --crypto ethereum --target 3000 --condition above
  
  # Monitor Dogecoin every 30 seconds
  python crypto_price_notifier.py --crypto dogecoin --interval 30
        """
    )
    
    parser.add_argument(
        '--crypto', '-c',
        default='bitcoin',
        help='Cryptocurrency ID (e.g., bitcoin, ethereum, dogecoin)'
    )
    
    parser.add_argument(
        '--target', '-t',
        type=float,
        help='Target price for notification'
    )
    
    parser.add_argument(
        '--condition',
        choices=['above', 'below'],
        default='above',
        help='Condition for notification (default: above)'
    )
    
    parser.add_argument(
        '--interval', '-i',
        type=int,
        default=60,
        help='Check interval in seconds (default: 60)'
    )
    
    parser.add_argument(
        '--duration', '-d',
        type=int,
        help='Total monitoring duration in seconds'
    )
    
    parser.add_argument(
        '--once',
        action='store_true',
        help='Check price once and exit'
    )
    
    args = parser.parse_args()
    
    # Create notifier instance
    notifier = CryptoPriceNotifier(
        crypto_id=args.crypto,
        target_price=args.target,
        condition=args.condition
    )
    
    # Run based on mode
    if args.once:
        price_data = notifier.get_current_price()
        if price_data:
            notifier.display_price_info(price_data)
    else:
        notifier.monitor(interval=args.interval, duration=args.duration)


if __name__ == '__main__':
    main()
