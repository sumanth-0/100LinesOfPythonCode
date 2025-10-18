#!/usr/bin/env python3
"""
File Name Sanitizer
Cleanse filenames in a folder by removing spaces and special characters.
"""

import os
import re
import sys
from pathlib import Path


def sanitize_filename(filename):
    """
    Clean a filename by replacing spaces and removing special characters.
    
    Args:
        filename: The original filename
        
    Returns:
        The sanitized filename
    """
    # Separate name and extension
    name, ext = os.path.splitext(filename)
    
    # Replace spaces with underscores
    name = name.replace(' ', '_')
    
    # Remove special characters (keep only alphanumeric, underscores, and hyphens)
    name = re.sub(r'[^a-zA-Z0-9_-]', '', name)
    
    # Remove multiple consecutive underscores
    name = re.sub(r'_+', '_', name)
    
    # Remove leading/trailing underscores and hyphens
    name = name.strip('_-')
    
    # If name is empty after sanitization, use a default
    if not name:
        name = 'unnamed_file'
    
    return f"{name}{ext}"


def sanitize_folder(folder_path, dry_run=False):
    """
    Sanitize all filenames in the specified folder.
    
    Args:
        folder_path: Path to the folder to process
        dry_run: If True, only show what would be renamed without actually renaming
    """
    folder = Path(folder_path)
    
    if not folder.exists():
        print(f"Error: Folder '{folder_path}' does not exist.")
        return
    
    if not folder.is_dir():
        print(f"Error: '{folder_path}' is not a directory.")
        return
    
    files = [f for f in folder.iterdir() if f.is_file()]
    
    if not files:
        print(f"No files found in '{folder_path}'.")
        return
    
    print(f"\nProcessing {len(files)} file(s) in '{folder_path}'...\n")
    
    renamed_count = 0
    skipped_count = 0
    
    for file_path in files:
        original_name = file_path.name
        sanitized_name = sanitize_filename(original_name)
        
        if original_name == sanitized_name:
            print(f"✓ Skipped: '{original_name}' (already clean)")
            skipped_count += 1
            continue
        
        new_path = file_path.parent / sanitized_name
        
        # Handle name conflicts
        counter = 1
        while new_path.exists():
            name, ext = os.path.splitext(sanitized_name)
            new_path = file_path.parent / f"{name}_{counter}{ext}"
            counter += 1
        
        if dry_run:
            print(f"→ Would rename: '{original_name}' → '{new_path.name}'")
        else:
            file_path.rename(new_path)
            print(f"✓ Renamed: '{original_name}' → '{new_path.name}'")
        
        renamed_count += 1
    
    print(f"\nSummary: {renamed_count} file(s) renamed, {skipped_count} file(s) skipped.")


if __name__ == "__main__":
    # Get folder path from command line or use current directory
    folder = sys.argv[1] if len(sys.argv) > 1 else '.'
    
    # Check for dry-run flag
    dry_run = '--dry-run' in sys.argv or '-d' in sys.argv
    
    print("File Name Sanitizer")
    print("=" * 50)
    
    if dry_run:
        print("[DRY RUN MODE - No files will be renamed]\n")
    
    sanitize_folder(folder, dry_run)
