#!/usr/bin/env python3
import os
import sys


def get_size(path):
    """Get total size of directory in bytes."""
    total = 0
    try:
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                try:
                    total += os.path.getsize(filepath)
                except (OSError, FileNotFoundError):
                    pass
    except (OSError, PermissionError):
        pass
    return total


def format_size(bytes_size):
    """Convert bytes to human-readable format."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_size < 1024.0:
            return f"{bytes_size:.1f} {unit}"
        bytes_size /= 1024.0
    return f"{bytes_size:.1f} PB"


def calculate_folder_sizes(directory):
    """Calculate sizes of all folders in directory."""
    folder_sizes = []
    
    try:
        items = os.listdir(directory)
        for item in items:
            item_path = os.path.join(directory, item)
            if os.path.isdir(item_path):
                size = get_size(item_path)
                folder_sizes.append((item, size))
    except (OSError, PermissionError) as e:
        print(f"Error accessing directory: {e}")
        return []
    
    return sorted(folder_sizes, key=lambda x: x[1], reverse=True)


def display_results(folder_sizes, directory):
    """Display folder sizes in formatted table."""
    if not folder_sizes:
        print("No folders found or permission denied")
        return
    
    print(f"\nFolder sizes in: {directory}")
    print("-" * 50)
    print(f"{'Folder Name':<30} {'Size':<15}")
    print("-" * 50)
    
    total_size = 0
    for folder, size in folder_sizes:
        formatted_size = format_size(size)
        print(f"{folder:<30} {formatted_size:<15}")
        total_size += size
    
    print("-" * 50)
    print(f"{'Total':<30} {format_size(total_size):<15}")


def main():
    """Main function."""
    print("Folder Size Calculator")
    print("=" * 25)
    
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        directory = input("Enter directory path (or . for current): ").strip()
        if not directory:
            directory = "."
    
    if not os.path.exists(directory):
        print(f"Directory not found: {directory}")
        return
    
    if not os.path.isdir(directory):
        print(f"Not a directory: {directory}")
        return
    
    print(f"\nCalculating folder sizes in: {os.path.abspath(directory)}")
    folder_sizes = calculate_folder_sizes(directory)
    display_results(folder_sizes, directory)


if __name__ == "__main__":
    main()