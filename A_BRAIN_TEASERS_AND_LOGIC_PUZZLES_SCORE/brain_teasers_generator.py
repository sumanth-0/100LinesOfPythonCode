
import random
import tkinter as tk
from tkinter import messagebox

class BrainTeasersGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Brain Teasers and Logic Puzzles")
        
        self.teasers = [
            {"question": "I speak without a mouth and hear without ears. What am I?", "answer": "echo"},
            {"question": "The more of this there is, the less you see. What is it?", "answer": "darkness"},
            {"question": "What has keys but can't open locks?", "answer": "piano"},
            {"question": "I’m tall when I’m young and short when I’m old. What am I?", "answer": "candle"},
            {"question": "What has to be broken before you can use it?", "answer": "egg"},
        ]
        
        self.score = 0
        self.current_teaser = None
        
        self.question_label = tk.Label(root, text="Press 'New Teaser' to start!", wraplength=300, justify="left")
        self.question_label.pack(pady=10)
        
        self.answer_entry = tk.Entry(root)
        self.answer_entry.pack(pady=5)
        
        tk.Button(root, text="Check Answer", command=self.check_answer).pack(pady=5)
        tk.Button(root, text="New Teaser", command=self.new_teaser).pack(pady=5)
        
        self.result_label = tk.Label(root, text="", wraplength=300, justify="left")
        self.result_label.pack(pady=10)
        
        self.score_label = tk.Label(root, text="Score: 0")
        self.score_label.pack(pady=10)
    
    def new_teaser(self):
        self.current_teaser = random.choice(self.teasers)
        self.question_label.config(text=self.current_teaser["question"])
        self.answer_entry.delete(0, tk.END)
        self.result_label.config(text="")

    def check_answer(self):
        answer = self.answer_entry.get().strip().lower()
        if self.current_teaser and answer == self.current_teaser["answer"]:
            self.result_label.config(text="Correct! Great job!")
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
        else:
            self.result_label.config(text="Incorrect. Try again or press 'New Teaser' for another puzzle.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BrainTeasersGenerator(root)
    root.mainloop()
