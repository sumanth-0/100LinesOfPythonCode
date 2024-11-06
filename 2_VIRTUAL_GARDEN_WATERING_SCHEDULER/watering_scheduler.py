class Plant:
    def __init__(self, name, water_freq):
        self.name = name
        self.water_freq = water_freq  # in days
        self.days_since_last_water = 0

    def needs_water(self):
        return self.days_since_last_water >= self.water_freq

    def water(self):
        self.days_since_last_water = 0

    def day_passed(self):
        self.days_since_last_water += 1

def main():
    plants = []
    print("Virtual Garden Watering Scheduler")
    
    while True:
        name = input("Enter plant name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        try:
            water_freq = int(input(f"Enter watering frequency for {name} (in days): "))
            plant = Plant(name, water_freq)
            plants.append(plant)
        except ValueError:
            print("Please enter a valid number for watering frequency.")
    
    print("\nDaily Watering Reminder:")
    for day in range(7):  # Simulating a week
        print(f"\nDay {day + 1}:")
        for plant in plants:
            plant.day_passed()
            if plant.needs_water():
                print(f"Water {plant.name} today!")
                plant.water()  # Watering the plant after reminder

if __name__ == "__main__":
    main()
