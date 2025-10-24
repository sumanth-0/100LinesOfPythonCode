"""
Daily Random Joke Fetcher
Fetches a random joke daily from an API and displays it with caching.
"""

import requests
import json
import os
from datetime import datetime, date


class DailyJokeFetcher:
    """Fetches and caches daily jokes from various joke APIs."""
    
    def __init__(self):
        """Initialize the joke fetcher with API endpoints."""
        self.cache_file = "daily_joke_cache.json"
        self.apis = [
            {
                'name': 'JokeAPI',
                'url': 'https://v2.jokeapi.dev/joke/Any?safe-mode',
                'parser': self.parse_jokeapi
            },
            {
                'name': 'Official Joke API',
                'url': 'https://official-joke-api.appspot.com/random_joke',
                'parser': self.parse_official_joke
            },
            {
                'name': 'icanhazdadjoke',
                'url': 'https://icanhazdadjoke.com/',
                'parser': self.parse_icanhazdad,
                'headers': {'Accept': 'application/json'}
            }
        ]
        self.current_api_index = 0
    
    def parse_jokeapi(self, data):
        """Parse JokeAPI response."""
        if data.get('type') == 'twopart':
            return f"{data['setup']}\n\n{data['delivery']}"
        else:
            return data.get('joke', 'No joke available')
    
    def parse_official_joke(self, data):
        """Parse Official Joke API response."""
        setup = data.get('setup', '')
        punchline = data.get('punchline', '')
        return f"{setup}\n\n{punchline}"
    
    def parse_icanhazdad(self, data):
        """Parse icanhazdadjoke API response."""
        return data.get('joke', 'No joke available')
    
    def load_cache(self):
        """Load cached joke data."""
        if os.path.exists(self.cache_file):
            try:
                with open(self.cache_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception:
                return {}
        return {}
    
    def save_cache(self, cache_data):
        """Save joke data to cache."""
        try:
            with open(self.cache_file, 'w', encoding='utf-8') as f:
                json.dump(cache_data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Warning: Could not save cache: {e}")
    
    def get_today_date_str(self):
        """Get today's date as a string."""
        return date.today().isoformat()
    
    def fetch_joke_from_api(self, api_config):
        """Fetch a joke from a specific API."""
        try:
            headers = api_config.get('headers', {})
            response = requests.get(api_config['url'], headers=headers, timeout=10)
            response.raise_for_status()
            data = response.json()
            joke = api_config['parser'](data)
            return joke, api_config['name']
        except Exception as e:
            print(f"Error fetching from {api_config['name']}: {e}")
            return None, None
    
    def get_daily_joke(self, force_new=False):
        """
        Get the daily joke. Uses cache if available for today.
        
        Args:
            force_new: Force fetching a new joke even if cached
            
        Returns:
            tuple: (joke_text, source_api, is_cached)
        """
        today = self.get_today_date_str()
        cache = self.load_cache()
        
        # Check if we have a cached joke for today
        if not force_new and today in cache:
            return cache[today]['joke'], cache[today]['source'], True
        
        # Try to fetch from APIs
        for attempt in range(len(self.apis)):
            api_config = self.apis[self.current_api_index]
            joke, source = self.fetch_joke_from_api(api_config)
            
            if joke:
                # Cache the joke
                cache[today] = {
                    'joke': joke,
                    'source': source,
                    'timestamp': datetime.now().isoformat()
                }
                self.save_cache(cache)
                
                # Rotate to next API for variety
                self.current_api_index = (self.current_api_index + 1) % len(self.apis)
                
                return joke, source, False
            
            # Try next API
            self.current_api_index = (self.current_api_index + 1) % len(self.apis)
        
        return "Couldn't fetch a joke today. Try again later! 😊", "Error", False
    
    def display_joke(self, joke, source, is_cached):
        """Display the joke with nice formatting."""
        current_time = datetime.now().strftime("%I:%M %p")
        current_date = datetime.now().strftime("%B %d, %Y")
        
        print("\n" + "=" * 70)
        print("😂 DAILY JOKE OF THE DAY 😂")
        print("=" * 70)
        print(f"📅 Date: {current_date}")
        print(f"⏰ Time: {current_time}")
        print(f"🔗 Source: {source}")
        if is_cached:
            print("💾 [Cached - Today's joke]")
        print("=" * 70)
        print()
        print(joke)
        print()
        print("=" * 70)
        print()
    
    def show_joke_history(self):
        """Show recent joke history."""
        cache = self.load_cache()
        
        if not cache:
            print("\n📝 No joke history available yet!\n")
            return
        
        print("\n" + "=" * 70)
        print("📚 JOKE HISTORY")
        print("=" * 70 + "\n")
        
        # Sort by date (newest first)
        sorted_dates = sorted(cache.keys(), reverse=True)
        
        for i, date_str in enumerate(sorted_dates[:7], 1):  # Show last 7 days
            joke_data = cache[date_str]
            print(f"{i}. {date_str} - Source: {joke_data['source']}")
            print(f"   {joke_data['joke'][:100]}...")
            print()
        
        print("=" * 70 + "\n")


def main():
    """Main function to run the daily joke fetcher."""
    fetcher = DailyJokeFetcher()
    
    print("\n" + "=" * 70)
    print("🎭 DAILY RANDOM JOKE FETCHER 🎭")
    print("=" * 70)
    print("\nOptions:")
    print("1. Get today's joke")
    print("2. Get a new random joke")
    print("3. View joke history")
    print("4. Exit")
    print()
    
    while True:
        try:
            choice = input("Enter your choice (1-4): ").strip()
            
            if choice == "1":
                print("\n🔍 Fetching today's joke...\n")
                joke, source, is_cached = fetcher.get_daily_joke()
                fetcher.display_joke(joke, source, is_cached)
                
            elif choice == "2":
                print("\n🔍 Fetching a new random joke...\n")
                joke, source, is_cached = fetcher.get_daily_joke(force_new=True)
                fetcher.display_joke(joke, source, is_cached)
                
            elif choice == "3":
                fetcher.show_joke_history()
                
            elif choice == "4":
                print("\n👋 Thanks for the laughs! Have a great day!\n")
                break
                
            else:
                print("\n❌ Invalid choice. Please enter 1-4.\n")
                
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!\n")
            break
        except Exception as e:
            print(f"\n❌ An error occurred: {e}\n")


if __name__ == "__main__":
    main()
