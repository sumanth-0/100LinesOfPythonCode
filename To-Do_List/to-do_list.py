import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
import sqlite3

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("600x400")
        self.main_frame = tk.Frame(self.root, bg="#2E2E2E")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.create_widgets()
        self.create_database()
        self.load_tasks()

    def create_widgets(self):
        frame = tk.Frame(self.main_frame, bg="#2E2E2E", padx=10, pady=10)
        frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

        tk.Label(frame, text="Task:", bg="#2E2E2E", fg="#FFFFFF").grid(row=0, column=0, sticky="w")
        self.task_entry = tk.Entry(frame, width=50, bg="#4B4B4B", fg="#FFFFFF", relief="flat")
        self.task_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame, text="Category:", bg="#2E2E2E", fg="#FFFFFF").grid(row=1, column=0, sticky="w")
        self.category_entry = tk.Entry(frame, width=50, bg="#4B4B4B", fg="#FFFFFF", relief="flat")
        self.category_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame, text="Due Date:", bg="#2E2E2E", fg="#FFFFFF").grid(row=2, column=0, sticky="w")
        self.due_date_entry = DateEntry(frame, width=20, date_pattern='yyyy-mm-dd', background='#4B4B4B', foreground='white', relief="flat")
        self.due_date_entry.grid(row=2, column=1, padx=5, pady=5)

        self.add_task_button = tk.Button(frame, text="Add Task", command=self.add_task, bg="#5A5A5A", fg="#FFFFFF", relief="flat")
        self.add_task_button.grid(row=3, column=1, sticky="e", pady=10)

        self.task_listbox = tk.Listbox(self.main_frame, bg="#2E2E2E", fg="#FFFFFF", height=15, relief="flat")
        self.task_listbox.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        self.delete_task_button = tk.Button(self.main_frame, text="Delete Task", command=self.delete_task, bg="#5A5A5A", fg="#FFFFFF", relief="flat")
        self.delete_task_button.pack(pady=5)

    def create_database(self):
        self.conn = sqlite3.connect("tasks.db")
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY,
                    task TEXT NOT NULL,
                    category TEXT,
                    due_date TEXT
                )
            """)

    def load_tasks(self):
        self.task_listbox.delete(0, tk.END)
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM tasks")
        for row in cursor.fetchall():
            self.task_listbox.insert(tk.END, f"{row[0]}: {row[1]} | {row[2]} | Due: {row[3]}")

    def add_task(self):
        task = self.task_entry.get()
        category = self.category_entry.get()
        due_date = self.due_date_entry.get()
        if task and category and due_date:
            with self.conn:
                self.conn.execute("INSERT INTO tasks (task, category, due_date) VALUES (?, ?, ?)", (task, category, due_date))
            self.load_tasks()
            self.task_entry.delete(0, tk.END)
            self.category_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please fill all fields.")

    def delete_task(self):
        selected_task = self.task_listbox.get(tk.ACTIVE)
        if selected_task:
            task_id = selected_task.split(":")[0]
            with self.conn:
                self.conn.execute("DELETE FROM tasks WHERE id=?", (task_id,))
            self.load_tasks()

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
