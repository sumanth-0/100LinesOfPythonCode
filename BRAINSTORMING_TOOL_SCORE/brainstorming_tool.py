
import tkinter as tk
from tkinter import messagebox

class BrainstormingTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Brainstorming Tool")
        self.ideas = []
        
        tk.Label(root, text="Idea:").grid(row=0, column=0, padx=10, pady=10)
        self.idea_entry = tk.Entry(root, width=30)
        self.idea_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(root, text="Category:").grid(row=1, column=0, padx=10, pady=10)
        self.category_entry = tk.Entry(root, width=30)
        self.category_entry.grid(row=1, column=1, padx=10, pady=10)

        add_button = tk.Button(root, text="Add Idea", command=self.add_idea)
        add_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.ideas_listbox = tk.Listbox(root, width=50)
        self.ideas_listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def add_idea(self):
        idea = self.idea_entry.get()
        category = self.category_entry.get()
        if idea and category:
            self.ideas.append((idea, category))
            self.ideas_listbox.insert(tk.END, f"{idea} ({category})")
            self.idea_entry.delete(0, tk.END)
            self.category_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Both Idea and Category are required")

if __name__ == "__main__":
    root = tk.Tk()
    app = BrainstormingTool(root)
    root.mainloop()
