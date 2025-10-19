#!/usr/bin/env python3
"""
URL Shortener CLI
A command-line interface for shortening URLs using both API-based and hash-based methods.
"""

import argparse
import hashlib
import json
import os
import sys
import requests
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

# Configuration
CONFIG_DIR = Path.home() / '.url_shortener'
HISTORY_FILE = CONFIG_DIR / 'history.json'
API_ENDPOINT = 'https://is.gd/create.php'

class URLShortener:
    """Main class for URL shortening operations."""
    
    def __init__(self):
        """Initialize the URL shortener."""
        self.ensure_config_dir()
        self.history = self.load_history()
    
    def ensure_config_dir(self):
        """Create configuration directory if it doesn't exist."""
        CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    
    def load_history(self):
        """Load URL shortening history from file."""
        if HISTORY_FILE.exists():
            try:
                with open(HISTORY_FILE, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return []
        return []
    
    def save_history(self):
        """Save URL shortening history to file."""
        try:
            with open(HISTORY_FILE, 'w') as f:
                json.dump(self.history, f, indent=2)
        except IOError as e:
            print(f"Warning: Could not save history: {e}", file=sys.stderr)
    
    def validate_url(self, url):
        """Validate if the given string is a valid URL."""
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except ValueError:
            return False
    
    def hash_based_shorten(self, url, length=8):
        """Generate a hash-based short code for the URL."""
        # Create a hash of the URL
        hash_object = hashlib.sha256(url.encode())
        hex_digest = hash_object.hexdigest()
        
        # Take first 'length' characters as short code
        short_code = hex_digest[:length]
        
        # Store the mapping
        entry = {
            'original_url': url,
            'short_code': short_code,
            'method': 'hash',
            'timestamp': datetime.now().isoformat(),
            'full_hash': hex_digest
        }
        
        # Check if URL already exists in history
        for item in self.history:
            if item.get('original_url') == url and item.get('method') == 'hash':
                return item['short_code']
        
        self.history.append(entry)
        self.save_history()
        
        return short_code
    
    def api_based_shorten(self, url, custom_code=None):
        """Shorten URL using is.gd API."""
        try:
            params = {
                'format': 'json',
                'url': url
            }
            
            if custom_code:
                params['shorturl'] = custom_code
            
            response = requests.get(API_ENDPOINT, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                
                if 'shorturl' in data:
                    entry = {
                        'original_url': url,
                        'short_url': data['shorturl'],
                        'method': 'api',
                        'timestamp': datetime.now().isoformat()
                    }
                    self.history.append(entry)
                    self.save_history()
                    return data['shorturl']
                elif 'errormessage' in data:
                    raise Exception(data['errormessage'])
            else:
                raise Exception(f"API request failed with status {response.status_code}")
        
        except requests.RequestException as e:
            raise Exception(f"Network error: {e}")
        except json.JSONDecodeError:
            raise Exception("Failed to parse API response")
    
    def expand_hash(self, short_code):
        """Expand a hash-based short code to original URL."""
        for entry in reversed(self.history):
            if entry.get('method') == 'hash' and entry.get('short_code') == short_code:
                return entry['original_url']
        return None
    
    def show_history(self, limit=10):
        """Display URL shortening history."""
        if not self.history:
            print("No history available.")
            return
        
        print(f"\nShowing last {min(limit, len(self.history))} entries:\n")
        print("{:<20} {:<50} {:<30}".format("Method", "Original URL", "Short URL/Code"))
        print("-" * 100)
        
        for entry in reversed(self.history[-limit:]):
            method = entry.get('method', 'unknown')
            original = entry.get('original_url', 'N/A')[:47] + '...'
            short = entry.get('short_url') or entry.get('short_code', 'N/A')
            print("{:<20} {:<50} {:<30}".format(method, original, short))

def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description='URL Shortener CLI - Shorten URLs using API or hash-based methods',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s -u https://example.com/very/long/url
  %(prog)s -u https://example.com -m hash
  %(prog)s -u https://example.com -c mylink
  %(prog)s -e abc12345
  %(prog)s --history
        """
    )
    
    parser.add_argument('-u', '--url', help='URL to shorten')
    parser.add_argument('-m', '--method', choices=['api', 'hash'], default='api',
                       help='Shortening method (default: api)')
    parser.add_argument('-c', '--custom', help='Custom short code (API method only)')
    parser.add_argument('-e', '--expand', help='Expand hash-based short code')
    parser.add_argument('-l', '--length', type=int, default=8,
                       help='Length of hash-based short code (default: 8)')
    parser.add_argument('--history', action='store_true',
                       help='Show URL shortening history')
    parser.add_argument('-n', '--number', type=int, default=10,
                       help='Number of history entries to show (default: 10)')
    
    args = parser.parse_args()
    
    shortener = URLShortener()
    
    # Show history
    if args.history:
        shortener.show_history(args.number)
        return
    
    # Expand short code
    if args.expand:
        original = shortener.expand_hash(args.expand)
        if original:
            print(f"Original URL: {original}")
        else:
            print(f"No URL found for short code: {args.expand}")
        return
    
    # Shorten URL
    if args.url:
        if not shortener.validate_url(args.url):
            print(f"Error: Invalid URL: {args.url}", file=sys.stderr)
            sys.exit(1)
        
        try:
            if args.method == 'hash':
                short_code = shortener.hash_based_shorten(args.url, args.length)
                print(f"\nOriginal URL: {args.url}")
                print(f"Short Code: {short_code}")
                print(f"\nNote: This is a hash-based code. Use --expand to retrieve the original URL.")
            else:
                short_url = shortener.api_based_shorten(args.url, args.custom)
                print(f"\nOriginal URL: {args.url}")
                print(f"Short URL: {short_url}")
        
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
