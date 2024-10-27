from PIL import Image, ImageOps
import sys

def apply_black_and_white(image):
    return image.convert("L")

def apply_sepia(image):
    width, height = image.size
    sepia_image = Image.new("RGB", (width, height))
    
    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            tr = int(0.393 * r + 0.769 * g + 0.189 * b)
            tg = int(0.349 * r + 0.686 * g + 0.168 * b)
            tb = int(0.272 * r + 0.534 * g + 0.131 * b)
            sepia_image.putpixel((x, y), (min(tr, 255), min(tg, 255), min(tb, 255)))

    return sepia_image

def apply_invert(image):
    return ImageOps.invert(image)

def main():
    print("Image Filter Application")
    image_path = input("Enter the path to the image: ")
    
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Error opening image: {e}")
        sys.exit(1)

    print("Choose a filter to apply:")
    print("1. Black and White")
    print("2. Sepia")
    print("3. Invert Colors")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        filtered_image = apply_black_and_white(image)
        output_path = "filtered_image_bw.jpg"
    elif choice == '2':
        filtered_image = apply_sepia(image)
        output_path = "filtered_image_sepia.jpg"
    elif choice == '3':
        filtered_image = apply_invert(image)
        output_path = "filtered_image_invert.jpg"
    else:
        print("Invalid choice!")
        sys.exit(1)

    filtered_image.save(output_path)
    print(f"Filtered image saved as {output_path}")

if __name__ == "__main__":
    main()
