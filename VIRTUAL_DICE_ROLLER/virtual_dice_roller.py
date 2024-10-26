import random
import tkinter as tk
from tkinter import messagebox

class VirtualDiceRoller:
    def __init__(self, root):
        self.root = root
        self.root.title("Virtual Dice Roller")
        self.root.geometry("300x200")
        
        self.label = tk.Label(root, text="Enter the number of dice:", font=("Arial", 12))
        self.label.pack(pady=10)
        
        self.dice_entry = tk.Entry(root, font=("Arial", 12))
        self.dice_entry.pack(pady=5)
        
        self.roll_button = tk.Button(root, text="Roll Dice", font=("Arial", 12), command=self.roll_dice)
        self.roll_button.pack(pady=10)
        
        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)
    
    def roll_dice(self):
        try:
            num_dice = int(self.dice_entry.get())
            results = [random.randint(1, 6) for _ in range(num_dice)]
            result_text = " + ".join(map(str, results)) + f" = {sum(results)}"
            self.result_label.config(text=f"Results: {result_text}")
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number of dice.")
            
def main():
    root = tk.Tk()
    app = VirtualDiceRoller(root)
    root.mainloop()

if __name__ == "__main__":
    main()
