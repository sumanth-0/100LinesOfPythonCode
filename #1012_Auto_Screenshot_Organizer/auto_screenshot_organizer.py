#!/usr/bin/env python3
"""
Auto Screenshot Organizer - Automatically organize screenshots by date
"""

import os
import shutil
import re
from datetime import datetime
from pathlib import Path
import argparse


def is_screenshot(filename):
    """Check if a file is a screenshot based on common naming patterns"""
    screenshot_patterns = [
        r'screenshot',
        r'screen shot',
        r'screen_shot',
        r'capture',
        r'scr_\d+',
        r'img_\d+',
    ]
    filename_lower = filename.lower()
    return any(re.search(pattern, filename_lower) for pattern in screenshot_patterns)


def get_file_date(filepath):
    """Get the creation/modification date of a file"""
    stat = os.stat(filepath)
    # Use creation time if available, otherwise use modification time
    timestamp = stat.st_birthtime if hasattr(stat, 'st_birthtime') else stat.st_mtime
    return datetime.fromtimestamp(timestamp)


def organize_screenshots(source_dir, dest_dir=None, dry_run=False):
    """Organize screenshots from source directory into dated folders"""
    source_path = Path(source_dir).expanduser().resolve()
    
    if not source_path.exists():
        print(f"Error: Source directory '{source_dir}' does not exist.")
        return
    
    # If no destination specified, create 'Screenshots_Organized' in source dir
    if dest_dir is None:
        dest_path = source_path / 'Screenshots_Organized'
    else:
        dest_path = Path(dest_dir).expanduser().resolve()
    
    if not dry_run:
        dest_path.mkdir(parents=True, exist_ok=True)
    
    # Supported image extensions
    image_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp'}
    
    moved_count = 0
    
    print(f"Scanning directory: {source_path}")
    print(f"Destination: {dest_path}")
    print("---")
    
    for file_path in source_path.iterdir():
        if file_path.is_file() and file_path.suffix.lower() in image_extensions:
            if is_screenshot(file_path.name):
                file_date = get_file_date(file_path)
                date_folder = file_date.strftime('%Y-%m-%d')
                target_dir = dest_path / date_folder
                target_file = target_dir / file_path.name
                
                # Handle duplicate filenames
                counter = 1
                while target_file.exists():
                    name_parts = file_path.stem
                    target_file = target_dir / f"{name_parts}_{counter}{file_path.suffix}"
                    counter += 1
                
                if dry_run:
                    print(f"[DRY RUN] Would move: {file_path.name} -> {date_folder}/")
                else:
                    target_dir.mkdir(parents=True, exist_ok=True)
                    shutil.move(str(file_path), str(target_file))
                    print(f"Moved: {file_path.name} -> {date_folder}/")
                
                moved_count += 1
    
    print("---")
    print(f"Total screenshots {'found' if dry_run else 'organized'}: {moved_count}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Organize screenshots by date automatically')
    parser.add_argument('source', help='Source directory containing screenshots')
    parser.add_argument('-d', '--dest', help='Destination directory (default: Screenshots_Organized in source)')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be moved without moving files')
    
    args = parser.parse_args()
    organize_screenshots(args.source, args.dest, args.dry_run)
