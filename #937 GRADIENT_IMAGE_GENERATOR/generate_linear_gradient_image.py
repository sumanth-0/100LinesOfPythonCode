import numpy as np
from PIL import Image
from pathlib import Path

def generate_linear_gradient(width, height, start_color, end_color, orientation='vertical'):
    """
    This function generate a linear gradient on vertical or horizontal orientation
    
    (args):
        - width(int) 
        - height(int)
        - start_color(tuple[int]) ex: "start_color=(255,0,0)"
        - end_color(tuple[int]) ex: "end_color=(0,255,0)"
        - orientation(str)
    return:
        image(PIL image)
    
    """
    gradient = np.zeros((height, width, 3), dtype=np.uint8)
    if orientation == 'vertical':
        for i in range(height):
            ratio = i / (height - 1)
            color = tuple(int(start + (end - start) * ratio) for start, end in zip(start_color, end_color))
            gradient[i, :, :] = color
    elif orientation == 'horizontal':
        for i in range(width):
            ratio = i / (width - 1)
            color = tuple(int(start + (end - start) * ratio) for start, end in zip(start_color, end_color))
            gradient[:, i, :] = color
    else:
        raise ValueError("Orientation must be 'vertical' or 'horizontal'.")
    return Image.fromarray(gradient)

if __name__ == "__main__":
    width, height = 500, 300
    start_color = (255, 0, 0)  # red
    end_color = (0, 0, 255)    # blue

    # Asking user for orientation
    orientation_input = input("Enter the orientation of the gradient (horizontal/vertical) : ").strip().lower()
    if orientation_input not in ['vertical', 'horizontal']:
        print("Invalid Orientation. Using 'vertical' orientation by default.")
        orientation_input = 'vertical'

    img = generate_linear_gradient(width, height, start_color, end_color, orientation=orientation_input)

    output_path = Path(__file__).parent / "images"
    output_path.mkdir(parents=True, exist_ok=True)
    img.save(output_path / "linear_gradient.png")
    print(f"Linear gradient saved to {output_path / 'linear_gradient.png'}")
