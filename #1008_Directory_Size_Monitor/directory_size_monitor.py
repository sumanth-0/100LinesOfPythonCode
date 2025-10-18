#!/usr/bin/env python3
"""
Directory Size Monitor - A CLI tool to analyze and report directory sizes
Issue #1008 - Calculate folder sizes and alert if it exceeds a threshold
"""

import os
import sys
import argparse
from pathlib import Path


def get_dir_size(path):
    """Calculate total size of directory recursively."""
    total = 0
    try:
        with os.scandir(path) as entries:
            for entry in entries:
                try:
                    if entry.is_file(follow_symlinks=False):
                        total += entry.stat().st_size
                    elif entry.is_dir(follow_symlinks=False):
                        total += get_dir_size(entry.path)
                except (PermissionError, OSError):
                    continue
    except (PermissionError, OSError):
        pass
    return total


def format_size(size_bytes):
    """Convert bytes to human-readable format."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} PB"


def parse_threshold(threshold_str):
    """Parse threshold string (e.g., '100MB', '1.5GB') to bytes."""
    units = {'B': 1, 'KB': 1024, 'MB': 1024**2, 'GB': 1024**3, 'TB': 1024**4}
    threshold_str = threshold_str.upper().strip()
    
    for unit, multiplier in units.items():
        if threshold_str.endswith(unit):
            try:
                value = float(threshold_str[:-len(unit)])
                return value * multiplier
            except ValueError:
                raise ValueError(f"Invalid threshold format: {threshold_str}")
    
    try:
        return float(threshold_str)
    except ValueError:
        raise ValueError(f"Invalid threshold format: {threshold_str}")


def analyze_directory(directory, threshold=None, recursive=False, top_n=None):
    """Analyze directory and report sizes."""
    path = Path(directory).resolve()
    
    if not path.exists():
        print(f"Error: Directory '{directory}' does not exist.")
        sys.exit(1)
    
    if not path.is_dir():
        print(f"Error: '{directory}' is not a directory.")
        sys.exit(1)
    
    print(f"\nAnalyzing: {path}")
    print("-" * 70)
    
    total_size = get_dir_size(str(path))
    print(f"Total size: {format_size(total_size)} ({total_size:,} bytes)")
    
    if threshold:
        threshold_bytes = parse_threshold(threshold)
        print(f"Threshold: {format_size(threshold_bytes)}")
        if total_size > threshold_bytes:
            print(f"⚠️  WARNING: Directory size exceeds threshold!")
            print(f"   Exceeded by: {format_size(total_size - threshold_bytes)}")
        else:
            print(f"✓ Directory size is within threshold.")
    
    if recursive or top_n:
        print(f"\nSubdirectories:")
        subdirs = []
        try:
            for item in path.iterdir():
                if item.is_dir():
                    size = get_dir_size(str(item))
                    subdirs.append((item.name, size))
        except PermissionError:
            print("Error: Permission denied.")
            return
        
        subdirs.sort(key=lambda x: x[1], reverse=True)
        display_count = top_n if top_n else len(subdirs)
        
        for name, size in subdirs[:display_count]:
            print(f"  {name:40s} {format_size(size):>15s}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Monitor and analyze directory sizes with threshold alerts."
    )
    parser.add_argument("directory", help="Directory path to analyze")
    parser.add_argument("-t", "--threshold", help="Size threshold (e.g., 100MB, 1.5GB)")
    parser.add_argument("-r", "--recursive", action="store_true", help="Show subdirectory sizes")
    parser.add_argument("-n", "--top", type=int, metavar="N", help="Show top N largest subdirectories")
    
    args = parser.parse_args()
    analyze_directory(args.directory, args.threshold, args.recursive, args.top)
