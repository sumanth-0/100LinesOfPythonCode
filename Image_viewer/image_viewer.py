import tkinter as tk
from PIL import ImageTk, Image

class ImageViewer:
    def __init__(self, images):
        self.root = tk.Tk()
        self.root.title("Image Viewer")

        self.images = images
        self.current_image_index = 0

        self.image_label = tk.Label(self.root)
        self.image_label.pack()

        self.prev_button = tk.Button(self.root, text="Previous", command=self.prev_image)
        self.prev_button.pack(side=tk.LEFT)

        self.next_button = tk.Button(self.root, text="Next", command=self.next_image)
        self.next_button.pack(side=tk.RIGHT)

        self.display_image()

    def display_image(self):
        image = Image.open(self.images[self.current_image_index])
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.image = photo  # Keep a reference to avoid garbage collection

    def prev_image(self):
        self.current_image_index = (self.current_image_index - 1) % len(self.images)
        self.display_image()

    def next_image(self):
        self.current_image_index = (self.current_image_index + 1) % len(self.images)
        self.display_image()

    def run(self):
        self.root.mainloop()

# Example usage:
image_files = ["image1.jpg", "image2.jpg", "image3.jpg"]  # Replace with your image paths
viewer = ImageViewer(image_files)
viewer.run()
