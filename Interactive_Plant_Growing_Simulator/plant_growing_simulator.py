import time

class Plant:
    """Class to represent the plant in the simulator."""
    def __init__(self):
        self.health = 0
        self.stage = 0  # 0: seed, 1: sprout, 2: plant, 3: flower

    def water(self):
        """Water the plant to increase its health."""
        self.health += 1
        self.update_stage()

    def sunlight(self):
        """Provide sunlight to the plant to increase its health."""
        self.health += 1
        self.update_stage()

    def update_stage(self):
        """Update the growth stage based on health."""
        if self.health >= 12:
            self.stage = 3  # Flower
        elif self.health >= 8:
            self.stage = 2  # Plant
        elif self.health >= 4:
            self.stage = 1  # Sprout
        else:
            self.stage = 0  # Seed

    def display(self):
        """Display the current growth stage of the plant."""
        stages = ["🌱 Seed", "🌿 Sprout", "🌳 Plant", "🌸 Flower"]
        print(f"Current Stage: {stages[self.stage]} (Health: {self.health})")


def main():
    """Run the plant growing simulator."""
    plant = Plant()
    print("Welcome to the Interactive Plant Growing Simulator!\n")
    
    while True:
        plant.display()
        action = input("Water (w), Sunlight (s), or Exit (e): ").lower()

        if action == 'w':
            plant.water()
        elif action == 's':
            plant.sunlight()
        elif action == 'e':
            print("Thanks for playing!")
            break
        else:
            print("Invalid action! Please choose 'w', 's', or 'e'.")
        
        time.sleep(1)  # Simulate time delay for realism


if __name__ == "__main__":
    main()
