import tkinter as tk
import pygame
from tkinter import filedialog

pygame.mixer.init()

def play_sound(file_path):
    sound = pygame.mixer.Sound(file_path)
    sound.play()

def load_sound(button):
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav;*.mp3")])
    if file_path:
        button.config(command=lambda: play_sound(file_path))

root = tk.Tk()
root.title("Soundboard")
root.geometry("300x200")

button1 = tk.Button(root, text="Click", width=10, command=lambda: play_sound('Sounds/click.mp3'))
button1.pack(pady=10)

button2 = tk.Button(root, text="Sound 1", width=10, command=lambda: play_sound('Sounds/soundone.mp3'))
button2.pack(pady=10)

button3 = tk.Button(root, text="Sound 2", width=10, command=lambda: play_sound('Sounds/soundtwo.mp3'))
button3.pack(pady=10)

custom_button = tk.Button(root, text="Load Sound", width=10, command=lambda: load_sound(custom_button))
custom_button.pack(pady=10)

root.mainloop()
