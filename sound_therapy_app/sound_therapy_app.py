# sound_therapy_app.py

import pygame
import time
import os

SOUNDS = {
    "Ocean Waves": "sounds/ocean_waves.mp3",
    "Rain": "sounds/rain.mp3",
    "Ambient Music": "sounds/ambient_music.mp3"
}

def play_sound(sound_name):
    """Play the selected sound."""
    if sound_name not in SOUNDS:
        print("Invalid selection. Please choose a valid sound.")
        return

    pygame.mixer.init()
    pygame.mixer.music.load(SOUNDS[sound_name])
    pygame.mixer.music.play(-1)  # Loop indefinitely
    print(f"Playing: {sound_name}. Press Enter to stop.")
    input()  # Wait for user to stop the sound
    pygame.mixer.music.stop()

def display_menu():
    """Display the sound menu."""
    print("\nSound Therapy & Relaxation App")
    print("Available Sounds:")
    for i, sound in enumerate(SOUNDS.keys(), 1):
        print(f"[{i}] {sound}")
    print("[0] Exit")

def main():
    """Main function to run the app."""
    if not os.path.exists("sounds"):
        print("Error: Sounds directory is missing.")
        return

    print("Welcome to the Sound Therapy & Relaxation App!")
    while True:
        display_menu()
        choice = input("Choose a sound to play or exit: ").strip()

        if choice == "0":
            print("Goodbye! Stay relaxed!")
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(SOUNDS):
            selected_sound = list(SOUNDS.keys())[int(choice) - 1]
            play_sound(selected_sound)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
