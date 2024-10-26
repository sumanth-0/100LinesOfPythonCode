import tkinter as tk
import time

class BinaryClock(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Binary Clock")
        self.configure(bg="black")
        self.time_label = tk.Label(self, font=("Helvetica", 48), bg="black", fg="white")
        self.time_label.pack(pady=20)
        self.update_time()

    def update_time(self):
        current_time = time.localtime()
        hours = format(current_time.tm_hour, '06b')
        minutes = format(current_time.tm_min, '06b')
        seconds = format(current_time.tm_sec, '06b')
        binary_time = f"{hours} : {minutes} : {seconds}"
        self.time_label.config(text=binary_time)
        self.after(1000, self.update_time)

if __name__ == "__main__":
    clock = BinaryClock()
    clock.mainloop()
