import random

# Predefined sets of characters, settings, actions, objects, and twists
characters = [
    "a fearless astronaut",
    "a quirky inventor",
    "a shape-shifting fox",
    "an undercover spy",
    "a lost pirate",
    "a time-traveling detective",
    "a clumsy wizard"
]

settings = [
    "on a hidden island",
    "inside a parallel universe",
    "in a floating city",
    "within an ancient temple",
    "in a dystopian future",
    "aboard a cursed ship",
    "in a secret laboratory"
]

actions = [
    "uncovered a dark conspiracy",
    "awakened an ancient evil",
    "triggered a catastrophic event",
    "found the key to immortality",
    "faced their greatest fear",
    "was forced to make an impossible choice",
    "discovered the ultimate truth"
]

objects = [
    "a golden compass",
    "an enchanted sword",
    "a cryptic journal",
    "a mysterious gem",
    "a cursed relic",
    "an ancient scroll",
    "a futuristic gadget"
]

twists = [
    "but time was running out",
    "and their memories began to fade",
    "but it was all part of a bigger plan",
    "and they realized they were part of the prophecy",
    "but they could never return home",
    "only to find out they had been betrayed",
    "but they were no longer human"
]


def print_intro():
    print("Welcome to the Extended Random Story Generator!")
    print("Each story is unique, filled with adventure, danger, and unexpected twists.")
    print("Let's dive into the tale...\n")


def generate_story():
    character = random.choice(characters)
    setting = random.choice(settings)
    action = random.choice(actions)
    obj = random.choice(objects)
    twist = random.choice(twists)

    story = (f"Once, {character} was {setting}. They discovered {obj} and {action}, "
             f"{twist}. The journey changed everything for them.")

    return story


def ask_for_another():
    response = input("\nWould you like to generate another story? (yes/no): ").lower()
    return response == 'yes'


def main():
    print_intro()
    while True:
        story = generate_story()
        print(story)
        if not ask_for_another():
            break
    print("\nThanks for using the Extended Random Story Generator! Goodbye!")


if __name__ == "__main__":
    main()
