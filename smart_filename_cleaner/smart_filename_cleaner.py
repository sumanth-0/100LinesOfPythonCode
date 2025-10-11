#!/usr/bin/env python3
"""
Smart Filename Cleaner
Batch renames files in a folder for consistency by:
- Converting to snake_case
- Removing spaces and special characters
- Removing duplicate words
- Making filenames lowercase and clean
"""

import os
import re
import sys
from pathlib import Path
from collections import defaultdict

def clean_filename(filename):
    """Clean a filename by removing special chars, spaces, duplicates, and converting to snake_case."""
    name, ext = os.path.splitext(filename)
    
    # Convert to lowercase
    name = name.lower()
    
    # Replace spaces and hyphens with underscores
    name = re.sub(r'[\s-]+', '_', name)
    
    # Remove special characters except underscores and dots
    name = re.sub(r'[^a-z0-9_.]', '', name)
    
    # Remove duplicate underscores
    name = re.sub(r'_+', '_', name)
    
    # Remove duplicate words (e.g., "file_file_name" -> "file_name")
    words = name.split('_')
    cleaned_words = []
    prev_word = None
    for word in words:
        if word and word != prev_word:
            cleaned_words.append(word)
            prev_word = word
    name = '_'.join(cleaned_words)
    
    # Strip leading/trailing underscores
    name = name.strip('_')
    
    # Ensure name is not empty
    if not name:
        name = 'unnamed'
    
    return name + ext.lower()

def rename_files(directory, preview=True):
    """Rename all files in the specified directory."""
    if not os.path.isdir(directory):
        print(f"Error: '{directory}' is not a valid directory.")
        return
    
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    if not files:
        print(f"No files found in '{directory}'.")
        return
    
    # Check for naming conflicts
    new_names = defaultdict(list)
    changes = []
    
    for filename in files:
        new_name = clean_filename(filename)
        if filename != new_name:
            new_names[new_name].append(filename)
            changes.append((filename, new_name))
    
    if not changes:
        print("No files need renaming. All filenames are already clean!")
        return
    
    # Display preview
    print(f"\nFiles to be renamed in '{directory}':")
    print("-" * 60)
    
    # Handle conflicts by adding numbers
    final_changes = []
    name_counter = defaultdict(int)
    
    for old_name, new_name in changes:
        # If there are conflicts, add a number
        if len(new_names[new_name]) > 1 or os.path.exists(os.path.join(directory, new_name)):
            name_counter[new_name] += 1
            base, ext = os.path.splitext(new_name)
            final_name = f"{base}_{name_counter[new_name]}{ext}"
        else:
            final_name = new_name
        
        final_changes.append((old_name, final_name))
        print(f"{old_name:30} -> {final_name}")
    
    print("-" * 60)
    print(f"Total: {len(final_changes)} files will be renamed.\n")
    
    if preview:
        response = input("Proceed with renaming? (yes/no): ").strip().lower()
        if response not in ['yes', 'y']:
            print("Operation cancelled.")
            return
    
    # Perform renaming
    success_count = 0
    for old_name, new_name in final_changes:
        try:
            old_path = os.path.join(directory, old_name)
            new_path = os.path.join(directory, new_name)
            os.rename(old_path, new_path)
            success_count += 1
        except Exception as e:
            print(f"Error renaming '{old_name}': {e}")
    
    print(f"\nSuccessfully renamed {success_count} out of {len(final_changes)} files.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python smart_filename_cleaner.py <directory> [--no-preview]")
        print("Example: python smart_filename_cleaner.py ./downloads")
        sys.exit(1)
    
    target_dir = sys.argv[1]
    preview = '--no-preview' not in sys.argv
    
    rename_files(target_dir, preview)
