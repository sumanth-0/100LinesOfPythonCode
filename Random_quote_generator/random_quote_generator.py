"""
Random Quote Generator 🧠
-------------------------
This simple Python script displays a random motivational quote each time you run it.

Useful for learning:
- Working with random.choice
- Basic data structures (lists)
- Clean code organization and readability

Author: <your_name_here>
"""

import random

def get_random_quote():
    """Return a random motivational quote from a predefined list."""
    quotes = [
        "Believe you can and you're halfway there. – Theodore Roosevelt",
        "The only way to do great work is to love what you do. – Steve Jobs",
        "Don't watch the clock; do what it does. Keep going. – Sam Levenson",
        "It always seems impossible until it's done. – Nelson Mandela",
        "Dream big and dare to fail. – Norman Vaughan",
        "Start where you are. Use what you have. Do what you can. – Arthur Ashe",
        "Everything you can imagine is real. – Pablo Picasso",
        "Act as if what you do makes a difference. It does. – William James",
    ]
    return random.choice(quotes)

def main():
    """Main function to print a random quote."""
    print("✨ Random Quote Generator ✨")
    print("-" * 40)
    print(get_random_quote())
    print("-" * 40)

if __name__ == "__main__":
    main()
