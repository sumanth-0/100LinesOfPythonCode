import tkinter as tk
import time
from tkinter import messagebox

running = False
start_time = 0
remaining = 0
is_work = True  # True = work session, False = break

def start():
    global running, start_time, remaining, is_work
    if not running:
        if remaining == 0:
            try:
                # Get minutes from the correct entry depending on work/break
                mins = int(work_entry.get() if is_work else break_entry.get())
                remaining = mins * 60
            except ValueError:
                messagebox.showerror("Error", "Enter valid minutes")
                return
        running = True
        start_time = time.time()
        update()  # Start updating the timer

def stop():
    global running, remaining
    if running:
        running = False
        # Adjust remaining time when stopped
        remaining -= time.time() - start_time

def reset():
    global running, remaining, is_work
    running = False
    remaining = 0
    is_work = True
    label.config(text="00:00")
    status_label.config(text="Work Time", fg="green")  # Reset status label

def update():
    global running, remaining, is_work
    if running:
        left = max(0, remaining - (time.time() - start_time))
        m, s = divmod(int(left), 60)  # Convert total seconds to minutes and seconds
        label.config(text=f"{m:02d}:{s:02d}")
        if left <= 0:
            running = False
            messagebox.showinfo("Done!", "Time for a break!" if is_work else "Back to work!")
            is_work = not is_work
            # Update label to show current phase
            status_label.config(text="Break Time" if not is_work else "Work Time",
                                fg="blue" if not is_work else "green")
            remaining = 0
            start()
            return
        root.after(100, update)  # Schedule next update in 100ms

# --- GUI ---
root = tk.Tk()
root.title("Pomodoro Timer")

# Work time entry
work_label = tk.Label(root, text="Enter work time in mins:", font=('Arial', 20))
work_label.grid(row=1, column=1)
work_entry = tk.Entry(root, width=20, justify='right', font=('Arial', 20))
work_entry.insert(0, "25")
work_entry.grid(row=1, column=2)

# Break time entry
break_label = tk.Label(root, text="Enter break time in mins:", font=('Arial', 20))
break_label.grid(row=2, column=1)
break_entry = tk.Entry(root, width=20, justify='right', font=('Arial', 20))
break_entry.insert(0, "5")
break_entry.grid(row=2, column=2)

# Show which Work/Break
status_label = tk.Label(root, text="Work Time", font=('Arial', 18), fg="green")
status_label.grid(row=3, column=1, columnspan=2, pady=5)

# Timer
label = tk.Label(root, text="00:00", font=("Arial", 50))
label.grid(row=4, column=1, rowspan=3)

# Start button
start_btn = tk.Button(root, text="Start", font=('Arial', 20), command=start)
start_btn.grid(row=4, column=2)

# Stop button
stop_btn = tk.Button(root, text="Stop", font=('Arial', 20), command=stop)
stop_btn.grid(row=5, column=2)

# Reset button
reset_btn = tk.Button(root, text="Reset", font=('Arial', 20), command=reset)
reset_btn.grid(row=6, column=2)

root.mainloop()
