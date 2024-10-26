import time
import random

class Plant:
    def __init__(self):
        self.growth_stage = 0
        self.watered = False

    def water(self):
        self.watered = True
        print("You watered the plant!")

    def grow(self):
        if self.watered:
            self.growth_stage += 1
            self.watered = False
            print("The plant has grown!")
        else:
            print("The plant is thirsty and needs water to grow.")

    def show_growth(self):
        stages = ["Seed", "Sprout", "Young Plant", "Mature Plant"]
        if self.growth_stage < len(stages):
            print(f"Current Growth Stage: {stages[self.growth_stage]}")
        else:
            print("The plant has reached its maximum growth!")

def main():
    plant = Plant()
    print("Welcome to the Virtual Plant Simulator!")
    
    while True:
        plant.show_growth()
        action = input("Do you want to (W)ater the plant, (G)row it, or (Q)uit? ").lower()

        if action == 'w':
            plant.water()
        elif action == 'g':
            plant.grow()
        elif action == 'q':
            print("Exiting the simulator.")
            break
        else:
            print("Invalid action! Please choose W, G, or Q.")

        time.sleep(1)

if __name__ == "__main__":
    main()
