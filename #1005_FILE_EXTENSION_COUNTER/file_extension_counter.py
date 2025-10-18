#!/usr/bin/env python3
"""
File Extension Counter
Counts and displays the number of files per extension in a specified directory.

Usage:
    python file_extension_counter.py [directory_path]
    
If no directory is specified, uses the current directory.
"""

import os
import sys
from collections import Counter
from pathlib import Path


def count_extensions(directory):
    """
    Count files by extension in the given directory.
    
    Args:
        directory (str): Path to the directory to scan
        
    Returns:
        Counter: Dictionary with extension counts
    """
    extensions = []
    
    try:
        path = Path(directory)
        if not path.exists():
            print(f"Error: Directory '{directory}' does not exist.")
            return Counter()
        
        if not path.is_dir():
            print(f"Error: '{directory}' is not a directory.")
            return Counter()
        
        # Walk through directory and collect extensions
        for item in path.rglob('*'):
            if item.is_file():
                ext = item.suffix if item.suffix else '(no extension)'
                extensions.append(ext)
        
        return Counter(extensions)
    
    except PermissionError:
        print(f"Error: Permission denied accessing '{directory}'.")
        return Counter()
    except Exception as e:
        print(f"Error: {e}")
        return Counter()


def display_results(extension_counts, directory):
    """
    Display the extension counts in a formatted table.
    
    Args:
        extension_counts (Counter): Dictionary with extension counts
        directory (str): The scanned directory path
    """
    if not extension_counts:
        print("No files found or unable to access directory.")
        return
    
    total_files = sum(extension_counts.values())
    
    print(f"\n{'='*60}")
    print(f"File Extension Count Report")
    print(f"Directory: {os.path.abspath(directory)}")
    print(f"{'='*60}\n")
    
    # Sort by count (descending) then by extension name
    sorted_extensions = sorted(
        extension_counts.items(),
        key=lambda x: (-x[1], x[0])
    )
    
    print(f"{'Extension':<20} {'Count':>10} {'Percentage':>12}")
    print(f"{'-'*20} {'-'*10} {'-'*12}")
    
    for ext, count in sorted_extensions:
        percentage = (count / total_files) * 100
        print(f"{ext:<20} {count:>10} {percentage:>11.1f}%")
    
    print(f"\n{'-'*60}")
    print(f"{'Total Files:':<20} {total_files:>10}")
    print(f"{'='*60}\n")


def main():
    """
    Main function to run the file extension counter.
    """
    # Get directory from command line argument or use current directory
    directory = sys.argv[1] if len(sys.argv) > 1 else '.'
    
    print(f"\nScanning directory: {os.path.abspath(directory)}...")
    
    # Count extensions
    extension_counts = count_extensions(directory)
    
    # Display results
    display_results(extension_counts, directory)


if __name__ == "__main__":
    main()
