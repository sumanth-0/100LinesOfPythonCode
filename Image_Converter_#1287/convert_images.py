"""
A Python utility script to convert all PNG files in a folder to JPEG, or
all JPEG files to PNG.

This script uses the Pillow (PIL) library for image processing.

Features:
- Converts all images in a folder between PNG and JPEG formats.
- Maintains original file names (only changes extensions).
- Handles errors gracefully (e.g., invalid image files or missing folder).
- Creates an output subfolder named 'converted' to avoid overwriting originals.

Usage:
    python convert_images.py
"""

import os
from PIL import Image

def convert_images(folder_path: str, target_format: str) -> None:
    """
    Convert all PNG files in a folder to JPEG or vice versa.

    Args:
        folder_path (str): The path to the folder containing images.
        target_format (str): The desired format, either 'jpeg' or 'png'.

    Returns:
        None
    """
    # Validate input format
    if target_format.lower() not in ("jpeg", "png"):
        print("Error: target_format must be 'jpeg' or 'png'")
        return

    # Create output directory
    output_dir = os.path.join(folder_path, "converted")
    os.makedirs(output_dir, exist_ok=True)

    # Determine source and target extensions
    src_ext = ".png" if target_format.lower() == "jpeg" else ".jpg"
    alt_src_ext = ".jpeg" if target_format.lower() == "png" else ".png"

    converted_count = 0

    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip subdirectories
        if not os.path.isfile(file_path):
            continue

        # Convert based on file extension
        if filename.lower().endswith((src_ext, alt_src_ext)):
            try:
                img = Image.open(file_path).convert("RGB")  # Convert to RGB mode
                new_filename = os.path.splitext(filename)[0] + f".{target_format.lower()}"
                save_path = os.path.join(output_dir, new_filename)
                img.save(save_path, target_format.upper())
                converted_count += 1
                print(f"Converted: {filename} → {new_filename}")
            except Exception as e:
                print(f"Skipped {filename}: {e}")

    if converted_count == 0:
        print("\nNo matching image files found for conversion.")
    else:
        print(f"\n Conversion complete! {converted_count} files saved to '{output_dir}'.")

if __name__ == "__main__":
    # Get user inputs
    folder = input("Enter the folder path containing images: ").strip()
    target = input("Enter target format ('jpeg' or 'png'): ").strip().lower()

    if not os.path.isdir(folder):
        print(" Error: The specified folder does not exist.")
    else:
        convert_images(folder, target)
