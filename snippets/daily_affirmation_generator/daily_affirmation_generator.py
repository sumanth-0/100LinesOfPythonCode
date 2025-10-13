#!/usr/bin/env python3
"""
Daily Affirmation Generator
Generates and displays random daily affirmations to boost positivity and motivation.

Usage:
    python daily_affirmation_generator.py
    python daily_affirmation_generator.py --count 5
"""
import random
import sys
from datetime import datetime

class DailyAffirmationGenerator:
    """Generates positive daily affirmations."""
    
    AFFIRMATIONS = [
        "I am worthy of love and respect.",
        "I am capable of achieving my goals.",
        "I choose to focus on what I can control.",
        "I am growing and learning every day.",
        "I trust in my ability to overcome challenges.",
        "I am grateful for all the good in my life.",
        "I radiate confidence and positive energy.",
        "I am deserving of success and happiness.",
        "I embrace change and welcome new opportunities.",
        "I am stronger than I think.",
        "I believe in myself and my abilities.",
        "I am making progress, one step at a time.",
        "I am surrounded by abundance and possibility.",
        "I choose positivity and optimism today.",
        "I am enough, just as I am.",
        "I release worry and embrace peace.",
        "I am creating the life I desire.",
        "I attract positive experiences and people.",
        "I am proud of how far I've come.",
        "I have the power to create positive change.",
        "I am resilient and adaptable.",
        "I trust the journey of my life.",
        "I am open to receiving joy and abundance.",
        "I choose to see the good in every situation.",
        "I am a magnet for success and prosperity.",
    ]
    
    def __init__(self, seed=None):
        """Initialize the generator with optional seed for reproducibility."""
        if seed:
            random.seed(seed)
    
    def get_affirmation(self):
        """Get a single random affirmation."""
        return random.choice(self.AFFIRMATIONS)
    
    def get_multiple_affirmations(self, count=3):
        """Get multiple unique affirmations."""
        count = min(count, len(self.AFFIRMATIONS))
        return random.sample(self.AFFIRMATIONS, count)
    
    def display_affirmation(self, affirmation):
        """Display a single affirmation in a formatted way."""
        print("\n" + "*" * 60)
        print(f"  {affirmation}")
        print("*" * 60 + "\n")
    
    def display_daily_affirmations(self, count=1):
        """Display daily affirmations with date header."""
        today = datetime.now().strftime("%A, %B %d, %Y")
        print("\n" + "=" * 60)
        print(f"  Daily Affirmations for {today}")
        print("=" * 60)
        
        if count == 1:
            affirmation = self.get_affirmation()
            self.display_affirmation(affirmation)
        else:
            affirmations = self.get_multiple_affirmations(count)
            for i, affirmation in enumerate(affirmations, 1):
                print(f"\n{i}. {affirmation}")
            print("\n" + "=" * 60 + "\n")

def main():
    """Main function to handle CLI usage."""
    count = 1
    
    # Parse command line arguments
    if len(sys.argv) > 1:
        if sys.argv[1] in ['-h', '--help']:
            print("Usage: python daily_affirmation_generator.py [--count N]")
            print("\nOptions:")
            print("  --count N  Display N affirmations (default: 1)")
            print("  -h, --help Show this help message")
            return
        elif sys.argv[1] == '--count' and len(sys.argv) > 2:
            try:
                count = int(sys.argv[2])
                if count < 1:
                    print("Error: Count must be at least 1")
                    sys.exit(1)
            except ValueError:
                print("Error: Count must be a number")
                sys.exit(1)
    
    generator = DailyAffirmationGenerator()
    generator.display_daily_affirmations(count)

if __name__ == "__main__":
    main()
