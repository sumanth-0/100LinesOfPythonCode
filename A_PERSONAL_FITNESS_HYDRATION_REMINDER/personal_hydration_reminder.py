import time
import datetime
import tkinter as tk
from threading import Timer

class HydrationReminder:
    def __init__(self, root):
        self.root = root
        self.root.title("Hydration Reminder")
        
        self.last_drink_time = None
        self.timer_interval = 3600  # Reminder every hour in seconds
        self.notification_label = tk.Label(root, text="", font=("Arial", 12))
        self.notification_label.pack(pady=20)

        self.update_reminder()
        
    def record_drink(self):
        self.last_drink_time = datetime.datetime.now()
        self.notification_label.config(text="Recorded: You drank water!")
        self.update_reminder()
    
    def update_reminder(self):
        current_time = datetime.datetime.now()
        if self.last_drink_time:
            elapsed_time = (current_time - self.last_drink_time).total_seconds()
            if elapsed_time >= self.timer_interval:
                self.notification_label.config(text="Reminder: Time to drink water!")
            else:
                next_reminder_in = self.timer_interval - elapsed_time
                Timer(next_reminder_in, self.update_reminder).start()
        else:
            self.notification_label.config(text="Reminder: Time to drink water!")
            Timer(self.timer_interval, self.update_reminder).start()
    
    def setup_ui(self):
        tk.Button(self.root, text="I drank water", command=self.record_drink, font=("Arial", 10)).pack(pady=10)
        tk.Button(self.root, text="Exit", command=self.root.quit, font=("Arial", 10)).pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = HydrationReminder(root)
    app.setup_ui()
    root.mainloop()
