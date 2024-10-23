import tkinter as tk
import time
import threading

class MoodLight:
    def __init__(self, master):
        self.master = master
        self.master.title("Mood Light Simulation")
        self.master.geometry("400x400")
        
        self.colors = ["#FFDDC1", "#FFABAB", "#FFC3A0", "#FF677D", "#D4A5A5", "#392F5A", "#1F3C88", "#61C0BF", "#6B4226"]
        self.index = 0
        self.running = True

        self.label = tk.Label(master, text="Mood Light Simulation", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.start_button = tk.Button(master, text="Start Mood Light", command=self.start_light)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(master, text="Stop Mood Light", command=self.stop_light)
        self.stop_button.pack(pady=10)

    def start_light(self):
        self.running = True
        threading.Thread(target=self.change_color).start()

    def stop_light(self):
        self.running = False

    def change_color(self):
        while self.running:
            # Change the background color of the window
            self.master.configure(bg=self.colors[self.index])
            self.index = (self.index + 1) % len(self.colors)
            time.sleep(1)  # Adjust the speed of color change here

def main():
    root = tk.Tk()
    mood_light = MoodLight(root)
    root.mainloop()

if __name__ == "__main__":
    main()
