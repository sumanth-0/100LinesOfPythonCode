#!/usr/bin/env python3
"""
Terminal File Search
A powerful command-line tool for searching files with various filters.
"""

import os
import sys
import argparse
from pathlib import Path
import fnmatch
from datetime import datetime


def format_size(size):
    """Format file size in human-readable format."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return f"{size:.2f} {unit}"
        size /= 1024.0
    return f"{size:.2f} PB"


def format_time(timestamp):
    """Format timestamp to readable date."""
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')


def matches_criteria(file_path, args):
    """Check if file matches all search criteria."""
    try:
        stat = file_path.stat()
        
        # Check name pattern
        if args.name and not fnmatch.fnmatch(file_path.name, args.name):
            return False
        
        # Check extension
        if args.ext and not file_path.suffix.lower() == f".{args.ext.lower()}":
            return False
        
        # Check minimum size
        if args.min_size and stat.st_size < args.min_size * 1024:
            return False
        
        # Check maximum size
        if args.max_size and stat.st_size > args.max_size * 1024:
            return False
        
        # Check file type
        if args.type:
            if args.type == 'f' and not file_path.is_file():
                return False
            if args.type == 'd' and not file_path.is_dir():
                return False
        
        return True
    except (OSError, PermissionError):
        return False


def search_files(directory, args):
    """Search files in directory based on criteria."""
    results = []
    try:
        path = Path(directory).resolve()
        
        for item in path.rglob('*') if args.recursive else path.glob('*'):
            if matches_criteria(item, args):
                results.append(item)
                
                if args.limit and len(results) >= args.limit:
                    break
    except PermissionError:
        print(f"Permission denied: {directory}", file=sys.stderr)
    
    return results


def display_results(results, args):
    """Display search results."""
    if not results:
        print("No files found matching the criteria.")
        return
    
    print(f"\nFound {len(results)} file(s):\n")
    
    for file_path in sorted(results):
        if args.verbose:
            try:
                stat = file_path.stat()
                size = format_size(stat.st_size)
                mtime = format_time(stat.st_mtime)
                print(f"{file_path} | Size: {size} | Modified: {mtime}")
            except OSError:
                print(file_path)
        else:
            print(file_path)


def main():
    parser = argparse.ArgumentParser(
        description="Search files in terminal with various filters"
    )
    parser.add_argument('directory', nargs='?', default='.', help='Directory to search (default: current)')
    parser.add_argument('-n', '--name', help='File name pattern (supports wildcards)')
    parser.add_argument('-e', '--ext', help='File extension (without dot)')
    parser.add_argument('-t', '--type', choices=['f', 'd'], help='Type: f=file, d=directory')
    parser.add_argument('--min-size', type=int, help='Minimum file size in KB')
    parser.add_argument('--max-size', type=int, help='Maximum file size in KB')
    parser.add_argument('-r', '--recursive', action='store_true', help='Search recursively')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output with details')
    parser.add_argument('-l', '--limit', type=int, help='Limit number of results')
    
    args = parser.parse_args()
    
    results = search_files(args.directory, args)
    display_results(results, args)


if __name__ == "__main__":
    main()
