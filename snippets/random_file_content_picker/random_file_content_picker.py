#!/usr/bin/env python3
"""
Random File Content Picker

This script reads a file and randomly selects a line from it.
Useful for displaying random quotes, tasks, tips, or any line-based content.

Usage:
    python random_file_content_picker.py <filename>
    python random_file_content_picker.py <filename> --count <number>
"""

import random
import sys
import os
import argparse
from pathlib import Path


def read_file_lines(filename):
    """
    Read all non-empty lines from a file.
    
    Args:
        filename (str): Path to the file to read
    
    Returns:
        list: List of non-empty lines from the file
    
    Raises:
        FileNotFoundError: If the file doesn't exist
        PermissionError: If the file can't be read
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file if line.strip()]
        return lines
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied to read '{filename}'.")
        sys.exit(1)
    except UnicodeDecodeError:
        print(f"Error: Unable to decode '{filename}'. Please ensure it's a text file.")
        sys.exit(1)


def pick_random_lines(lines, count=1):
    """
    Pick random line(s) from a list of lines.
    
    Args:
        lines (list): List of lines to choose from
        count (int): Number of lines to pick
    
    Returns:
        list: List of randomly selected lines
    """
    if not lines:
        print("Error: The file is empty or contains only whitespace.")
        sys.exit(1)
    
    if count > len(lines):
        print(f"Warning: Requested {count} lines but file only has {len(lines)} lines.")
        count = len(lines)
    
    return random.sample(lines, count) if count > 1 else [random.choice(lines)]


def main():
    """
    Main function to parse arguments and display random lines.
    """
    parser = argparse.ArgumentParser(
        description='Pick random lines from a text file',
        epilog='Example: python random_file_content_picker.py quotes.txt --count 3'
    )
    parser.add_argument('filename', help='Path to the text file')
    parser.add_argument(
        '-c', '--count',
        type=int,
        default=1,
        help='Number of random lines to pick (default: 1)'
    )
    parser.add_argument(
        '-n', '--numbered',
        action='store_true',
        help='Show line numbers with output'
    )
    
    args = parser.parse_args()
    
    # Validate count
    if args.count < 1:
        print("Error: Count must be at least 1.")
        sys.exit(1)
    
    # Read file and pick random lines
    lines = read_file_lines(args.filename)
    selected_lines = pick_random_lines(lines, args.count)
    
    # Display selected lines
    print(f"\n{'='*60}")
    print(f"Random pick from: {Path(args.filename).name}")
    print(f"{'='*60}\n")
    
    for i, line in enumerate(selected_lines, 1):
        if args.numbered:
            print(f"{i}. {line}")
        else:
            print(line)
    
    print(f"\n{'='*60}\n")


if __name__ == "__main__":
    main()
