#!/usr/bin/env python3
"""
Personalized Tarot Card Pull
Draws tarot cards based on user input for personalized readings
"""

import random
import hashlib
from datetime import datetime

# Major Arcana cards with meanings
MAJOR_ARCANA = {
    "The Fool": "New beginnings, innocence, spontaneity",
    "The Magician": "Manifestation, resourcefulness, power",
    "The High Priestess": "Intuition, sacred knowledge, divine feminine",
    "The Empress": "Femininity, beauty, nature, abundance",
    "The Emperor": "Authority, establishment, structure",
    "The Hierophant": "Spiritual wisdom, tradition, conformity",
    "The Lovers": "Love, harmony, relationships, choices",
    "The Chariot": "Control, willpower, victory",
    "Strength": "Inner strength, courage, compassion",
    "The Hermit": "Soul searching, introspection, solitude",
    "Wheel of Fortune": "Good luck, karma, life cycles",
    "Justice": "Justice, fairness, truth, cause and effect",
    "The Hanged Man": "Pause, surrender, letting go",
    "Death": "Endings, transformation, transition",
    "Temperance": "Balance, moderation, patience",
    "The Devil": "Shadow self, attachment, addiction",
    "The Tower": "Sudden change, upheaval, revelation",
    "The Star": "Hope, faith, purpose, renewal",
    "The Moon": "Illusion, fear, anxiety, subconscious",
    "The Sun": "Positivity, fun, warmth, success",
    "Judgement": "Reflection, reckoning, awakening",
    "The World": "Completion, accomplishment, travel"
}

def get_personalized_seed(name, birthdate, question):
    """Generate a personalized seed from user information"""
    combined = f"{name.lower()}{birthdate}{question.lower()}{datetime.now().date()}"
    return int(hashlib.md5(combined.encode()).hexdigest(), 16)

def draw_cards(num_cards, seed=None):
    """Draw specified number of tarot cards"""
    if seed:
        random.seed(seed)
    cards = list(MAJOR_ARCANA.items())
    return random.sample(cards, min(num_cards, len(cards)))

def display_reading(cards, question, name):
    """Display the tarot reading in a formatted way"""
    print("\n" + "="*60)
    print(f"   Personalized Tarot Reading for {name}")
    print("="*60)
    print(f"\nQuestion: {question}\n")
    
    positions = ["Past", "Present", "Future"] if len(cards) == 3 else [f"Card {i+1}" for i in range(len(cards))]
    
    for i, (card, meaning) in enumerate(cards):
        position = positions[i] if i < len(positions) else f"Card {i+1}"
        print(f"\n{position}: {card}")
        print(f"Meaning: {meaning}")
        print("-" * 60)

def main():
    print("Welcome to Personalized Tarot Card Pull!\n")
    
    name = input("Enter your name: ").strip()
    birthdate = input("Enter your birthdate (YYYY-MM-DD): ").strip()
    question = input("What question do you seek guidance on? ").strip()
    
    print("\nHow many cards would you like to draw?")
    print("1 - Single card (Quick insight)")
    print("3 - Three-card spread (Past, Present, Future)")
    print("5 - Five-card spread (Detailed reading)")
    
    try:
        num_cards = int(input("\nEnter number (1, 3, or 5): "))
        if num_cards not in [1, 3, 5]:
            num_cards = 3
    except ValueError:
        num_cards = 3
    
    seed = get_personalized_seed(name, birthdate, question)
    drawn_cards = draw_cards(num_cards, seed)
    display_reading(drawn_cards, question, name)
    
    print("\n" + "="*60)
    print("Thank you for using Personalized Tarot Card Pull!")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
