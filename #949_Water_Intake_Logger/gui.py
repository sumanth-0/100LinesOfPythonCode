import tkinter as tk
from tkinter import ttk, messagebox
import logger

class WaterTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Water Intake Logger")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        self.create_widgets()
        self.update_display()

    # Creates all gui widgets
    def create_widgets(self):
        title = tk.Label(self.root, text="💧 Water Intake Logger", font=("Arial", 18, "bold"), pady=20)
        title.pack()

        # current Total Frame
        total_frame = tk.Frame(self.root, bg="#e3f2fd", pady=15)
        total_frame.pack(fill="x", padx=20, pady=10)
        tk.Label(total_frame, text="Today's Total:", font=("Arial", 12), bg="#e3f2fd").pack()
        self.total_label = tk.Label(total_frame, text="0 ml", font=("Arial", 24, "bold"), fg="#1976d2", bg="#e3f2fd")
        self.total_label.pack()

        # Goal Label
        self.goal_label = tk.Label(self.root, text="Goal: 2000 ml", font=("Arial", 10), fg="#666")
        self.goal_label.pack()

        # Progress Bar
        self.progress = ttk.Progressbar(self.root, length=300, mode='determinate')
        self.progress.pack(pady=10)
        self.progress_label = tk.Label(self.root, text="0%", font=("Arial", 10))
        self.progress_label.pack()

        # Quick add buttons frame
        button_frame = tk.Frame(self.root, pady=20)
        button_frame.pack()
        tk.Label(button_frame, text="Quick Add:", font=("Arial", 11, "bold")).grid(row=0, column=0, columnspan=3, pady=5)

        # 250ml button
        btn_250 = tk.Button(button_frame, text="250 ml", width=8, command=lambda: self.add_water(250), bg="#64b5f6", fg="white", font=("Arial", 10))
        btn_250.grid(row=1, column=0, padx=5)

        # 500ml button
        btn_500 = tk.Button(button_frame, text="500 ml", width=8, command=lambda: self.add_water(500), bg="#42a5f5", fg="white", font=("Arial", 10))
        btn_500.grid(row=1, column=1, padx=5)

        # 750ml button
        btn_750 = tk.Button(button_frame, text="750 ml", width=8, command=lambda: self.add_water(750), bg="#2196f3", fg="white", font=("Arial", 10))
        btn_750.grid(row=1, column=2, padx=5)
    
        # Settings Button
        btn_settings = tk.Button(self.root, text="⚙️ Change Goal", command=self.change_goal, bg="#757575", fg="white", pady=5)
        btn_settings.pack(pady=10)

        # Reset Button
        btn_reset = tk.Button(self.root, text="🔄 Reset Today", command=self.reset_today, bg="#d32f2f", fg="white", pady=5) 
        btn_reset.pack(pady=5)

    # add water and update display
    def add_water(self, amount):
        logger.add_water(amount)
        self.update_display()  
        self.check_reminder()  

    # updates all display elements with current data
    def update_display(self):
        stats = logger.get_stats()
        self.total_label.config(text=f"{stats['total']} ml")
        self.goal_label.config(text=f"Goal: {stats['goal']} ml")
        self.progress['value'] = stats['progress']
        self.progress_label.config(text=f"{stats['progress']}%")

    # check if reminder is needed & display it
    def check_reminder(self):

        if logger.needs_reminder():
            goal = logger.get_goal()
            total = logger.get_today_total()
            remaining = goal - total

            reminder_msg = f"💧💧💧 Drink more water! 💧💧💧\n\n"
            reminder_msg += f"You've had {total} ml today.\n"
            reminder_msg += f"Goal: {goal} ml\n"
            reminder_msg += f"Still need: {remaining} ml"

            messagebox.showinfo("Reminder", reminder_msg)

    # to change daily goal
    def change_goal(self):
        from tkinter import simpledialog
        
        current_goal = logger.get_goal()
        new_goal = simpledialog.askinteger("Change Goal", 
                                        f"Current goal: {current_goal} ml\n\nEnter new goal:",
                                        minvalue=500, maxvalue=10000)
        
        if new_goal:
            logger.set_goal(new_goal)
            self.update_display()
            messagebox.showinfo("Success", f"Goal updated to {new_goal} ml!")

    # resets water intake
    def reset_today(self):
        result = messagebox.askyesno("Reset Today", "Are you sure you want to reset today's intake?")
        if result:
            data = logger.load_data()
            today = logger.datetime.now().strftime("%Y-%m-%d")
            data["entries"] = [e for e in data["entries"] if e["date"] != today]
            logger.save_data(data)
            self.update_display()
            messagebox.showinfo("Reset", "Today's intake has been reset!")
