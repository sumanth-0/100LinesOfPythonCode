
# Basic Image Comparison Tool

from PIL import Image, ImageChops
import matplotlib.pyplot as plt

def compare_images(image1_path, image2_path):
    img1 = Image.open(image1_path)
    img2 = Image.open(image2_path)

    # Check if images are the same size
    if img1.size != img2.size:
        print("Images must be the same size for comparison.")
        return

    # Calculate the difference
    diff = ImageChops.difference(img1, img2)

    if diff.getbbox() is None:
        print("Images are identical.")
    else:
        print("Images are different.")
    
    return img1, img2, diff

def main():
    # Example image paths
    image1_path = input("Enter the path for the first image: ")
    image2_path = input("Enter the path for the second image: ")

    img1, img2, diff = compare_images(image1_path, image2_path)

    # Display images
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 3, 1)
    plt.imshow(img1)
    plt.title("Image 1")
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(img2)
    plt.title("Image 2")
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(diff)
    plt.title("Difference")
    plt.axis('off')

    plt.show()

if __name__ == "__main__":
    main()
