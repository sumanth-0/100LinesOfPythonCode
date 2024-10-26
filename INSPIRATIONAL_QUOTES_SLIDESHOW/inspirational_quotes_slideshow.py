import tkinter as tk
import random

class QuotesSlideshow:
    def __init__(self, master):
        self.master = master
        self.master.title("Inspirational Quotes Slideshow")
        self.master.geometry("600x400")
        self.quotes = [
            "Believe you can and you're halfway there.",
            "The only way to do great work is to love what you do.",
            "You are never too old to set another goal or to dream a new dream.",
            "Act as if what you do makes a difference. It does.",
            "Success is not how high you have climbed, but how you make a positive difference to the world."
        ]
        self.label = tk.Label(master, text="", wraplength=500, font=("Helvetica", 16), bg="lightblue")
        self.label.pack(expand=True, fill='both')
        self.show_quote()
        
    def show_quote(self):
        quote = random.choice(self.quotes)
        self.label.config(text=quote)
        self.master.after(3000, self.show_quote)  # Change quote every 3 seconds

def main():
    root = tk.Tk()
    app = QuotesSlideshow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
