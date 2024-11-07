import random
import time

# Sample database of animal sounds
ANIMAL_SOUNDS = {
    "Lion": "roar",
    "Dog": "bark",
    "Cat": "meow",
    "Cow": "moo",
    "Elephant": "trumpet"
}

def play_sound(animal: str) -> None:
    print(f"Playing sound: {ANIMAL_SOUNDS[animal]}")  # Simulate playing sound

def animal_quiz() -> None:
    animal = random.choice(list(ANIMAL_SOUNDS.keys()))
    attempts = 3
    print("\nGuess the animal sound!\n")

    while attempts > 0:
        play_sound(animal)
        guess = input("Your guess: ").strip().capitalize()
        if guess == animal:
            print("Correct! Well done!")
            return
        else:
            attempts -= 1
            print(f"Wrong! {attempts} attempts remaining.")
            if attempts == 1:
                print(f"Hint: The animal starts with '{animal[0]}'.")

    print(f"Out of attempts! The correct answer was: {animal}.")

def main():
    print("Welcome to the Animal Sound Recognizer!")
    score = 0
    rounds = int(input("How many rounds would you like to play? "))
    for _ in range(rounds):
        animal_quiz()
        score += 1
        time.sleep(1)

    print(f"\nGame Over! Your final score is {score}/{rounds}.")

if __name__ == "__main__":
    main()
