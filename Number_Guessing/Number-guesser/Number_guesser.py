import random

def play_game():
    random_num = random.randint(1, 100)
    guesses = 0
    while True:
        try:
            user = input(f"Guess #{guesses + 1} (1-100) or 'q' to quit: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting game.")
            return False

        if user.lower() == 'q':
            print("Quitting current game.")
            return False

        try:
            guess = int(user)
        except ValueError:
            print("Please enter a valid integer between 1 and 100, or 'q' to quit.")
            continue

        if not 1 <= guess <= 100:
            print("Please guess a number between 1 and 100.")
            continue

        guesses += 1

        if guess == random_num:
            plural = "guess" if guesses == 1 else "guesses"
            print(f"You won in {guesses} {plural}! The number was {random_num}.")
            return True
        elif guess > random_num:
            print("Your guess is too high.")
        else:
            print("Your guess is too low.")

def main():
    while True:
        play_game()
        try:
            answer = input("Would you like to play again? (Y/N): ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye.")
            return
        if answer in ('n', 'no'):
            print("Thanks for playing. Goodbye.")
            return
        if answer in ('y', 'yes'):
            continue
        print("Please answer Y or N.")

if __name__ == "__main__":
    main()