import random

# A list of random compliments
compliments = [
    "Your smile could light up the entire galaxy!",
    "You're not just smart; you're brilliantly unique.",
    "If kindness were a currency, you'd be a billionaire.",
    "Your energy is contagious in the best possible way.",
    "You're the kind of person who makes every room better.",
    "Your creativity knows no bounds—pure inspiration!",
    "You've got a heart of gold and a mind of diamonds.",
    "You're hilariously awesome and awesomely hilarious.",
    "Your determination is the stuff of legends.",
    "You're a walking, talking ray of sunshine.",
    "Your laugh is music to everyone's ears.",
    "You're talented in ways you don't even realize yet.",
    "Your empathy makes the world a warmer place.",
    "You're brave, bold, and beautifully yourself.",
    "Your ideas are as fresh as a summer breeze.",
    "You're the friend everyone wishes they had.",
    "Your passion is infectious and inspiring.",
    "You're a masterpiece in a world of sketches.",
    "Your wit is sharper than a tack—love it!",
    "You're destined for greatness, no doubt."
]

def generate_compliments(num_compliments=5):
    """Generate a list of random compliments."""
    if num_compliments > len(compliments):
        num_compliments = len(compliments)
    return random.sample(compliments, num_compliments)

def main():
    print("Random Compliments Generator")
    try:
        num = int(input("How many compliments? (default 5): ").strip() or "5")
    except ValueError:
        num = 5
    
    if num <= 0:
        print("No compliments? You're still amazing!")
        return
    
    compliments_list = generate_compliments(num)
    print(f"\nHere are {num} compliments just for you:\n")
    for i, comp in enumerate(compliments_list, 1):
        print(f"{i}. {comp}")
        print()

if __name__ == "__main__":
    main()
