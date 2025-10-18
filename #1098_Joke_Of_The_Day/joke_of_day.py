#!/usr/bin/env python3
"""
Joke of the Day CLI - Enhanced Version
Fetches and displays jokes from multiple public APIs with various features.
Supports multiple joke categories, favorites, and joke history.

Author: anieoni0
Issue: #1098
"""

import requests
import json
import sys
import argparse
from datetime import datetime
import random
import os

class JokeOfTheDay:
    """Main class for managing joke fetching and display."""
    
    def __init__(self):
        """Initialize the joke fetcher with API endpoints."""
        self.apis = {
            'official': 'https://official-joke-api.appspot.com/random_joke',
            'programming': 'https://official-joke-api.appspot.com/jokes/programming/random',
            'general': 'https://official-joke-api.appspot.com/jokes/general/random'
        }
        self.history_file = os.path.expanduser('~/.joke_history.json')
        self.favorites_file = os.path.expanduser('~/.joke_favorites.json')
    
    def get_joke(self, category='official'):
        """Fetch a random joke from the specified API category."""
        api_url = self.apis.get(category, self.apis['official'])
        
        try:
            response = requests.get(api_url, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            # Handle list response (some APIs return arrays)
            if isinstance(data, list) and len(data) > 0:
                data = data[0]
            
            return data
        except requests.exceptions.RequestException as e:
            print(f"Error fetching joke: {e}", file=sys.stderr)
            return None
        except json.JSONDecodeError:
            print("Error: Could not decode JSON response.", file=sys.stderr)
            return None
    
    def display_joke(self, joke_data, interactive=True):
        """Display a joke with formatting."""
        if not joke_data:
            print("No joke data available.")
            return False
        
        setup = joke_data.get('setup', 'No setup available')
        punchline = joke_data.get('punchline', 'No punchline available')
        joke_type = joke_data.get('type', 'general')
        
        print("\n" + "="*50)
        print("🎭 JOKE OF THE DAY 🎭".center(50))
        print("="*50)
        print(f"\nCategory: {joke_type.upper()}")
        print(f"\n📝 SETUP:\n{setup}")
        
        if interactive:
            input("\n⏎ Press Enter for the punchline...")
        
        print(f"\n😄 PUNCHLINE:\n{punchline}")
        print("\n" + "="*50 + "\n")
        
        # Save to history
        self.save_to_history(joke_data)
        return True
    
    def save_to_history(self, joke_data):
        """Save joke to history file."""
        try:
            history = self.load_json_file(self.history_file)
            joke_entry = {
                'setup': joke_data.get('setup'),
                'punchline': joke_data.get('punchline'),
                'timestamp': datetime.now().isoformat(),
                'type': joke_data.get('type', 'general')
            }
            history.append(joke_entry)
            # Keep only last 10 jokes
            history = history[-10:]
            self.save_json_file(self.history_file, history)
        except Exception as e:
            print(f"Warning: Could not save to history: {e}", file=sys.stderr)
    
    def load_json_file(self, filename):
        """Load data from JSON file."""
        if os.path.exists(filename):
            try:
                with open(filename, 'r') as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def save_json_file(self, filename, data):
        """Save data to JSON file."""
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

def main():
    """Main function to run the Joke CLI."""
    parser = argparse.ArgumentParser(description='Joke of the Day CLI')
    parser.add_argument('-c', '--category', 
                       choices=['official', 'programming', 'general'],
                       default='official',
                       help='Category of jokes to fetch')
    parser.add_argument('-n', '--no-interactive',
                       action='store_true',
                       help='Display joke without interactive pause')
    
    args = parser.parse_args()
    
    joke_fetcher = JokeOfTheDay()
    joke_data = joke_fetcher.get_joke(args.category)
    
    if joke_data:
        joke_fetcher.display_joke(joke_data, interactive=not args.no_interactive)
    else:
        print("Failed to fetch joke. Please try again later.")
        sys.exit(1)

if __name__ == "__main__":
    main()
