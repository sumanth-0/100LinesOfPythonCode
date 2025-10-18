import random

def display_welcome():
    """Display welcome message and game rules."""
    print("\n" + "="*50)
    print("   Welcome to Dice Guess Challenge!")
    print("="*50)
    print("\nRules:")
    print("1. The computer will roll a dice (1-6)")
    print("2. Try to guess the number!")
    print("3. You have 3 attempts per round")
    print("4. Score points for correct guesses")
    print("5. Try to beat your high score!\n")

def roll_dice():
    """Roll a dice and return a random number between 1 and 6."""
    return random.randint(1, 6)

def get_player_guess():
    """Get and validate player's guess."""
    while True:
        try:
            guess = int(input("Enter your guess (1-6): "))
            if 1 <= guess <= 6:
                return guess
            else:
                print("Please enter a number between 1 and 6!")
        except ValueError:
            print("Invalid input! Please enter a number.")

def play_round():
    """Play a single round of the game."""
    dice_value = roll_dice()
    attempts = 3
    score = 0
    
    print("\n" + "-"*50)
    print("New Round! The dice has been rolled...")
    print(f"You have {attempts} attempts to guess the number.")
    print("-"*50)
    
    for attempt in range(1, attempts + 1):
        print(f"\nAttempt {attempt}/{attempts}")
        guess = get_player_guess()
        
        if guess == dice_value:
            points = (attempts - attempt + 1) * 10
            score += points
            print(f"\n🎉 Correct! You guessed it in {attempt} attempt(s)!")
            print(f"You earned {points} points!")
            return score
        elif guess < dice_value:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
    
    print(f"\n❌ Out of attempts! The dice was: {dice_value}")
    return score

def play_game():
    """Main game loop."""
    display_welcome()
    total_score = 0
    high_score = 0
    rounds_played = 0
    
    while True:
        rounds_played += 1
        print(f"\n{'='*50}")
        print(f"Round {rounds_played} | Current Score: {total_score} | High Score: {high_score}")
        print(f"{'='*50}")
        
        round_score = play_round()
        total_score += round_score
        
        if total_score > high_score:
            high_score = total_score
            if round_score > 0:
                print("\n🏆 New high score!")
        
        print(f"\nRound Score: {round_score}")
        print(f"Total Score: {total_score}")
        
        play_again = input("\nPlay another round? (y/n): ").lower().strip()
        if play_again != 'y':
            break
    
    print("\n" + "="*50)
    print("   Game Over!")
    print("="*50)
    print(f"Rounds Played: {rounds_played}")
    print(f"Final Score: {total_score}")
    print(f"High Score: {high_score}")
    print("\nThanks for playing Dice Guess Challenge!\n")

if __name__ == "__main__":
    play_game()
