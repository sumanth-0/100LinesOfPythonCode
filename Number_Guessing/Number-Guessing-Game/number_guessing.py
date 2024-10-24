import random

def get_random_number(lower, upper):
    """Generate a random number between lower and upper bounds."""
    return random.randint(lower, upper)

def get_user_guess():
    """Prompt user for a guess and return it."""
    while True:
        try:
            guess = int(input("Enter your guess: "))
            return guess
        except ValueError:
            print("Please enter a valid integer.")

def play_game():
    """Main function to play the number guessing game."""
    print("Welcome to the Number Guessing Game!")
    lower_bound = 1
    upper_bound = 100
    random_number = get_random_number(lower_bound, upper_bound)
    attempts = 0
    max_attempts = 10

    print(f"Guess a number between {lower_bound} and {upper_bound}. You have {max_attempts} attempts.")

    while attempts < max_attempts:
        guess = get_user_guess()
        attempts += 1

        if guess < lower_bound or guess > upper_bound:
            print(f"Please guess a number within the range ({lower_bound}-{upper_bound}).")
            continue

        if guess < random_number:
            print("Too low! Try again.")
        elif guess > random_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {random_number} in {attempts} attempts.")
            break
    else:
        print(f"Sorry, you've run out of attempts. The number was {random_number}.")

if __name__ == "__main__":
    play_game()
