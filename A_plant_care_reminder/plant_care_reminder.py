# plant_care_reminder.py

import time
from datetime import datetime, timedelta

class Plant:
    def __init__(self, name, water_interval, fertilize_interval, rotate_interval):
        self.name = name
        self.water_interval = water_interval
        self.fertilize_interval = fertilize_interval
        self.rotate_interval = rotate_interval
        self.last_watered = datetime.now()
        self.last_fertilized = datetime.now()
        self.last_rotated = datetime.now()

    def needs_care(self):
        """Check what care the plant needs."""
        now = datetime.now()
        care_tasks = []
        if now >= self.last_watered + timedelta(days=self.water_interval):
            care_tasks.append("Water")
        if now >= self.last_fertilized + timedelta(days=self.fertilize_interval):
            care_tasks.append("Fertilize")
        if now >= self.last_rotated + timedelta(days=self.rotate_interval):
            care_tasks.append("Rotate")
        return care_tasks

    def perform_care(self, task):
        """Update the last performed care action."""
        now = datetime.now()
        if task == "Water":
            self.last_watered = now
        elif task == "Fertilize":
            self.last_fertilized = now
        elif task == "Rotate":
            self.last_rotated = now

class PlantCareReminder:
    def __init__(self):
        self.plants = []

    def add_plant(self, name, water_interval, fertilize_interval, rotate_interval):
        """Add a new plant to the tracker."""
        plant = Plant(name, water_interval, fertilize_interval, rotate_interval)
        self.plants.append(plant)
        print(f"Added {name} to your plant care tracker.")

    def check_care(self):
        """Display care tasks for all plants."""
        print("\nPlant Care Summary:")
        for plant in self.plants:
            care_tasks = plant.needs_care()
            if care_tasks:
                print(f"{plant.name} needs: {', '.join(care_tasks)}")
            else:
                print(f"{plant.name} is all set for now.")

    def care_for_plant(self, plant_name, task):
        """Perform a care task for a specific plant."""
        for plant in self.plants:
            if plant.name == plant_name:
                plant.perform_care(task)
                print(f"Performed '{task}' for {plant.name}.")
                return
        print(f"No plant found with the name {plant_name}.")

def main():
    tracker = PlantCareReminder()
    print("Welcome to Plant Care Reminder!")
    
    while True:
        print("\nOptions:")
        print("1. Add a plant")
        print("2. Check plant care needs")
        print("3. Care for a plant")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter plant name: ")
            water_interval = int(input("Watering interval (days): "))
            fertilize_interval = int(input("Fertilizing interval (days): "))
            rotate_interval = int(input("Rotating interval (days): "))
            tracker.add_plant(name, water_interval, fertilize_interval, rotate_interval)
        elif choice == "2":
            tracker.check_care()
        elif choice == "3":
            plant_name = input("Enter the plant name: ")
            task = input("Enter the task (Water/Fertilize/Rotate): ")
            tracker.care_for_plant(plant_name, task)
        elif choice == "4":
            print("Goodbye! Remember to care for your plants!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
