import tkinter as tk

class MoodRingSimulator:
    def __init__(self, master):
        self.master = master
        self.master.title("Mood Ring Simulator")
        self.master.geometry("300x200")
        
        self.label = tk.Label(master, text="Enter your mood:", font=("Helvetica", 14))
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(master)
        self.entry.pack(pady=10)

        self.button = tk.Button(master, text="Get Mood Color", command=self.update_color)
        self.button.pack(pady=10)
        
        self.color_display = tk.Canvas(master, width=100, height=100)
        self.color_display.pack(pady=10)

    def update_color(self):
        mood = self.entry.get().lower()
        color = self.get_color(mood)
        self.color_display.config(bg=color)

    def get_color(self, mood):
        mood_colors = {
            'happy': 'yellow',
            'sad': 'blue',
            'angry': 'red',
            'calm': 'green',
            'excited': 'orange',
            'bored': 'grey',
            'confused': 'purple'
        }
        return mood_colors.get(mood, 'white')  # Default to white if mood not recognized

def main():
    root = tk.Tk()
    app = MoodRingSimulator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
