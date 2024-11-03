# tarot_reader.py

import random

def tarot_reading():
    """Simulates a simple tarot card reading."""

    suits = ["Wands", "Cups", "Swords", "Pentacles"]
    cards = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Page", "Knight", "Queen", "King"]

    # Draw three cards
    card1 = random.choice(suits) + " of " + random.choice(cards)
    card2 = random.choice(suits) + " of " + random.choice(cards)
    card3 = random.choice(suits) + " of " + random.choice(cards)

    print("Your three cards are:")
    print(f"1. {card1}")
    print(f"2. {card2}")
    print(f"3. {card3}")

    # Basic interpretations (you can customize these)
    print("\nInterpretation:")
    # ... (Add your specific interpretations here)

if __name__ == "__main__":
    tarot_reading()
