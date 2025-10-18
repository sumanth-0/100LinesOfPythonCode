from PIL import Image
import random
import os

# --- Configuration ---
WIDTH = 100
HEIGHT = 100
FILENAME = "random_pixel_pattern.png"

def generate_random_pixel_art(width, height):
    """Generates a random pixel pattern and saves it as a PNG image."""
    print(f"Generating a {width}x{height} image...")
    
    # 1. Create a new image canvas in RGB mode
    # The image is initially black
    img = Image.new('RGB', (width, height), 'black')
    
    # 2. Load the image's pixel data for manipulation
    pixels = img.load()
    
    # 3. Iterate over every single pixel (x is column, y is row)
    for x in range(width):
        for y in range(height):
            # 4. Generate a random color (RGB tuple)
            # Each color component (Red, Green, Blue) is a random integer from 0 to 255
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            
            # 5. Set the pixel color
            pixels[x, y] = (r, g, b)
            
    # Save the file
    img.save(FILENAME)
    print(f"Image successfully saved as '{FILENAME}'")

if __name__ == "__main__":
    # Ensure the script runs from the repository root for clean saving
    if not os.path.exists('PIXEL_ART'):
        os.makedirs('PIXEL_ART')
        
    # Change directory so the image saves cleanly inside the folder
    os.chdir('PIXEL_ART')
    
    generate_random_pixel_art(WIDTH, HEIGHT)
    
    # Optional: Go back to the root directory
    os.chdir('..')