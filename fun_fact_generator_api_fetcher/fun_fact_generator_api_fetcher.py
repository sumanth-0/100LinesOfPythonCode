#!/usr/bin/env python3
"""
Fun Fact Generator API Fetcher
Fetches and displays random fun facts from various public APIs
"""

import argparse
import requests
import json
import sys
from typing import Dict, Optional


class FunFactFetcher:
    """Fetches fun facts from multiple APIs"""
    
    def __init__(self):
        self.apis = {
            'uselessfacts': 'https://uselessfacts.jsph.pl/random.json?language=en',
            'catfacts': 'https://catfact.ninja/fact',
            'numbers': 'http://numbersapi.com/random/trivia',
            'chucknorris': 'https://api.chucknorris.io/jokes/random',
            'advice': 'https://api.adviceslip.com/advice'
        }
    
    def fetch_useless_fact(self) -> Optional[str]:
        """Fetch from useless facts API"""
        try:
            response = requests.get(self.apis['uselessfacts'], timeout=5)
            if response.status_code == 200:
                return response.json()['text']
        except Exception as e:
            print(f"Error fetching useless fact: {e}", file=sys.stderr)
        return None
    
    def fetch_cat_fact(self) -> Optional[str]:
        """Fetch from cat facts API"""
        try:
            response = requests.get(self.apis['catfacts'], timeout=5)
            if response.status_code == 200:
                return response.json()['fact']
        except Exception as e:
            print(f"Error fetching cat fact: {e}", file=sys.stderr)
        return None
    
    def fetch_number_fact(self) -> Optional[str]:
        """Fetch from numbers API"""
        try:
            response = requests.get(self.apis['numbers'], timeout=5)
            if response.status_code == 200:
                return response.text
        except Exception as e:
            print(f"Error fetching number fact: {e}", file=sys.stderr)
        return None
    
    def fetch_chuck_norris(self) -> Optional[str]:
        """Fetch from Chuck Norris API"""
        try:
            response = requests.get(self.apis['chucknorris'], timeout=5)
            if response.status_code == 200:
                return response.json()['value']
        except Exception as e:
            print(f"Error fetching Chuck Norris joke: {e}", file=sys.stderr)
        return None
    
    def fetch_advice(self) -> Optional[str]:
        """Fetch from advice slip API"""
        try:
            response = requests.get(self.apis['advice'], timeout=5)
            if response.status_code == 200:
                return response.json()['slip']['advice']
        except Exception as e:
            print(f"Error fetching advice: {e}", file=sys.stderr)
        return None
    
    def get_fact(self, source: str = 'uselessfacts') -> Optional[str]:
        """Get a fact from the specified source"""
        fetchers = {
            'uselessfacts': self.fetch_useless_fact,
            'catfacts': self.fetch_cat_fact,
            'numbers': self.fetch_number_fact,
            'chucknorris': self.fetch_chuck_norris,
            'advice': self.fetch_advice
        }
        return fetchers.get(source, self.fetch_useless_fact)()


def main():
    parser = argparse.ArgumentParser(description='Fetch random fun facts from various APIs')
    parser.add_argument('-s', '--source', choices=['uselessfacts', 'catfacts', 'numbers', 'chucknorris', 'advice'],
                        default='uselessfacts', help='Choose fact source (default: uselessfacts)')
    parser.add_argument('-l', '--list', action='store_true', help='List all available sources')
    args = parser.parse_args()
    
    fetcher = FunFactFetcher()
    
    if args.list:
        print("Available fact sources:")
        for source in fetcher.apis.keys():
            print(f"  - {source}")
        return
    
    fact = fetcher.get_fact(args.source)
    if fact:
        print(f"\n🎉 Fun Fact from {args.source}:")
        print(f"\n{fact}\n")
    else:
        print("Failed to fetch a fun fact. Please try again.", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
