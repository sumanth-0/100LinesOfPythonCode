#!/usr/bin/env python3
"""
Quick File Backup - Fast file and folder backup tool with timestamp

This script provides a simple CLI tool to backup files and folders
to a designated backup directory with automatic timestamping.

Usage:
    python quick_file_backup.py <source> [destination]

If destination is not provided, it creates a 'backups' folder in the current directory.
"""

import os
import shutil
import sys
from datetime import datetime
from pathlib import Path


def create_backup_directory(base_path):
    """Create backup directory with timestamp."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = Path(base_path) / f"backup_{timestamp}"
    backup_dir.mkdir(parents=True, exist_ok=True)
    return backup_dir


def get_size_str(size_bytes):
    """Convert bytes to human-readable format."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} TB"


def backup_file(source, destination):
    """Backup a single file."""
    try:
        dest_file = destination / Path(source).name
        shutil.copy2(source, dest_file)
        size = os.path.getsize(source)
        print(f"✓ Backed up: {source} ({get_size_str(size)})")
        return True
    except Exception as e:
        print(f"✗ Failed to backup {source}: {e}")
        return False


def backup_directory(source, destination):
    """Backup an entire directory."""
    try:
        dest_dir = destination / Path(source).name
        shutil.copytree(source, dest_dir)
        
        total_size = sum(
            os.path.getsize(os.path.join(dirpath, filename))
            for dirpath, _, filenames in os.walk(dest_dir)
            for filename in filenames
        )
        
        print(f"✓ Backed up directory: {source} ({get_size_str(total_size)})")
        return True
    except Exception as e:
        print(f"✗ Failed to backup directory {source}: {e}")
        return False


def main():
    """Main function to handle backup process."""
    if len(sys.argv) < 2:
        print("Usage: python quick_file_backup.py <source> [destination]")
        print("\nExample:")
        print("  python quick_file_backup.py myfile.txt")
        print("  python quick_file_backup.py myfolder /path/to/backups")
        sys.exit(1)
    
    source = sys.argv[1]
    base_dest = sys.argv[2] if len(sys.argv) > 2 else "backups"
    
    if not os.path.exists(source):
        print(f"Error: Source '{source}' does not exist.")
        sys.exit(1)
    
    print(f"\n{'='*50}")
    print("Quick File Backup Tool")
    print(f"{'='*50}\n")
    
    backup_dir = create_backup_directory(base_dest)
    print(f"Backup location: {backup_dir}\n")
    
    success = False
    if os.path.isfile(source):
        success = backup_file(source, backup_dir)
    elif os.path.isdir(source):
        success = backup_directory(source, backup_dir)
    
    if success:
        print(f"\n✓ Backup completed successfully!")
        print(f"Location: {backup_dir}")
    else:
        print(f"\n✗ Backup failed.")
        sys.exit(1)


if __name__ == "__main__":
    main()
