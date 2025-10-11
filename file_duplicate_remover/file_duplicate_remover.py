#!/usr/bin/env python3
"""File Duplicate Remover - Scan folder and remove duplicates by hash."""

import os
import sys
import hashlib
from pathlib import Path
from collections import defaultdict

def calculate_hash(filepath, algorithm='sha256', chunk_size=8192):
    """Calculate hash of a file."""
    hasher = hashlib.new(algorithm)
    try:
        with open(filepath, 'rb') as f:
            while chunk := f.read(chunk_size):
                hasher.update(chunk)
        return hasher.hexdigest()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return None

def find_duplicates(folder_path):
    """Find duplicate files in a folder by comparing hashes."""
    hash_map = defaultdict(list)
    folder = Path(folder_path)
    
    if not folder.exists():
        print(f"Error: Folder '{folder_path}' does not exist.")
        return {}
    
    print(f"Scanning folder: {folder.absolute()}")
    files = list(folder.rglob('*'))
    total_files = len([f for f in files if f.is_file()])
    
    print(f"Found {total_files} files. Calculating hashes...")
    
    for file_path in files:
        if file_path.is_file():
            file_hash = calculate_hash(file_path)
            if file_hash:
                hash_map[file_hash].append(file_path)
    
    duplicates = {h: paths for h, paths in hash_map.items() if len(paths) > 1}
    return duplicates

def display_duplicates(duplicates):
    """Display duplicate files grouped by hash."""
    if not duplicates:
        print("\nNo duplicate files found.")
        return
    
    print(f"\nFound {len(duplicates)} sets of duplicate files:")
    total_duplicates = sum(len(paths) - 1 for paths in duplicates.values())
    total_size = 0
    
    for i, (file_hash, paths) in enumerate(duplicates.items(), 1):
        size = paths[0].stat().st_size
        wasted = size * (len(paths) - 1)
        total_size += wasted
        
        print(f"\n[{i}] Hash: {file_hash[:16]}... ({len(paths)} copies, {size:,} bytes each)")
        for path in paths:
            print(f"    - {path}")
    
    print(f"\nTotal: {total_duplicates} duplicate file(s) wasting {total_size:,} bytes")

def remove_duplicates(duplicates, keep_first=True):
    """Remove duplicate files, keeping one copy."""
    if not duplicates:
        return
    
    removed_count = 0
    for paths in duplicates.values():
        files_to_remove = paths[1:] if keep_first else paths[:-1]
        for file_path in files_to_remove:
            try:
                file_path.unlink()
                print(f"Removed: {file_path}")
                removed_count += 1
            except Exception as e:
                print(f"Error removing {file_path}: {e}")
    
    print(f"\nSuccessfully removed {removed_count} duplicate file(s).")

def main():
    """Main function to handle command-line arguments and execute."""
    if len(sys.argv) < 2:
        print("Usage: python file_duplicate_remover.py <folder_path> [--remove]")
        print("  <folder_path>  : Path to scan for duplicates")
        print("  --remove       : Remove duplicates (keeps first occurrence)")
        sys.exit(1)
    
    folder_path = sys.argv[1]
    remove_flag = '--remove' in sys.argv
    
    duplicates = find_duplicates(folder_path)
    display_duplicates(duplicates)
    
    if remove_flag and duplicates:
        response = input("\nAre you sure you want to remove duplicates? (yes/no): ")
        if response.lower() == 'yes':
            remove_duplicates(duplicates)
        else:
            print("Operation cancelled.")

if __name__ == '__main__':
    main()
