
import tkinter as tk
from tkinter import colorchooser

class ColorPaletteGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Color Palette Generator")
        self.choose_button = tk.Button(root, text="Choose Color", command=self.pick_color)
        self.choose_button.pack(pady=10)
        self.palette_label = tk.Label(root, text="", font=("Arial", 12))
        self.palette_label.pack(pady=10)

    def pick_color(self):
        color_code = colorchooser.askcolor(title="Choose Base Color")[1]
        if color_code:
            palette = self.generate_palette(color_code)
            self.palette_label.config(text=f"Palette: {', '.join(palette)}")

    def generate_palette(self, base_color):
        # Simplified palette generation
        return [base_color, "#ffffff", "#000000", "#ff0000", "#00ff00"]

if __name__ == "__main__":
    root = tk.Tk()
    app = ColorPaletteGenerator(root)
    root.mainloop()
