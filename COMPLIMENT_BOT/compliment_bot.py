"""
🪄 Compliment Bot
Each time you run it, it gives a friendly compliment chosen randomly.
Author: Diya Satish Kumar
"""

import random
import time
import textwrap

# 🌸 List of wholesome compliments
COMPLIMENTS = [
    "Someone’s smiling right now because of you 💖",
    "You make the world brighter just by being in it 🌞",
    "You’re doing amazing — don’t forget that! ✨",
    "You have a kind heart and a sharp mind 💡",
    "You bring out the best in others 🌷",
    "Your presence makes everything better 🌈",
    "You’re one of a kind — keep being you 🌟",
    "Someone out there is grateful for you today 💌",
    "You make even ordinary moments special 🌻",
    "The world needs more people like you 🌍",
]

def compliment_bot():
    print("\n🌸 Welcome to the Compliment Bot 🌸\n")
    time.sleep(0.5)

    compliment = random.choice(COMPLIMENTS)
    wrapped = textwrap.fill(compliment, width=60)
    
    for char in wrapped:
        print(char, end='', flush=True)
        time.sleep(0.02)  # Typing effect
    
    print("\n\n💬 Run me again for another compliment!\n")

if __name__ == "__main__":
    compliment_bot()
