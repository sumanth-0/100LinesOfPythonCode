import os
import random
from PIL import Image

def create_collage(folder_path, collage_width=800, collage_height=600, output_filename="collage.jpg"):
    # Get all image files from the folder
    image_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith(('jpg', 'jpeg', 'png'))]
    
    # Create a blank canvas for the collage
    collage = Image.new("RGB", (collage_width, collage_height), (255, 255, 255))  # white background

    # Loop through each image file
    for img_file in image_files:
        img = Image.open(img_file)
        
        # Resize the image to a random smaller size (so it fits well)
        img.thumbnail((random.randint(100, 200), random.randint(100, 200)))
        
        # Pick a random position to paste the image
        x = random.randint(0, collage_width - img.width)
        y = random.randint(0, collage_height - img.height)
        
        # Paste the image onto the collage
        collage.paste(img, (x, y))

    # Save the final collage image
    collage.save(output_filename)
    print(f"Collage saved as '{output_filename}'")  # Feedback for user

# Run the function
folder_path = "path/to/your/folder"  # Replace with your folder path
create_collage(folder_path)
