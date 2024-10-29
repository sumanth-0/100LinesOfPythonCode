import random
import time
import os

# Function to generate Simon's pattern
def generate_simon_pattern(length=10):
    colors = ['R', 'G', 'B', 'Y']
    return [random.choice(colors) for _ in range(length)]

# Function to clear the console (works on most OS)
def clear_console():
    # Check if operating system is Windows
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Function to display Simon's pattern with a delay
def show_simon_pattern(simon_pattern):
    for color in simon_pattern:
        print(color, end=' ', flush=True)
        time.sleep(1)  # Display each color with 1s delay
    time.sleep(2)  # Wait for 2 second before clearing
    clear_console()

# Function to compare Simon's pattern with user's pattern
def compare_patterns(simon_pattern, user_pattern):
    user_score = 0
    min_length = min(len(simon_pattern), len(user_pattern))

    # Use a two-pointer approach to compare both patterns
    for i in range(min_length):
        if simon_pattern[i] == user_pattern[i]:
            user_score += 1  # Increase score for correct match
    return user_score

def main():
    print("Welcome to Simon Says!")

    # Generate Simon's pattern
    simon_pattern = generate_simon_pattern()

    # Show Simon's pattern with delay
    print("Watch carefully!")
    show_simon_pattern(simon_pattern)

    # Get user's pattern as input after clearing the console
    user_input = input("Now repeat the sequence (use R, G, B, Y separated by space): ")
    user_pattern = user_input.split()  # Convert input string to a list

    # Calculate score using two-pointer comparison
    user_score = compare_patterns(simon_pattern, user_pattern)

    print(f"Your score: {user_score}")
    print("Simon's pattern was:", ' '.join(simon_pattern))

if __name__ == "__main__":
    main()
