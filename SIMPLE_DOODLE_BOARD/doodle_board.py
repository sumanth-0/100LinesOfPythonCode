import tkinter as tk
from tkinter import colorchooser

class DoodleBoard:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Doodle Board")

        self.canvas = tk.Canvas(master, bg="white", width=800, height=600)
        self.canvas.pack()

        self.last_x, self.last_y = None, None
        self.color = "black"
        self.brush_size = 5

        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

        self.color_button = tk.Button(master, text="Choose Color", command=self.choose_color)
        self.color_button.pack(side=tk.LEFT)

        self.brush_size_label = tk.Label(master, text="Brush Size:")
        self.brush_size_label.pack(side=tk.LEFT)

        self.brush_size_entry = tk.Entry(master, width=5)
        self.brush_size_entry.pack(side=tk.LEFT)
        self.brush_size_entry.insert(0, "5")

    def draw(self, event):
        if self.last_x and self.last_y:
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y, fill=self.color, width=self.brush_size)
        self.last_x, self.last_y = event.x, event.y

    def reset(self, event):
        self.last_x, self.last_y = None, None
        self.brush_size = int(self.brush_size_entry.get())

    def choose_color(self):
        self.color = colorchooser.askcolor()[1]

def main():
    root = tk.Tk()
    doodle_board = DoodleBoard(root)
    root.mainloop()

if __name__ == "__main__":
    main()
