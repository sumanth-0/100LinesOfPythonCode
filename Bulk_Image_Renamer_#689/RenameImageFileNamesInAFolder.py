"""
This script renames all image files in a specified folder sequentially 
with a user-defined prefix. The renamed files will follow the format:

    <prefix>_1.<ext>, <prefix>_2.<ext>, <prefix>_3.<ext>, ...

For example, if the prefix is 'photo' and the folder contains:
    imgA.jpg, imgB.png, imgC.jpeg

After running the script, the files will be renamed as:
    photo_1.jpg, photo_2.png, photo_3.jpeg

Supported image extensions: .jpg, .jpeg, .png, .gif, .bmp, .tiff
"""

import os

def rename_images_in_folder(folder_path: str, prefix: str) -> None:
    """
    Rename all image files in a given folder sequentially with a user-defined prefix.

    Args:
        folder_path (str): The path to the folder containing the images.
        prefix (str): The prefix to use for renamed images.

    Returns:
        None
    """
    # Supported image file extensions
    image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff')

    # Validate folder path
    if not os.path.isdir(folder_path):
        print(f"Error: '{folder_path}' is not a valid directory.")
        return

    # Get a list of image files in the folder
    images = [f for f in os.listdir(folder_path) if f.lower().endswith(image_extensions)]
    images.sort()  # Sort alphabetically for consistent renaming order

    if not images:
        print("No image files found in the specified folder.")
        return

    # Rename images sequentially
    for index, filename in enumerate(images, start=1):
        old_path = os.path.join(folder_path, filename)
        extension = os.path.splitext(filename)[1]
        new_filename = f"{prefix}_{index}{extension}"
        new_path = os.path.join(folder_path, new_filename)

        try:
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} → {new_filename}")
        except Exception as e:
            print(f"Error renaming {filename}: {e}")

    print("\nRenaming completed successfully!")


if __name__ == "__main__":
    # Example usage: User provides folder path and prefix
    folder = input("Enter the folder path containing images: ").strip()
    prefix = input("Enter the prefix for renamed images: ").strip()
    rename_images_in_folder(folder, prefix)
