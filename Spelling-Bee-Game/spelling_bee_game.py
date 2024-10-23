import random
import pyttsx3

# List of words for the spelling bee game
word_list = ["apple", "banana", "grapefruit", "strawberry", "watermelon", "pineapple", "blueberry", "orange", "mango", "papaya"]

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak_word(word):
    """Speaks the word using text-to-speech."""
    engine.say(word)
    engine.runAndWait()

def spelling_bee_game():
    correct_count = 0
    incorrect_count = 0

    print("Welcome to the Spelling Bee Game!")
    print("I will speak out a word, and you have to type its correct spelling.")
    print("Type 'exit' anytime to quit the game.\n")

    while True:
        word = random.choice(word_list)
        speak_word(word)

        user_input = input("Spell the word: ")

        # Exit the game if the user types 'exit'
        if user_input.lower() == 'exit':
            break

        # Check if the user spelled the word correctly
        if user_input.lower() == word.lower():
            print("Correct!\n")
            correct_count += 1
        else:
            print(f"Incorrect! The correct spelling was '{word}'.\n")
            incorrect_count += 1

    # Game Over Summary
    print("Game Over! Here's your final score:")
    print(f"Correct Answers: {correct_count}")
    print(f"Incorrect Answers: {incorrect_count}")

if __name__ == "__main__":
    spelling_bee_game()
