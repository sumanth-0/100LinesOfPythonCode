import random
import tkinter as tk

class RandomFactsGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title("Random Facts Generator")

        self.facts = [
            "Honey never spoils.",
            "Octopuses have three hearts.",
            "Bananas are berries, but strawberries aren't.",
            "A group of flamingos is called a 'flamboyance'.",
            "Wombat poop is cube-shaped.",
            "Cats have fewer toes on their back paws."
        ]

        self.fact_label = tk.Label(master, text="", wraplength=300)
        self.fact_label.pack(pady=20)

        self.generate_button = tk.Button(master, text="Generate Random Fact", command=self.generate_fact)
        self.generate_button.pack(pady=10)

    def generate_fact(self):
        fact = random.choice(self.facts)
        self.fact_label.config(text=fact)

if __name__ == "__main__":
    root = tk.Tk()
    random_facts_app = RandomFactsGenerator(root)
    root.mainloop()
