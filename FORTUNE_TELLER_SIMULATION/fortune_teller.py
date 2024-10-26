import random

def get_fortune():
    fortunes = [
        "You will find great fortune in unexpected places.",
        "Beware of those who bring you cookies.",
        "The stars align in your favor; don't ignore them.",
        "A great opportunity will present itself; be ready!",
        "You will meet someone important today.",
        "Expect to hear good news in the near future.",
        "A journey awaits you, both physically and spiritually.",
        "You will discover a hidden talent soon.",
        "Fortune favors the bold; take a chance!",
        "You will soon gain something you have long desired."
    ]
    
    return random.choice(fortunes)

def main():
    print("Welcome to the Fortune Teller Simulation!")
    while True:
        input("Press Enter to receive your fortune... ")
        fortune = get_fortune()
        print(f"Your fortune: {fortune}")
        again = input("Would you like to ask again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thank you for visiting the Fortune Teller. Goodbye!")
            break

if __name__ == "__main__":
    main()
