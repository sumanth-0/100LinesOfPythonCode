import time
from datetime import datetime
import random

class QuoteReflectionApp:
    def __init__(self):
        self.quotes = [
            "The only limit to our realization of tomorrow is our doubts of today.",
            "Life isn’t about finding yourself. Life is about creating yourself.",
            "Success is not final, failure is not fatal: it is the courage to continue that counts.",
            "Happiness is not by chance, but by choice.",
            "Dream big and dare to fail."
        ]
        self.reflections = []

    def get_quote_of_the_day(self):
        return random.choice(self.quotes)

    def add_reflection(self, quote, reflection):
        self.reflections.append({
            "date": datetime.now().strftime("%Y-%m-%d"),
            "quote": quote,
            "reflection": reflection
        })

    def view_past_reflections(self):
        print("\n--- Past Reflections ---")
        for entry in self.reflections:
            print(f"Date: {entry['date']}")
            print(f"Quote: {entry['quote']}")
            print(f"Reflection: {entry['reflection']}\n")

    def start(self):
        print("Welcome to Quote of the Day with Personal Reflection!")
        daily_quote = self.get_quote_of_the_day()
        print(f"\nToday's Quote:\n\"{daily_quote}\"")
        
        reflection = input("\nReflect on this quote (type your response): ").strip()
        self.add_reflection(daily_quote, reflection)
        
        view_log = input("\nWould you like to see your past reflections? (yes/no): ").strip().lower()
        if view_log == "yes":
            self.view_past_reflections()

if __name__ == "__main__":
    app = QuoteReflectionApp()
    app.start()
