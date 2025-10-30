"""
This script automatically organizes files in the user's Downloads folder
by moving them into categorized subfolders based on file type.

Example:
    A file named 'photo.jpg' will be moved to the 'Images' folder.
    A file named 'report.pdf' will be moved to the 'Documents' folder.

Supported categories:
    - Images
    - Documents
    - Videos
    - Music
    - Archives
    - Applications
    - Others
"""

import os
import shutil
from pathlib import Path

def organize_downloads(downloads_path: str) -> None:
    """
    Organize files in the specified Downloads folder by file type.

    Args:
        downloads_path (str): The path to the user's Downloads folder.

    Returns:
        None
    """
    # Define file categories and their associated extensions
    categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg"],
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx", ".csv"],
        "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv"],
        "Music": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"],
        "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
        "Applications": [".exe", ".msi", ".dmg", ".pkg", ".app"],
    }

    # Convert path string to Path object for easier handling
    downloads_dir = Path(downloads_path)

    # Validate that the provided path is a directory
    if not downloads_dir.is_dir():
        print(f"Error: '{downloads_path}' is not a valid directory.")
        return

    # List all files in the Downloads folder (ignore subfolders)
    files = [f for f in downloads_dir.iterdir() if f.is_file()]

    if not files:
        print("No files found in the Downloads folder.")
        return

    # Iterate over files and move them into categorized folders
    for file_path in files:
        file_extension = file_path.suffix.lower()  # e.g., '.jpg'
        destination_folder = None

        # Determine which category the file belongs to
        for category, extensions in categories.items():
            if file_extension in extensions:
                destination_folder = downloads_dir / category
                break

        # If no matching category, move to "Others"
        if not destination_folder:
            destination_folder = downloads_dir / "Others"

        # Create the destination folder if it doesn't exist
        destination_folder.mkdir(exist_ok=True)

        # Construct the new file path
        destination_path = destination_folder / file_path.name

        try:
            # Move the file to the categorized folder
            shutil.move(str(file_path), str(destination_path))
            print(f"Moved: {file_path.name} → {destination_folder.name}/")
        except Exception as e:
            print(f"Error moving {file_path.name}: {e}")

    print("\n Downloads folder organized successfully!")


if __name__ == "__main__":
    # Default path to the user's Downloads folder
    user_downloads = str(Path.home() / "Downloads")

    print("Automatic Downloads Organizer")
    print(f"Target folder: {user_downloads}\n")

    # Run the organizer function
    organize_downloads(user_downloads)
