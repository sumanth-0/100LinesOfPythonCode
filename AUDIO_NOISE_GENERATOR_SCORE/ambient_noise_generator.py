
import tkinter as tk
from tkinter import messagebox
import random

class AmbientNoiseGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Ambient Noise Generator")
        
        tk.Label(root, text="Choose Your Ambient Sounds:").pack(pady=10)
        
        self.sounds = {
            "Rain": tk.BooleanVar(),
            "Ocean Waves": tk.BooleanVar(),
            "Forest": tk.BooleanVar(),
            "Coffee Shop": tk.BooleanVar(),
            "Campfire": tk.BooleanVar()
        }
        
        for sound in self.sounds:
            tk.Checkbutton(root, text=sound, variable=self.sounds[sound]).pack(anchor="w", padx=10)
        
        play_button = tk.Button(root, text="Play Ambient Noise", command=self.play_ambient_noise)
        play_button.pack(pady=10)
        
        self.result_label = tk.Label(root, text="", wraplength=300, justify="left")
        self.result_label.pack(pady=10)

    def play_ambient_noise(self):
        selected_sounds = [sound for sound, var in self.sounds.items() if var.get()]
        if selected_sounds:
            noise_message = f"Playing {', '.join(selected_sounds)}..."
        else:
            noise_message = "No sounds selected. Please choose an ambient sound to play."
        self.result_label.config(text=noise_message)

if __name__ == "__main__":
    root = tk.Tk()
    app = AmbientNoiseGenerator(root)
    root.mainloop()
