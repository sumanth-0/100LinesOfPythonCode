
import random
import tkinter as tk

captions = {
    "inspirational": [
        "Chasing dreams, one step at a time. 🌟",
        "Believe in yourself and all that you are. ✨",
        "Every day is a new beginning. Embrace it!",
    ],
    "humorous": [
        "I need six months of vacation, twice a year. 😜",
        "I'm on a seafood diet. I see food, and I eat it. 🦀",
        "Current mood: 100% myself, 0% sorry. 😎",
    ],
    "travel": [
        "Exploring the world, one city at a time. 🌍",
        "Wander often, wonder always.",
        "Take only memories, leave only footprints.",
    ]
}

class CaptionGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Social Media Caption Generator")
        
        self.theme_var = tk.StringVar()
        
        tk.Label(root, text="Select a Theme:", font=("Arial", 12)).pack(pady=5)
        
        for theme in captions.keys():
            tk.Radiobutton(root, text=theme.capitalize(), variable=self.theme_var, value=theme, font=("Arial", 10)).pack(anchor="w")
        
        self.generate_button = tk.Button(root, text="Generate Caption", command=self.generate_caption)
        self.generate_button.pack(pady=10)
        
        self.caption_label = tk.Label(root, text="", font=("Arial", 12, "italic"), wraplength=250, fg="blue")
        self.caption_label.pack(pady=5)
    
    def generate_caption(self):
        theme = self.theme_var.get()
        if theme:
            caption = random.choice(captions[theme])
            self.caption_label.config(text=caption)
        else:
            self.caption_label.config(text="Please select a theme first!", fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = CaptionGenerator(root)
    root.mainloop()
