import random

class Character:
    def __init__(self, name):
        self.name = name
        self.strength = random.randint(1, 20)
        self.agility = random.randint(1, 20)
        self.intelligence = random.randint(1, 20)

    def display_attributes(self):
        print(f"Character Name: {self.name}")
        print(f"Strength: {self.strength}")
        print(f"Agility: {self.agility}")
        print(f"Intelligence: {self.intelligence}")

def main():
    character_name = input("Enter the character's name: ")
    character = Character(character_name)
    character.display_attributes()

if __name__ == "__main__":
    main()
