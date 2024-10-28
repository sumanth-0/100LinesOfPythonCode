import cv2
from PIL import Image

# ASCII characters used for mapping grayscale values
ASCII_CHARS = "@%#*+=-:. "

# Resize image based on desired width
def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width)
    return image.resize((new_width, new_height))

# Convert each pixel to grayscale
def grayscale(image):
    return image.convert("L")

# Map grayscale pixel values to ASCII characters
def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = "".join([ASCII_CHARS[min(9, pixel * len(ASCII_CHARS) // 256)] for pixel in pixels])
    return ascii_str

# Format ASCII string into multiple lines based on image width
def image_to_ascii(image, new_width=100):
    image = resize_image(image, new_width)
    image = grayscale(image)
    
    ascii_str = pixels_to_ascii(image)
    ascii_img = "\n".join([ascii_str[i:i+new_width] for i in range(0, len(ascii_str), new_width)])
    
    return ascii_img

# Capture image from webcam and convert to ASCII
def capture_and_convert():
    # Initialize the webcam
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Could not open webcam")
        return

    # Read a frame from the webcam
    ret, frame = cap.read()
    
    # Release the webcam
    cap.release()
    
    if not ret:
        print("Failed to capture image")
        return

    # Convert the image from BGR to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Convert to PIL Image
    pil_image = Image.fromarray(frame_rgb)
    
    # Convert to ASCII
    ascii_art = image_to_ascii(pil_image)
    
    # Print the ASCII art
    print(ascii_art)

# Run the capture and convert function
capture_and_convert()
