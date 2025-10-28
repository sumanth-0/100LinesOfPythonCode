import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageFont, ImageDraw
import os

# Function to add watermark
def add_watermark(image_path, watermark_text, color):
    try:
        if not os.path.isfile(image_path):
            messagebox.showerror("Error", "File not found! Please select a valid image.")
            return

        # Open image and prepare overlay
        image = Image.open(image_path).convert("RGBA")
        width, height = image.size
        overlay = Image.new("RGBA", image.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(overlay)

        font_size = min(width, height) // 10
        try:
            font = ImageFont.truetype("arial.ttf", font_size)
        except:
            font = ImageFont.load_default()

        # Draw text at the center (semi-transparent)
        x, y = width // 2, height // 2
        draw.text((x, y), watermark_text, fill=(*color, 128), font=font, anchor="mm")

        # Merge overlay with original image
        result = Image.alpha_composite(image, overlay).convert("RGB")

        # Save the new image
        save_path = os.path.join(os.path.dirname(image_path), "watermarked_image.jpg")
        result.save(save_path)
        result.show()
        messagebox.showinfo("Success", f"Watermarked image saved to:\n{save_path}")
        
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to select an image file
def select_image(entry_box):
    path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if not path:
        messagebox.showwarning("Warning", "No file selected.")
        return
    entry_box.delete(0, tk.END)
    entry_box.insert(0, path)

# Function to take the image_path and watermark_text and add the watermark
def apply_watermark(path_entry, text_entry, color_option):
    image_path = path_entry.get().strip()
    watermark_text = text_entry.get().strip()

    if not image_path:
        messagebox.showwarning("Warning", "Please select an image first.")
        return
    if not watermark_text:
        messagebox.showwarning("Warning", "Please enter watermark text.")
        return

    # Color (black or white)
    color = (0, 0, 0) if color_option.get() == "Black" else (255, 255, 255)
    
    add_watermark(image_path, watermark_text, color)

# ------------------ GUI SETUP ------------------

root = tk.Tk()
root.title("Simple Image Watermarker")
root.geometry("450x200")

# Image path
tk.Label(root, text="Image:").grid(row=0, column=0, padx=10, pady=5)
path_entry = tk.Entry(root, width=40)
path_entry.grid(row=0, column=1)
tk.Button(root, text="Select", command=lambda: select_image(path_entry)).grid(row=0, column=2, padx=5)

# Watermark text 
tk.Label(root, text="Watermark text:").grid(row=1, column=0, padx=10, pady=5)
text_entry = tk.Entry(root, width=40)
text_entry.grid(row=1, column=1)

# Color option
tk.Label(root, text="Color:").grid(row=2, column=0, padx=10, pady=5)
color_choice = tk.StringVar(value="Black")
tk.OptionMenu(root, color_choice, "Black", "White").grid(row=2, column=1, sticky="w")

# Insert watermark button
tk.Button(root, text="Insert Watermark", 
          command=lambda: apply_watermark(path_entry, text_entry, color_choice)).grid(row=3, column=1, pady=10)

# Close button
tk.Button(root, text="Close", command=root.destroy).grid(row=3, column=2)

root.mainloop()
