#!/usr/bin/env python3
"""
Random File Selector

A command-line tool to randomly select one or more files from a specified directory.
Supports filtering by file extension, recursive search, and various output formats.

Author: GitHub Contributor
Issue: #1009
"""

import os
import sys
import random
import argparse
from pathlib import Path
from typing import List, Optional
import json


class RandomFileSelector:
    """
    A class to handle random file selection from directories.
    """
    
    def __init__(self, directory: str, recursive: bool = False, 
                 extensions: Optional[List[str]] = None, 
                 exclude_hidden: bool = True):
        """
        Initialize the RandomFileSelector.
        
        Args:
            directory: Path to the directory to search
            recursive: Whether to search subdirectories
            extensions: List of file extensions to filter (e.g., ['.txt', '.py'])
            exclude_hidden: Whether to exclude hidden files
        """
        self.directory = Path(directory)
        self.recursive = recursive
        self.extensions = [ext.lower() if ext.startswith('.') else f'.{ext.lower()}' 
                          for ext in (extensions or [])]
        self.exclude_hidden = exclude_hidden
        
        if not self.directory.exists():
            raise ValueError(f"Directory does not exist: {directory}")
        if not self.directory.is_dir():
            raise ValueError(f"Path is not a directory: {directory}")
    
    def get_all_files(self) -> List[Path]:
        """
        Get all files from the directory based on the specified criteria.
        
        Returns:
            List of Path objects for files
        """
        files = []
        
        if self.recursive:
            pattern = '**/*'
        else:
            pattern = '*'
        
        for item in self.directory.glob(pattern):
            # Skip if it's a directory
            if item.is_dir():
                continue
            
            # Skip hidden files if requested
            if self.exclude_hidden and item.name.startswith('.'):
                continue
            
            # Filter by extension if specified
            if self.extensions and item.suffix.lower() not in self.extensions:
                continue
            
            files.append(item)
        
        return files
    
    def select_random_files(self, count: int = 1, unique: bool = True) -> List[Path]:
        """
        Select random files from the directory.
        
        Args:
            count: Number of files to select
            unique: Whether to select unique files (no duplicates)
        
        Returns:
            List of randomly selected Path objects
        """
        all_files = self.get_all_files()
        
        if not all_files:
            return []
        
        if unique:
            count = min(count, len(all_files))
            return random.sample(all_files, count)
        else:
            return [random.choice(all_files) for _ in range(count)]
    
    def get_file_info(self, file_path: Path) -> dict:
        """
        Get detailed information about a file.
        
        Args:
            file_path: Path to the file
        
        Returns:
            Dictionary containing file information
        """
        stats = file_path.stat()
        return {
            'name': file_path.name,
            'path': str(file_path.absolute()),
            'size': stats.st_size,
            'extension': file_path.suffix,
            'relative_path': str(file_path.relative_to(self.directory))
        }


def format_output(files: List[Path], selector: RandomFileSelector, 
                  output_format: str = 'simple') -> str:
    """
    Format the output based on the specified format.
    
    Args:
        files: List of selected files
        selector: RandomFileSelector instance
        output_format: Output format ('simple', 'detailed', 'json')
    
    Returns:
        Formatted string output
    """
    if not files:
        return "No files found matching the criteria."
    
    if output_format == 'json':
        file_infos = [selector.get_file_info(f) for f in files]
        return json.dumps(file_infos, indent=2)
    
    elif output_format == 'detailed':
        output = []
        for i, file_path in enumerate(files, 1):
            info = selector.get_file_info(file_path)
            output.append(f"\n[{i}] {info['name']}")
            output.append(f"    Path: {info['path']}")
            output.append(f"    Size: {info['size']} bytes")
            output.append(f"    Extension: {info['extension'] or 'None'}")
        return '\n'.join(output)
    
    else:  # simple
        return '\n'.join(str(f.absolute()) for f in files)


def main():
    """
    Main function to handle command-line arguments and execute the program.
    """
    parser = argparse.ArgumentParser(
        description='Randomly select files from a directory',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s /path/to/directory
  %(prog)s /path/to/directory -n 5 -r
  %(prog)s /path/to/directory -e txt py -f detailed
  %(prog)s /path/to/directory -e jpg png -n 3 -f json
        """
    )
    
    parser.add_argument('directory', type=str, 
                       help='Directory to search for files')
    parser.add_argument('-n', '--number', type=int, default=1,
                       help='Number of files to select (default: 1)')
    parser.add_argument('-r', '--recursive', action='store_true',
                       help='Search subdirectories recursively')
    parser.add_argument('-e', '--extensions', nargs='+', 
                       help='Filter by file extensions (e.g., txt py jpg)')
    parser.add_argument('-f', '--format', choices=['simple', 'detailed', 'json'],
                       default='simple', help='Output format (default: simple)')
    parser.add_argument('--include-hidden', action='store_true',
                       help='Include hidden files (starting with .)')
    parser.add_argument('--allow-duplicates', action='store_true',
                       help='Allow selecting the same file multiple times')
    parser.add_argument('-s', '--seed', type=int,
                       help='Random seed for reproducible results')
    
    args = parser.parse_args()
    
    # Set random seed if provided
    if args.seed is not None:
        random.seed(args.seed)
    
    try:
        # Create selector instance
        selector = RandomFileSelector(
            directory=args.directory,
            recursive=args.recursive,
            extensions=args.extensions,
            exclude_hidden=not args.include_hidden
        )
        
        # Select random files
        selected_files = selector.select_random_files(
            count=args.number,
            unique=not args.allow_duplicates
        )
        
        # Format and print output
        output = format_output(selected_files, selector, args.format)
        print(output)
        
        # Exit with success
        sys.exit(0)
        
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(2)


if __name__ == '__main__':
    main()
