
from PIL import Image, ImageDraw, ImageFont
import tkinter as tk
from tkinter import filedialog, colorchooser, messagebox

class QuotePosterMaker:
    def __init__(self, root):
        self.root = root
        self.root.title("Quote Poster Maker")

        self.quote_text = tk.StringVar()
        self.font_color = "black"
        self.image_path = None

        tk.Label(root, text="Enter Quote:").pack(pady=5)
        tk.Entry(root, textvariable=self.quote_text, width=50).pack(pady=5)

        tk.Button(root, text="Choose Background Image", command=self.load_image).pack(pady=5)
        tk.Button(root, text="Choose Font Color", command=self.choose_color).pack(pady=5)
        tk.Button(root, text="Generate Poster", command=self.generate_poster).pack(pady=5)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=5)

    def load_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if self.image_path:
            self.result_label.config(text="Background image loaded.")

    def choose_color(self):
        self.font_color = colorchooser.askcolor()[1]

    def generate_poster(self):
        if not self.image_path or not self.quote_text.get():
            messagebox.showerror("Input Error", "Please load an image and enter a quote.")
            return

        img = Image.open(self.image_path).convert("RGBA")
        draw = ImageDraw.Draw(img)

        try:
            font = ImageFont.truetype("arial.ttf", 40)
        except IOError:
            font = ImageFont.load_default()

        width, height = img.size
        text = self.quote_text.get()
        text_width, text_height = draw.textsize(text, font=font)
        text_position = ((width - text_width) // 2, (height - text_height) // 2)

        draw.text(text_position, text, fill=self.font_color, font=font)
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        
        if save_path:
            img.save(save_path)
            messagebox.showinfo("Success", f"Poster saved to {save_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuotePosterMaker(root)
    root.mainloop()
