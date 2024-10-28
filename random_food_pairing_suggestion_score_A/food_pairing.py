import random

class FoodPairingSuggestion:
    def __init__(self):
        self.pairings = [
            ("Peanut Butter", "Jelly"),
            ("Wine", "Cheese"),
            ("Bacon", "Chocolate"),
            ("Strawberries", "Balsamic Vinegar"),
            ("Apples", "Peanut Butter"),
            ("Chili", "Cornbread"),
            ("Popcorn", "Chocolate"),
            ("Pizza", "Pineapple"),
            ("French Fries", "Ice Cream"),
            ("Mango", "Sticky Rice"),
        ]

    def get_random_pairing(self):
        """Get a random food pairing suggestion."""
        return random.choice(self.pairings)

def main():
    """Main function to suggest food pairings."""
    food_pairing = FoodPairingSuggestion()
    suggestion = food_pairing.get_random_pairing()
    print(f"Suggested Food Pairing: {suggestion[0]} and {suggestion[1]}")

if __name__ == "__main__":
    main()
