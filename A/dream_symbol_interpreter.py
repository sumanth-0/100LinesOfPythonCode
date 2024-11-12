import random

# Dictionary of classic dream symbols and their meanings
dream_symbols = {
    "falling": "A sign of insecurity, loss of control, or fear of failure.",
    "water": "Represents emotions, the unconscious mind, or cleansing.",
    "flying": "A feeling of freedom, achievement, or escaping reality.",
    "teeth falling out": "Associated with anxiety, self-esteem, or fear of aging.",
    "chasing": "Can symbolize avoidance or a need to confront something.",
    "death": "Often signifies transformation or a new beginning rather than literal death.",
    "house": "Represents the self or different aspects of one's life.",
    "snake": "A symbol of hidden fears, transformation, or healing.",
}

# Function to interpret a dream symbol
def interpret_symbol(symbol):
    meaning = dream_symbols.get(symbol.lower())
    if meaning:
        return f"Interpretation for '{symbol}': {meaning}"
    else:
        return f"Sorry, no interpretation available for '{symbol}'. Try another symbol!"

# Additional advice for recurring themes
def recurring_theme_advice():
    advice = [
        "Recurring dreams often point to unresolved issues or concerns in your waking life.",
        "Consider keeping a dream journal to identify patterns over time.",
        "Sometimes recurring themes reflect habits or emotions you're currently experiencing.",
    ]
    return random.choice(advice)

# User interaction simulation
if __name__ == "__main__":
    print("Welcome to the Dream Symbol Interpreter!")
    symbol = input("Enter a dream symbol you'd like to interpret: ")
    print(interpret_symbol(symbol))

    if input("Is this a recurring theme in your dreams? (yes/no): ").lower() == "yes":
        print("Advice on recurring themes:")
        print(recurring_theme_advice())
