import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class OpticalIllusionViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Optical Illusion Viewer")

        # List of optical illusions (add paths to images)
        self.illusions = [
            {"image": "illusion1.jpg", "description": "An optical illusion that tricks your brain."},
            {"image": "illusion2.jpg", "description": "Can you see the hidden images?"},
            {"image": "illusion3.jpg", "description": "A classic spiraling illusion."},
        ]

        self.current_illusion = 0
        self.display_illusion()

        self.info_button = tk.Button(root, text="Info", command=self.show_info)
        self.info_button.pack()

        self.next_button = tk.Button(root, text="Next", command=self.next_illusion)
        self.next_button.pack()

    def display_illusion(self):
        illusion_data = self.illusions[self.current_illusion]
        img = Image.open(illusion_data["image"])
        img = img.resize((400, 400))
        self.photo = ImageTk.PhotoImage(img)

        if hasattr(self, 'illusion_label'):
            self.illusion_label.destroy()
        self.illusion_label = tk.Label(self.root, image=self.photo)
        self.illusion_label.image = self.photo
        self.illusion_label.pack()

    def show_info(self):
        illusion_data = self.illusions[self.current_illusion]
        messagebox.showinfo("Optical Illusion Info", illusion_data["description"])

    def next_illusion(self):
        self.current_illusion = (self.current_illusion + 1) % len(self.illusions)
        self.display_illusion()

def main():
    root = tk.Tk()
    viewer = OpticalIllusionViewer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
