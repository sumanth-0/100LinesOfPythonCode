import random

# Famous quote parts: beginnings, middles, ends
beginnings = [
    "To be or not to be, that is the question:",
    "I have a dream that one day",
    "Ask not what your country can do for you",
    "The only thing we have to fear is fear itself",
    "That's one small step for man, one giant leap",
    "I am not a crook",
    "Mr. Gorbachev, tear down this wall!",
    "Four score and seven years ago",
    "We shall fight on the beaches, we shall fight on the landing grounds",
    "It was the best of times, it was the worst of times"
]

middles = [
    "but instead, we should all just",
    "in a galaxy far, far away, where people",
    "while eating pizza and watching cat videos",
    "because who needs logic when you have",
    "if you believe in yourself and",
    "even though my cat disagrees",
    "with a side of sarcasm and",
    "after a long nap and some coffee",
    "unless it's Monday, then we're doomed",
    "surrounded by bad decisions and"
]

ends = [
    "dance like nobody's watching.",
    "live like you're in a sitcom.",
    "ask what you can do for your pizza.",
    "fear the dentist more than anything.",
    "for the remote control.",
    "but my browser history says otherwise.",
    "and build a blanket fort.",
    "ago, when dinosaurs roamed TikTok.",
    "fight for the last slice of cake.",
    "it was naptime."
]

def mash_quote():
    """Mix parts into a funny new quote."""
    begin = random.choice(beginnings)
    mid = random.choice(middles)
    end = random.choice(ends)
    return f"{begin} {mid} {end}"

def main():
    print("Funny Quote Masher")
    try:
        num = int(input("How many mashed quotes? (default 5): ").strip() or "5")
    except ValueError:
        num = 5
    
    print("\nMashed Quotes:\n")
    for i in range(num):
        quote = mash_quote()
        print(f"{i+1}. {quote}")
        print()

if __name__ == "__main__":
    main()
