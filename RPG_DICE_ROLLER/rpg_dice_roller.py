import random

class RPGDiceRoller:
    def __init__(self):
        self.dice_types = {
            'd4': 4,
            'd6': 6,
            'd8': 8,
            'd10': 10,
            'd12': 12,
            'd20': 20
        }

    def roll_dice(self, dice, modifier=0):
        if dice not in self.dice_types:
            return "Invalid dice type."
        roll = random.randint(1, self.dice_types[dice])
        return roll + modifier

def main():
    roller = RPGDiceRoller()
    dice_type = input("Enter the dice type (d4, d6, d8, d10, d12, d20): ").strip().lower()
    modifier = input("Enter a modifier (default is 0): ")
    modifier = int(modifier) if modifier.isdigit() else 0
    result = roller.roll_dice(dice_type, modifier)
    print(f"Rolled {dice_type}: {result}")

if __name__ == "__main__":
    main()
