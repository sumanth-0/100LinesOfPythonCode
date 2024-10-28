import os
import random
from PIL import Image

def create_collage(image_folder, collage_width, collage_height, output_file):
    """Create a collage from images in the specified folder."""
    images = []
    
    # Load images from the specified folder
    for filename in os.listdir(image_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            img_path = os.path.join(image_folder, filename)
            images.append(Image.open(img_path))

    if not images:
        print("No images found in the specified folder.")
        return

    # Randomly shuffle images
    random.shuffle(images)

    # Create a blank canvas for the collage
    collage = Image.new('RGB', (collage_width, collage_height), (255, 255, 255))

    # Calculate the number of rows and columns for the collage
    cols = 4  # Number of columns
    rows = 3  # Number of rows

    # Calculate individual image width and height based on the collage dimensions
    img_width = collage_width // cols
    img_height = collage_height // rows

    img_index = 0
    for row in range(rows):
        for col in range(cols):
            if img_index < len(images):
                img = images[img_index]
                # Resize image to fit into the collage grid
                img = img.resize((img_width, img_height), Image.LANCZOS)
                x = col * img_width
                y = row * img_height
                collage.paste(img, (x, y))
                img_index += 1

    # Save the collage image
    collage.save(output_file)
    print(f"Collage created and saved as {output_file}")

def main():
    """Main function to run the collage creation program."""
    image_folder = input("Enter the path to your image folder (e.g., C:/pictures/whatever): ")
    output_file = input("Enter the output file name (e.g., collage.jpg): ")
    
    # Set desired collage dimensions
    collage_width = 800  # Set your desired width
    collage_height = 600  # Set your desired height
    
    # Check if the provided path is a valid directory
    if not os.path.isdir(image_folder):
        print(f"The directory '{image_folder}' does not exist. Please check the path and try again.")
        return

    create_collage(image_folder, collage_width, collage_height, output_file)

if __name__ == "__main__":
    main()
