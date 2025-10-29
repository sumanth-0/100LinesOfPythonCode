import os
import glob
from PIL import Image

def images_to_pdf(folder_path, output_pdf="Merged_Images.pdf"):
    """Convert all images in a given folder into a single PDF."""
    # Check if folder exists
    if not os.path.exists(folder_path):
        print("❌ Folder not found. Please check the path and try again.")
        return
    
    # Get all supported image files
    supported_exts = ('*.png', '*.jpg', '*.jpeg', '*.bmp', '*.webp')
    image_files = []
    for ext in supported_exts:
        image_files.extend(glob.glob(os.path.join(folder_path, ext)))
    
    # Sort files alphabetically (optional)
    image_files.sort()
    
    if not image_files:
        print("⚠️ No image files found in this folder.")
        return
    
    print(f"Found {len(image_files)} image(s). Creating PDF...")
    
    # Open and convert all images to RGB
    images = [Image.open(img).convert("RGB") for img in image_files]
    
    # Save all images into one PDF
    output_path = os.path.join(folder_path, output_pdf)
    images[0].save(output_path, save_all=True, append_images=images[1:])
    
    print(f"✅ PDF created successfully: {output_path}")

def main():
    print("=== Image to PDF Converter ===")
    folder_path = input("📁 Enter the folder path containing your images: ").strip('" ')
    images_to_pdf(folder_path)

if __name__ == "__main__":
    main()
