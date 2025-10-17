import numpy as np
from PIL import Image

# --- 1. CONFIGURATION ---
WIDTH = 256  # Image width in pixels
HEIGHT = 256 # Image height in pixels
MAX_ITER = 100 # Maximum number of iterations for the fractal formula
# Defines the area of the complex plane to zoom into (Mandelbrot standard view)
X_MIN, X_MAX = -2.0, 1.0
Y_MIN, Y_MAX = -1.5, 1.5

# --- 2. FRACTAL GENERATION FUNCTION ---
def mandelbrot(c):
    """
    Calculates the number of iterations before the sequence z = z^2 + c diverges.
    """
    z = 0
    n = 0
    while abs(z) <= 2 and n < MAX_ITER:
        z = z*z + c
        n += 1
    return n

# --- 3. MAIN SCRIPT ---
def generate_and_save_fractal():
    # Create an empty numpy array to store the iteration counts for each pixel
    image_data = np.zeros((HEIGHT, WIDTH), dtype=np.uint8)

    # 3.1 Map pixels to complex plane and calculate value
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Map pixel coordinates (x, y) to the complex plane (real, imag)
            real = X_MIN + (x / WIDTH) * (X_MAX - X_MIN)
            imag = Y_MIN + (y / HEIGHT) * (Y_MAX - Y_MIN)
            c = complex(real, imag)

            # Calculate the Mandelbrot value
            color_value = mandelbrot(c)

            # Store the result, scaling the iteration count (0 to 100) to a
            # grayscale value (0 to 255). We use a square root for better contrast.
            image_data[y, x] = int(np.sqrt(color_value / MAX_ITER) * 255)

    # 3.2 Create and save the image using Pillow
    
    # Convert the numpy array to a Pillow Image object (grayscale 'L' mode)
    img = Image.fromarray(image_data, 'L')
    
    # Convert to a color mode (like 'RGB') for better visuals, if desired.
    # We use a simple color map here for a classic look.
    # Note: For simplicity, the coloring remains grayscale-like for the "small fractal" request.
    
    # Save the image as a PNG file
    file_name = "small_mandelbrot_fractal.png"
    img.save(file_name, "PNG")

    print(f"✅ Success! Fractal image saved as {file_name} with size {WIDTH}x{HEIGHT} pixels.")

if __name__ == "__main__":
    generate_and_save_fractal()