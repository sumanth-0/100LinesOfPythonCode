import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import DateEntry
from plyer import notification
import threading
import time
from datetime import datetime

class EventReminderApp:
    def __init__(self, master):
        # Set up the main window
        self.master = master
        self.master.title("Event Reminder App")
        self.master.geometry("400x450")

        # Event name input
        self.event_label = tk.Label(master, text="Event Name:")
        self.event_label.pack(pady=5)
        self.event_entry = tk.Entry(master, width=50)
        self.event_entry.pack(pady=5)

        # Date selection
        self.date_label = tk.Label(master, text="Select Date:")
        self.date_label.pack(pady=5)
        self.date_entry = DateEntry(master, width=47, background='darkblue', foreground='white', borderwidth=2)
        self.date_entry.pack(pady=5)

        # Time selection
        self.time_label = tk.Label(master, text="Select Time:")
        self.time_label.pack(pady=5)
        time_frame = tk.Frame(master)
        time_frame.pack(pady=5)
        self.hour_spinbox = tk.Spinbox(time_frame, from_=1, to=12, width=5, format="%02.0f")
        self.hour_spinbox.pack(side=tk.LEFT, padx=2)
        self.minute_spinbox = tk.Spinbox(time_frame, from_=0, to=59, width=5, format="%02.0f")
        self.minute_spinbox.pack(side=tk.LEFT, padx=2)
        self.ampm_combobox = ttk.Combobox(time_frame, values=["AM", "PM"], width=5)
        self.ampm_combobox.set("AM")
        self.ampm_combobox.pack(side=tk.LEFT, padx=2)

        # Add reminder button
        self.add_button = tk.Button(master, text="Add Reminder", command=self.add_reminder)
        self.add_button.pack(pady=20)

        # List to store reminders
        self.reminders = []

    def add_reminder(self):
        # Gather input data
        event_name = self.event_entry.get()
        event_date = self.date_entry.get_date()
        event_hour = self.hour_spinbox.get()
        event_minute = self.minute_spinbox.get()
        event_ampm = self.ampm_combobox.get()

        if not event_name:
            messagebox.showwarning("Input Error", "Please enter event name.")
            return

        # Format event time
        event_time = f"{event_hour}:{event_minute} {event_ampm}"

        try:
            # Parse date and time
            event_datetime = datetime.strptime(f"{event_date} {event_time}", "%Y-%m-%d %I:%M %p")
        except ValueError:
            messagebox.showerror("Input Error", "Invalid time format.")
            return

        # Add reminder to list
        self.reminders.append((event_name, event_datetime))
        messagebox.showinfo("Reminder Added", f"Reminder for '{event_name}' on {event_datetime.strftime('%Y-%m-%d %I:%M %p')} added.")
        self.event_entry.delete(0, tk.END)

        # Start checking reminders
        threading.Thread(target=self.check_reminders).start()

    def check_reminders(self):
        while self.reminders:
            current_time = datetime.now()
            for event_name, event_datetime in self.reminders:
                if current_time >= event_datetime:
                    # Notify user
                    notification.notify(
                        title="Event Reminder",
                        message=f"It's time for: {event_name}",
                        timeout=10
                    )
                    self.reminders.remove((event_name, event_datetime))
            time.sleep(1)  # Check every second

def main():
    root = tk.Tk()
    app = EventReminderApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()