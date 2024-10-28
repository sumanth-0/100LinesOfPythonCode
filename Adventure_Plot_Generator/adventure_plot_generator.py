import random

def generate_plot():
    """Generate a random adventure plot with unique characters, settings, and challenges."""
    characters = ['a brave knight', 'a cunning thief', 'a wise wizard', 'a fearless warrior', 'an unlikely hero']
    settings = ['in a haunted forest', 'in a distant galaxy', 'in an ancient castle', 'on a deserted island', 'in a bustling city']
    challenges = ['facing a dragon', 'solving an ancient riddle', 'battling a dark sorcerer', 'escaping from a sinking ship', 'finding a hidden treasure']

    character = random.choice(characters)
    setting = random.choice(settings)
    challenge = random.choice(challenges)

    return f"Plot: {character} {setting}, {challenge}."

def main():
    print("Welcome to the Random Adventure Plot Generator!")
    user_input = input("Press Enter to generate a random adventure plot.")
    
    if user_input == "":
        print(generate_plot())
    else:
        print("Goodbye!")

if __name__ == "__main__":
    main()
