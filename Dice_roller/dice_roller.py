import random
import time  # Import time for sleep function

# Function to roll the dice
def roll_dice():
    return random.randint(1, 6)
  
def dice_roller():
    while True:
        # Taking input from user
        roll = input("Press 'r' to roll the dice, or 'q' to quit: ").lower()

        if roll == 'r':
            result = roll_dice()
            print(f"You rolled a {result}!")
            time.sleep(1)  # Optional: wait for 1 second before the next prompt
        elif roll == 'q':
            print("Thanks for playing! Goodbye!")
            break  # Exit the loop and end the program
        else:
            print("Invalid input. Please press 'r' to roll or 'q' to quit.")
          
if __name__ == "__main__":
    dice_roller()
