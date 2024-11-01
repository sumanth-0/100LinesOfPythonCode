
import tkinter as tk
from tkinter import messagebox

class CareerPersonalityTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Career Personality Test")
        
        self.questions = [
            "Do you enjoy working with numbers?",
            "Do you like working with people?",
            "Are you interested in technology?",
            "Do you enjoy creative work?",
            "Do you prefer outdoor activities?",
        ]
        
        self.responses = []
        
        tk.Label(root, text="Career Personality Test").pack(pady=10)
        
        for question in self.questions:
            frame = tk.Frame(root)
            frame.pack(anchor="w", pady=5)
            
            tk.Label(frame, text=question).pack(anchor="w")
            response = tk.IntVar(value=0)
            tk.Radiobutton(frame, text="Yes", variable=response, value=1).pack(side="left")
            tk.Radiobutton(frame, text="No", variable=response, value=0).pack(side="left")
            self.responses.append(response)
        
        tk.Button(root, text="Get Career Suggestions", command=self.get_career_suggestions).pack(pady=20)
        
        self.result_label = tk.Label(root, text="", wraplength=300, justify="left")
        self.result_label.pack(pady=10)
    
    def get_career_suggestions(self):
        score = sum([response.get() for response in self.responses])
        if score >= 4:
            suggestion = "Suggested Career: Data Scientist, Engineer, or Software Developer.\nExplore technical and analytical fields."
        elif score >= 2:
            suggestion = "Suggested Career: Marketing Specialist, HR, or Teacher.\nConsider careers with a mix of social and organizational skills."
        else:
            suggestion = "Suggested Career: Artist, Writer, or Outdoor Guide.\nExplore careers that allow for creativity and working independently."
        
        self.result_label.config(text=suggestion)

if __name__ == "__main__":
    root = tk.Tk()
    app = CareerPersonalityTest(root)
    root.mainloop()
