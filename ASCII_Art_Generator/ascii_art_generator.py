from PIL import Image

ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio * 0.55)  # Adjust for better aspect ratio in ASCII
    return image.resize((new_width, new_height))

def grayscale_image(image):
    return image.convert("L")

def image_to_ascii(image, width=100):
    image = resize_image(image, width)
    image = grayscale_image(image)
    pixels = image.getdata()
    ascii_str = ''.join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    
    ascii_art = [ascii_str[index: index + width] for index in range(0, len(ascii_str), width)]
    return "\n".join(ascii_art)

def save_ascii_art(ascii_art, file_name="ascii_art.txt"):
    with open(file_name, "w") as file:
        file.write(ascii_art)

# Example usage
image_path = "input_image.jpg"
output_path = "output_ascii_art.txt"
image = Image.open(image_path)
ascii_art = image_to_ascii(image)
save_ascii_art(ascii_art, output_path)
