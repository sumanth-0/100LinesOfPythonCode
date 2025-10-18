#!/usr/bin/env python3
"""
File Extension Counter - Counts files by extension in a directory
Usage: python file_extension_counter.py [directory_path]
"""
import os
import sys
from collections import Counter
from pathlib import Path

def count_extensions(directory):
    """Count files by extension in the given directory."""
    extensions = []
    try:
        path = Path(directory)
        if not path.exists():
            print(f"Error: Directory '{directory}' does not exist.")
            return Counter()
        if not path.is_dir():
            print(f"Error: '{directory}' is not a directory.")
            return Counter()
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
    """Display the extension counts in a formatted table."""
    if not extension_counts:
        print("No files found or unable to access directory.")
        return
    total_files = sum(extension_counts.values())
    print(f"\n{'='*60}")
    print(f"File Extension Count Report")
    print(f"Directory: {os.path.abspath(directory)}")
    print(f"{'='*60}\n")
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
    """Main function to run the file extension counter."""
    directory = sys.argv[1] if len(sys.argv) > 1 else '.'
    print(f"\nScanning directory: {os.path.abspath(directory)}...")
    extension_counts = count_extensions(directory)
    display_results(extension_counts, directory)

if __name__ == "__main__":
    main()
