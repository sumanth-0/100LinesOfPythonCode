class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.happiness = 50

    def feed(self):
        self.hunger -= 10
        if self.hunger < 0:
            self.hunger = 0
        print(f"{self.name} is being fed! Hunger level: {self.hunger}")

    def play(self):
        self.happiness += 10
        if self.happiness > 100:
            self.happiness = 100
        print(f"{self.name} is playing! Happiness level: {self.happiness}")

    def care(self):
        self.happiness += 5
        self.hunger -= 5
        if self.happiness > 100:
            self.happiness = 100
        if self.hunger < 0:
            self.hunger = 0
        print(f"You're taking care of {self.name}! Happiness: {self.happiness}, Hunger: {self.hunger}")

    def status(self):
        print(f"{self.name}'s current hunger: {self.hunger}, happiness: {self.happiness}")

def main():
    pet_name = input("What is your pet's name? ")
    pet = VirtualPet(pet_name)

    while True:
        print("\nWhat would you like to do?")
        print("1. Feed")
        print("2. Play")
        print("3. Care")
        print("4. Check Status")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            pet.feed()
        elif choice == '2':
            pet.play()
        elif choice == '3':
            pet.care()
        elif choice == '4':
            pet.status()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
