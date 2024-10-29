
# Import necessary libraries
from PIL import Image, ImageChops
import matplotlib.pyplot as plt

# Function to compare two images
def compare_images(image1_path, image2_path):
    # Open images
    img1 = Image.open(image1_path)
    img2 = Image.open(image2_path)

    # Calculate the difference
    diff = ImageChops.difference(img1, img2)

    # Show images and the difference
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 3, 1)
    plt.title("Image 1")
    plt.imshow(img1)
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.title("Image 2")
    plt.imshow(img2)
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.title("Difference")
    plt.imshow(diff)
    plt.axis('off')

    plt.show()

# User input for image paths
if __name__ == "__main__":
    image1_path = input("Enter the path for the first image: ")
    image2_path = input("Enter the path for the second image: ")
    compare_images(image1_path, image2_path)
