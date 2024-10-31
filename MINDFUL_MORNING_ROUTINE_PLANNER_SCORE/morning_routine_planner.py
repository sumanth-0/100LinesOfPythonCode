
import tkinter as tk
from tkinter import ttk
import time
import threading

class MorningRoutinePlanner:
    def __init__(self, root):
        self.root = root
        self.root.title("Mindful Morning Routine Planner")
        self.activities = [("Meditate", 5), ("Exercise", 10), ("Journal", 5)]
        self.create_gui()
    
    def create_gui(self):
        self.timer_label = tk.Label(self.root, text="Activity Timer: -", font=("Arial", 14))
        self.timer_label.grid(row=0, column=0, columnspan=2, pady=10)

        for i, (activity, duration) in enumerate(self.activities):
            tk.Label(self.root, text=f"{activity} ({duration} mins)").grid(row=i+1, column=0, sticky="w", padx=10)
            start_button = tk.Button(self.root, text="Start", command=lambda d=duration: self.start_timer(d))
            start_button.grid(row=i+1, column=1, padx=5)

    def start_timer(self, minutes):
        self.timer_label.config(text=f"Activity Timer: {minutes} mins remaining")
        for i in range(minutes * 60, -1, -1):
            mins, secs = divmod(i, 60)
            self.timer_label.config(text=f"Activity Timer: {mins:02d}:{secs:02d}")
            time.sleep(1)
            self.root.update()

if __name__ == "__main__":
    root = tk.Tk()
    app = MorningRoutinePlanner(root)
    root.mainloop()
