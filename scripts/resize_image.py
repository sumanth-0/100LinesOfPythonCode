# image_resizer.py
# Resize an image to the given width and height
# Usage: python image_resizer.py input.jpg output.jpg 300 300

from PIL import Image
import sys

def resize_image(input_path, output_path, width, height):
    img = Image.open(input_path)
    resized = img.resize((width, height))
    resized.save(output_path)
    print(f"Image resized successfully and saved as {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python image_resizer.py input.jpg output.jpg width height")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    width = int(sys.argv[3])
    height = int(sys.argv[4])

    resize_image(input_file, output_file, width, height)
