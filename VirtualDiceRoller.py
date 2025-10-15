import random

def roll_dice(num_dice, num_sides):
    """
    Simulates rolling a specified number of dice with a specified number of sides.

    Args:
        num_dice (int): The number of dice to roll.
        num_sides (int): The number of sides on each die.

    Returns:
        list: A list of integers representing the outcome of each die roll.
    """
    if num_dice <= 0 or num_sides <= 0:
        return []
    
    rolls = []
    for _ in range(num_dice):
        roll = random.randint(1, num_sides)
        rolls.append(roll)
    return rolls

def main():
    """
    Main function to run the dice rolling simulator.
    """
    print("--- Dice Rolling Simulator ---")

    while True:
        try:
            # Get user input for the number of dice
            num_dice_input = input("Enter the number of dice to roll (or 'q' to quit): ")
            if num_dice_input.lower() == 'q':
                break

            num_dice = int(num_dice_input)

            # Get user input for the number of sides
            num_sides = int(input("Enter the number of sides on each die (e.g., 6): "))

            if num_dice <= 0 or num_sides <= 0:
                print("Please enter positive numbers for dice and sides.")
                continue

            # Roll the dice
            results = roll_dice(num_dice, num_sides)
            total = sum(results)

            # Print the results
            print("\n--- Results ---")
            print(f"You rolled {num_dice} dice with {num_sides} sides.")
            print(f"Outcomes: {results}")
            print(f"Total: {total}")
            print("-----------------\n")

        except ValueError:
            print("Invalid input. Please enter whole numbers.")
        except Exception as e:
            print(f"An error occurred: {e}")

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
