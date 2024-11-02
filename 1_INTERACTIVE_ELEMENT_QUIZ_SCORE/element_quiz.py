
import tkinter as tk
import random

elements = [
    {"name": "Hydrogen", "symbol": "H", "number": 1},
    {"name": "Helium", "symbol": "He", "number": 2},
    {"name": "Lithium", "symbol": "Li", "number": 3},
    # Add more elements as needed...
]

class ElementQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Element Quiz")
        
        self.score = 0
        self.current_question = None
        self.answer_var = tk.StringVar()
        
        self.question_label = tk.Label(root, text="", font=("Arial", 14))
        self.question_label.pack(pady=10)
        
        self.answer_entry = tk.Entry(root, textvariable=self.answer_var, font=("Arial", 12))
        self.answer_entry.pack(pady=5)
        
        self.submit_button = tk.Button(root, text="Submit Answer", command=self.check_answer)
        self.submit_button.pack(pady=5)
        
        self.feedback_label = tk.Label(root, text="", font=("Arial", 12))
        self.feedback_label.pack(pady=5)
        
        self.score_label = tk.Label(root, text=f"Score: {self.score}", font=("Arial", 12))
        self.score_label.pack(pady=10)
        
        self.next_question()
    
    def next_question(self):
        self.current_question = random.choice(elements)
        question_type = random.choice(["symbol", "number"])
        
        if question_type == "symbol":
            self.question_label.config(text=f"What is the symbol for {self.current_question['name']}?")
        else:
            self.question_label.config(text=f"What is the atomic number for {self.current_question['name']}?")
        
        self.answer_var.set("")
        self.feedback_label.config(text="")

    def check_answer(self):
        answer = self.answer_var.get().strip()
        correct_answer = str(self.current_question["symbol"] if "symbol" in self.question_label.cget("text") else self.current_question["number"])
        
        if answer.lower() == correct_answer.lower():
            self.feedback_label.config(text="Correct!", fg="green")
            self.score += 1
        else:
            self.feedback_label.config(text=f"Incorrect. The correct answer is {correct_answer}.", fg="red")
        
        self.score_label.config(text=f"Score: {self.score}")
        self.root.after(1000, self.next_question)

if __name__ == "__main__":
    root = tk.Tk()
    app = ElementQuiz(root)
    root.mainloop()
