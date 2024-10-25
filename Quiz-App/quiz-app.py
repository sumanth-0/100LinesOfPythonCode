import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.root.geometry("400x300")
        
        # Quiz data: questions, options, and answers
        self.questions = [
            {"question": "What is the capital of France?", "options": ["Paris", "Rome", "Berlin", "Madrid"], "answer": "Paris"},
            {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Saturn"], "answer": "Mars"},
            {"question": "What is the largest ocean?", "options": ["Atlantic", "Indian", "Pacific", "Arctic"], "answer": "Pacific"}
        ]
        
        self.current_question = 0
        self.score = 0

        # UI components
        self.question_label = tk.Label(root, text="", font=("Arial", 12), wraplength=300)
        self.question_label.pack(pady=20)
        
        self.option_var = tk.StringVar()
        self.options = []
        for i in range(4):
            radio_btn = tk.Radiobutton(root, text="", variable=self.option_var, value="", font=("Arial", 10))
            radio_btn.pack(anchor="w", padx=50)
            self.options.append(radio_btn)
        
        self.submit_btn = tk.Button(root, text="Submit Answer", command=self.submit_answer)
        self.submit_btn.pack(pady=10)
        
        self.next_btn = tk.Button(root, text="Next Question", command=self.next_question, state="disabled")
        self.next_btn.pack(pady=5)
        
        self.load_question()

    def load_question(self):
        """Loads the current question and its options."""
        self.option_var.set("")
        question_data = self.questions[self.current_question]
        self.question_label.config(text=question_data["question"])
        
        for i, option in enumerate(question_data["options"]):
            self.options[i].config(text=option, value=option)
        
        self.submit_btn.config(state="normal")
        self.next_btn.config(state="disabled")
    
    def submit_answer(self):
        """Checks the user's answer and updates the score."""
        selected_answer = self.option_var.get()
        correct_answer = self.questions[self.current_question]["answer"]
        
        if selected_answer == correct_answer:
            self.score += 1
            messagebox.showinfo("Correct!", "Good job! That's the right answer.")
        else:
            messagebox.showinfo("Incorrect", f"Oops! The correct answer was: {correct_answer}.")
        
        self.submit_btn.config(state="disabled")
        self.next_btn.config(state="normal")
    
    def next_question(self):
        """Moves to the next question or shows the final score if quiz is over."""
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.load_question()
        else:
            messagebox.showinfo("Quiz Complete", f"You've completed the quiz! Your score: {self.score}/{len(self.questions)}")
            self.root.destroy()

# Initialize the quiz app
root = tk.Tk()
app = QuizApp(root)
root.mainloop()
