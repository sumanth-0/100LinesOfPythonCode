#!/usr/bin/env python3
"""
Guess the Animal Sound Game
A fun CLI game where players guess which animal makes a specific sound.
This game quizzes users on their knowledge of animal sounds.
"""

import random
import sys

# Animal sound database
ANIMAL_SOUNDS = {
    'dog': ['woof', 'bark', 'bow-wow', 'arf'],
    'cat': ['meow', 'purr', 'mew'],
    'cow': ['moo', 'low'],
    'pig': ['oink', 'squeal'],
    'duck': ['quack'],
    'sheep': ['baa', 'bleat'],
    'horse': ['neigh', 'whinny'],
    'lion': ['roar'],
    'elephant': ['trumpet'],
    'owl': ['hoot', 'screech'],
    'frog': ['ribbit', 'croak'],
    'bee': ['buzz'],
    'snake': ['hiss'],
    'rooster': ['cock-a-doodle-doo', 'crow'],
    'donkey': ['hee-haw', 'bray'],
    'wolf': ['howl', 'awoo'],
    'bird': ['chirp', 'tweet'],
    'mouse': ['squeak'],
    'goat': ['bleat', 'maa'],
    'turkey': ['gobble']
}

def display_welcome():
    """Display welcome message and game instructions."""
    print("\n" + "="*50)
    print("🐾 GUESS THE ANIMAL SOUND GAME 🐾")
    print("="*50)
    print("\nWelcome! Test your knowledge of animal sounds!")
    print("You'll be given a sound, and you need to guess the animal.\n")

def get_random_question():
    """Generate a random question with animal and sound."""
    animal = random.choice(list(ANIMAL_SOUNDS.keys()))
    sound = random.choice(ANIMAL_SOUNDS[animal])
    return animal, sound

def generate_options(correct_animal, num_options=4):
    """Generate multiple choice options including the correct answer."""
    options = [correct_animal]
    all_animals = list(ANIMAL_SOUNDS.keys())
    all_animals.remove(correct_animal)
    
    while len(options) < num_options and len(all_animals) > 0:
        option = random.choice(all_animals)
        all_animals.remove(option)
        options.append(option)
    
    random.shuffle(options)
    return options

def display_question(sound, options, question_num):
    """Display the question and options to the player."""
    print(f"\nQuestion {question_num}:")
    print(f"What animal makes this sound: '{sound}'?\n")
    
    for idx, option in enumerate(options, 1):
        print(f"{idx}. {option.capitalize()}")
    print()

def get_player_answer(num_options):
    """Get and validate player's answer."""
    while True:
        try:
            answer = input("Your answer (1-4): ").strip()
            answer_num = int(answer)
            if 1 <= answer_num <= num_options:
                return answer_num
            else:
                print(f"Please enter a number between 1 and {num_options}.")
        except ValueError:
            print("Invalid input! Please enter a number.")
        except KeyboardInterrupt:
            print("\n\nGame interrupted. Goodbye!")
            sys.exit(0)

def play_game():
    """Main game loop."""
    display_welcome()
    
    # Game settings
    num_questions = 5
    score = 0
    
    print(f"You will answer {num_questions} questions. Let's begin!\n")
    input("Press Enter to start...")
    
    for question_num in range(1, num_questions + 1):
        # Generate question
        correct_animal, sound = get_random_question()
        options = generate_options(correct_animal)
        
        # Display question
        display_question(sound, options, question_num)
        
        # Get player's answer
        player_answer = get_player_answer(len(options))
        selected_animal = options[player_answer - 1]
        
        # Check answer
        if selected_animal == correct_animal:
            print("✓ Correct! 🎉")
            score += 1
        else:
            print(f"✗ Wrong! The correct answer was: {correct_animal.capitalize()}")
        
        # Show score
        print(f"Current score: {score}/{question_num}")
    
    # Final results
    print("\n" + "="*50)
    print("GAME OVER!")
    print("="*50)
    print(f"\nFinal Score: {score}/{num_questions}")
    
    percentage = (score / num_questions) * 100
    if percentage == 100:
        print("🏆 Perfect! You're an animal sound expert!")
    elif percentage >= 80:
        print("🌟 Excellent! You know your animal sounds well!")
    elif percentage >= 60:
        print("👍 Good job! Keep learning!")
    else:
        print("📚 Keep practicing! You'll get better!")
    
    print("\nThank you for playing!\n")

if __name__ == "__main__":
    play_game()
