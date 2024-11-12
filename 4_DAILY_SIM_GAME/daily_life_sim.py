import random

class LifeSimulator:
    def __init__(self):
        self.happiness = 50
        self.energy = 50
        self.finances = 100

    def choose_activity(self, activity):
        if activity == "work":
            self.energy -= 20
            self.finances += 30
            self.happiness -= 10
        elif activity == "hobby":
            self.energy -= 10
            self.happiness += 20
            self.finances -= 5
        elif activity == "rest":
            self.energy += 30
            self.happiness += 10
        else:
            print("Unknown activity.")

        self.check_status()

    def check_status(self):
        self.happiness = max(0, min(self.happiness, 100))
        self.energy = max(0, min(self.energy, 100))
        self.finances = max(0, min(self.finances, 200))

        print(f"Status - Happiness: {self.happiness}, Energy: {self.energy}, Finances: {self.finances}")

    def simulate_day(self):
        activities = ["work", "hobby", "rest"]
        for _ in range(3):  # Choose three activities per day
            activity = random.choice(activities)
            print(f"Activity chosen: {activity}")
            self.choose_activity(activity)

if __name__ == "__main__":
    game = LifeSimulator()
    days = int(input("Enter the number of days to simulate: "))
    for day in range(days):
        print(f"\n--- Day {day + 1} ---")
        game.simulate_day()
