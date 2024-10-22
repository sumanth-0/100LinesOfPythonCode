import random

# Function to roll the dice
def roll_dice():
    return random.randint(1, 6)
  
def dice_roller():
    while True:
        # taking input from user
        roll = input("Press 'r' to roll the dice, or 'q' to quit: ").lower()

        if roll == 'r':
            result = roll_dice()
            print(f"You rolled a {result}!")
        elif roll == 'q':
              print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid input. Please press 'r' to roll or 'q' to quit.")
          
if __name__ == "__main__":
    dice_roller()
