from PIL import Image

class ImageResizerCropper:
    def __init__(self, file_path):
        self.image = Image.open(file_path)
    
    def resize_image(self, width, height):
        resized_image = self.image.resize((width, height))
        resized_image.show()
        return resized_image
    
    def crop_image(self, left, upper, right, lower):
        cropped_image = self.image.crop((left, upper, right, lower))
        cropped_image.show()
        return cropped_image

def main():
    file_path = input("Enter the path of the image file: ")
    tool = ImageResizerCropper(file_path)
    
    print("Choose an option: 1. Resize 2. Crop")
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == "1":
        width = int(input("Enter new width: "))
        height = int(input("Enter new height: "))
        resized_image = tool.resize_image(width, height)
        save_path = input("Enter path to save resized image (e.g., resized_image.jpg): ")
        resized_image.save(save_path)
        print("Image resized and saved successfully.")
        
    elif choice == "2":
        left = int(input("Enter left crop boundary: "))
        upper = int(input("Enter upper crop boundary: "))
        right = int(input("Enter right crop boundary: "))
        lower = int(input("Enter lower crop boundary: "))
        cropped_image = tool.crop_image(left, upper, right, lower)
        save_path = input("Enter path to save cropped image (e.g., cropped_image.jpg): ")
        cropped_image.save(save_path)
        print("Image cropped and saved successfully.")
    
    else:
        print("Invalid choice. Please restart the program.")

if __name__ == "__main__":
    main()
