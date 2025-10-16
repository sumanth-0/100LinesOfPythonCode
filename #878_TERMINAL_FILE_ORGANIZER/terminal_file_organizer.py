import os
import shutil
from pathlib import Path

def organize_files(directory: str):
    """
    Organize files in the given directory into folders based on file extension.
    Example: .jpg -> Images/, .mp3 -> Music/, .pdf -> Documents/
    """
    # Convert to Path object
    base_path = Path(directory)

    if not base_path.exists():
        print(f"❌ Directory not found: {directory}")
        return

    # Define file type categories
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
        "Music": [".mp3", ".wav", ".aac", ".flac"],
        "Videos": [".mp4", ".mkv", ".mov", ".avi"],
        "Archives": [".zip", ".rar", ".tar", ".gz"],
        "Scripts": [".py", ".js", ".sh", ".bat"],
        "Others": []  # fallback category
    }

    # Create categorized folders if not existing
    for folder in file_types.keys():
        folder_path = base_path / folder
        folder_path.mkdir(exist_ok=True)

    # Go through each file in the directory
    for item in base_path.iterdir():
        if item.is_file():
            moved = False
            for folder, extensions in file_types.items():
                if item.suffix.lower() in extensions:
                    shutil.move(str(item), str(base_path / folder / item.name))
                    moved = True
                    break
            if not moved:
                shutil.move(str(item), str(base_path / "Others" / item.name))

    print("✅ Files have been organized successfully!")


def main():
    print("=== Terminal File Organizer ===")
    target_dir = input("Enter the directory path to organize: ").strip()
    organize_files(target_dir)


if __name__ == "__main__":
    main()
