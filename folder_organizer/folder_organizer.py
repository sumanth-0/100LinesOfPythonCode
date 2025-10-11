#!/usr/bin/env python3
"""
Folder Organizer - Automatically organize files into folders by extension
Author: Folder Organizer
Description: Sorts and moves files into subfolders based on their file extensions
"""

import os
import shutil
from pathlib import Path

# Define file type categories and their extensions
FILE_CATEGORIES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.ico', '.webp'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.xls', '.xlsx', '.ppt', '.pptx'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm'],
    'Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz'],
    'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.h', '.php', '.rb', '.go'],
    'Executables': ['.exe', '.dmg', '.app', '.deb', '.rpm', '.msi'],
    'Data': ['.json', '.xml', '.csv', '.sql', '.db', '.sqlite'],
}

def get_category(extension):
    """Return the category for a given file extension"""
    extension = extension.lower()
    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category
    return 'Others'

def organize_folder(folder_path):
    """Organize files in the given folder into subfolders by extension"""
    folder_path = Path(folder_path)
    
    if not folder_path.exists():
        print(f"Error: Folder '{folder_path}' does not exist.")
        return
    
    if not folder_path.is_dir():
        print(f"Error: '{folder_path}' is not a directory.")
        return
    
    print(f"Organizing files in: {folder_path}\n")
    
    files_moved = 0
    files_skipped = 0
    
    # Get all files in the directory (not subdirectories)
    for item in folder_path.iterdir():
        if item.is_file():
            # Get file extension
            extension = item.suffix
            
            if not extension:
                category = 'Others'
            else:
                category = get_category(extension)
            
            # Create category folder if it doesn't exist
            category_folder = folder_path / category
            category_folder.mkdir(exist_ok=True)
            
            # Move file to category folder
            destination = category_folder / item.name
            
            # Handle duplicate file names
            counter = 1
            while destination.exists():
                stem = item.stem
                destination = category_folder / f"{stem}_{counter}{extension}"
                counter += 1
            
            try:
                shutil.move(str(item), str(destination))
                print(f"Moved: {item.name} -> {category}/")
                files_moved += 1
            except Exception as e:
                print(f"Error moving {item.name}: {e}")
                files_skipped += 1
    
    print(f"\nOrganization complete!")
    print(f"Files moved: {files_moved}")
    print(f"Files skipped: {files_skipped}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        target_folder = sys.argv[1]
    else:
        target_folder = input("Enter the folder path to organize (or press Enter for current directory): ").strip()
        if not target_folder:
            target_folder = "."
    
    organize_folder(target_folder)
