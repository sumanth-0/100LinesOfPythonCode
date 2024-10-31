
import tkinter as tk
import random

class LanguageFlashcards:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Learning Flashcards")
        self.words = {"hello": "hola", "world": "mundo", "thanks": "gracias"}
        self.create_gui()

    def create_gui(self):
        self.word_label = tk.Label(self.root, text="", font=("Arial", 16))
        self.word_label.pack(pady=10)
        
        show_button = tk.Button(self.root, text="Show Word", command=self.show_word)
        show_button.pack(pady=5)
        
        self.translation_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.translation_label.pack(pady=5)
        
        mark_button = tk.Button(self.root, text="Mark as Known", command=self.mark_known)
        mark_button.pack(pady=5)

    def show_word(self):
        self.current_word, self.translation = random.choice(list(self.words.items()))
        self.word_label.config(text=self.current_word)
        self.translation_label.config(text="")

    def mark_known(self):
        self.translation_label.config(text=f"Translation: {self.translation}")
        del self.words[self.current_word]

if __name__ == "__main__":
    root = tk.Tk()
    app = LanguageFlashcards(root)
    root.mainloop()
