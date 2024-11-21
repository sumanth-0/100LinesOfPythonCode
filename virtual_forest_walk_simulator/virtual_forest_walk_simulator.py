# virtual_forest_walk_simulator.py

import time
import random

class VirtualForestWalk:
    def __init__(self):
        self.sounds = [
            "Birds chirping",
            "Leaves rustling",
            "Stream flowing",
            "Wind blowing through trees",
            "Rain pattering on leaves",
            "Distant thunder",
            "Footsteps on the forest floor"
        ]
        self.intensity_levels = ["Low", "Medium", "High"]
        self.selected_sounds = []
        self.selected_intensity = "Medium"

    def play_sound(self):
        """Simulate the sound environment in the forest walk."""
        if not self.selected_sounds:
            print("\nNo sounds selected. Please choose sounds to play.")
            return

        print("\nStarting your virtual forest walk...")
        for sound in self.selected_sounds:
            print(f"Playing: {sound} at {self.selected_intensity} intensity.")
            time.sleep(3)  # Simulate the sound playing for a short duration
        print("\nEnjoy the peaceful walk! Press Ctrl+C to exit.")

    def customize_walk(self):
        """Let users customize the soundscape of the forest walk."""
        print("\nChoose sounds for your forest walk:")
        for i, sound in enumerate(self.sounds, 1):
            print(f"{i}. {sound}")
        choices = input("\nEnter the numbers of the sounds you'd like (separate with commas): ").split(',')
        self.selected_sounds = [self.sounds[int(choice)-1] for choice in choices]

        print("\nSelect intensity for the sounds:")
        for i, level in enumerate(self.intensity_levels, 1):
            print(f"{i}. {level}")
        intensity_choice = int(input("Enter the number for intensity (1=Low, 2=Medium, 3=High): "))
        self.selected_intensity = self.intensity_levels[intensity_choice - 1]

    def start_walk(self):
        """Start the forest walk with user customization."""
        print("\nWelcome to the Virtual Forest Walk Simulator!")
        self.customize_walk()
        self.play_sound()

def main():
    forest_walk = VirtualForestWalk()
    forest_walk.start_walk()

if __name__ == "__main__":
    main()
