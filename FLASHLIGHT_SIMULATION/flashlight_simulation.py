import tkinter as tk

class FlashlightApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Flashlight Simulation")
        self.canvas = tk.Canvas(master, width=800, height=600, bg="black")
        self.canvas.pack()
        self.radius = 100
        self.master.bind('<Motion>', self.move_flashlight)
        self.create_darkness()

    def create_darkness(self):
        self.canvas.create_rectangle(0, 0, 800, 600, fill='black', outline='')

    def move_flashlight(self, event):
        self.create_darkness()
        x = event.x
        y = event.y
        self.canvas.create_oval(x - self.radius, y - self.radius, x + self.radius, y + self.radius, fill='white', outline='')

def main():
    root = tk.Tk()
    app = FlashlightApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
