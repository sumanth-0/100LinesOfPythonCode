import numpy as np
from PIL import Image
from pathlib import Path

def generate_radial_gradient(width, height, start_color, end_color, radius_factor=1.0):
    """
    Generate a radial gradient from the center to the edge.
    
    (args):
        - width(int) 
        - height(int)
        - start_color(tuple[int]) ex: "start_color=(255,0,0)"
        - end_color(tuple[int]) ex: "end_color=(0,255,0)"
        - orientation(str)
    return:
        image(PIL Image)
    
    """
    gradient = np.zeros((height, width, 3), dtype=np.uint8)
    center_x, center_y = width / 2, height / 2
    max_radius = np.sqrt(center_x**2 + center_y**2) * radius_factor

    for y in range(height):
        for x in range(width):
            dx, dy = x - center_x, y - center_y
            distance = np.sqrt(dx**2 + dy**2)
            ratio = min(distance / max_radius, 1.0)
            color = tuple(int(start + (end - start) * ratio) for start, end in zip(start_color, end_color))
            gradient[y, x, :] = color

    return Image.fromarray(gradient)

if __name__ == "__main__":
    width, height = 500, 500
    start_color = (255, 255, 0)  # jaune
    end_color = (255, 0, 0)      # rouge

    # Asking user to input radius
    try:
        radius_input = float(input("Please enter the radius for the radial gradient(0-1) : "))
        if not 0 < radius_input <= 1:
            print("Invalid value. Using default radius value '1.0'.")
            radius_input = 1.0
    except ValueError:
        print("Invalid input. Using default radius value '1.0'.")
        radius_input = 1.0

    img = generate_radial_gradient(width, height, start_color, end_color, radius_factor=radius_input)

    output_path = Path(__file__).parent / "images"
    output_path.mkdir(parents=True, exist_ok=True)
    img.save(output_path / "radial_gradient.png")
    print(f"Radial gradient saved to {output_path / 'images/radial_gradient.png'}")
