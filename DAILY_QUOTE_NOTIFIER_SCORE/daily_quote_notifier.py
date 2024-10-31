
import tkinter as tk
import random

class QuoteNotifier:
    def __init__(self, root):
        self.root = root
        self.root.title("Daily Quote Notifier")
        self.quotes = [
            "Believe you can and you're halfway there.",
            "The best way to get started is to quit talking and begin doing.",
            "Success is not final, failure is not fatal: it is the courage to continue that counts."
        ]
        self.create_gui()

    def create_gui(self):
        self.quote_label = tk.Label(self.root, text="", wraplength=250, font=("Arial", 12))
        self.quote_label.pack(pady=20)
        self.show_quote()
        
        refresh_button = tk.Button(self.root, text="New Quote", command=self.show_quote)
        refresh_button.pack(pady=10)

    def show_quote(self):
        quote = random.choice(self.quotes)
        self.quote_label.config(text=quote)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuoteNotifier(root)
    root.mainloop()
