
import tkinter as tk
import random

class StoryPlotGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Story Plot Generator")
        
        tk.Button(root, text="Generate Plot", command=self.generate_plot).pack(pady=20)
        
        self.plot_label = tk.Label(root, text="", wraplength=300, justify="left")
        self.plot_label.pack(pady=10)
        
        self.characters = ["a brave knight", "a cunning detective", "an alien from Mars"]
        self.settings = ["in an abandoned castle", "on a distant planet", "during a stormy night"]
        self.conflicts = ["facing a secret enemy", "trying to save the world", "lost without any memory"]

    def generate_plot(self):
        character = random.choice(self.characters)
        setting = random.choice(self.settings)
        conflict = random.choice(self.conflicts)
        plot = f"{character} {setting}, {conflict}."
        self.plot_label.config(text=plot)

if __name__ == "__main__":
    root = tk.Tk()
    app = StoryPlotGenerator(root)
    root.mainloop()
