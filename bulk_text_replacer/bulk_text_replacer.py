#!/usr/bin/env python3
"""
Bulk Text Replacer

A comprehensive tool for performing bulk find-and-replace operations across multiple files.
Supports regular expressions, case-sensitive/insensitive matching, backup creation,
and interactive confirmation modes.

Author: Comet Assistant
Issue: #879 - Bulk Text Replacer
Repository: sumanth-0/100LinesOfPythonCode
"""

import os
import re
import sys
import argparse
import shutil
from pathlib import Path
from typing import List, Tuple, Optional
import json
from datetime import datetime


class BulkTextReplacer:
    """
    A class to handle bulk text replacement operations across multiple files.
    """
    
    def __init__(self, directory: str, pattern: str, replacement: str,
                 file_extension: str = None, recursive: bool = True,
                 case_sensitive: bool = True, use_regex: bool = False,
                 backup: bool = True, interactive: bool = False):
        """
        Initialize the BulkTextReplacer with configuration parameters.
        
        Args:
            directory: Root directory to search for files
            pattern: Text pattern to find
            replacement: Text to replace with
            file_extension: Filter by file extension (e.g., '.txt', '.py')
            recursive: Search subdirectories recursively
            case_sensitive: Whether matching should be case-sensitive
            use_regex: Treat pattern as regular expression
            backup: Create backup files before modification
            interactive: Ask for confirmation before each replacement
        """
        self.directory = Path(directory)
        self.pattern = pattern
        self.replacement = replacement
        self.file_extension = file_extension
        self.recursive = recursive
        self.case_sensitive = case_sensitive
        self.use_regex = use_regex
        self.backup = backup
        self.interactive = interactive
        
        # Statistics tracking
        self.files_processed = 0
        self.files_modified = 0
        self.total_replacements = 0
        self.errors = []
        
    def find_files(self) -> List[Path]:
        """
        Find all files matching the specified criteria.
        
        Returns:
            List of Path objects for matching files
        """
        files = []
        
        if self.recursive:
            pattern = '**/*' + (self.file_extension if self.file_extension else '')
            files = list(self.directory.glob(pattern))
        else:
            pattern = '*' + (self.file_extension if self.file_extension else '')
            files = list(self.directory.glob(pattern))
        
        # Filter out directories
        files = [f for f in files if f.is_file()]
        
        return files
    
    def create_backup(self, file_path: Path) -> bool:
        """
        Create a backup copy of the file.
        
        Args:
            file_path: Path to the file to backup
            
        Returns:
            True if backup was successful, False otherwise
        """
        try:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            backup_path = file_path.with_suffix(f'{file_path.suffix}.backup_{timestamp}')
            shutil.copy2(file_path, backup_path)
            return True
        except Exception as e:
            self.errors.append(f"Backup failed for {file_path}: {str(e)}")
            return False
    
    def replace_in_file(self, file_path: Path) -> Tuple[int, str]:
        """
        Perform replacement operations in a single file.
        
        Args:
            file_path: Path to the file to process
            
        Returns:
            Tuple of (number of replacements, modified content)
        """
        try:
            # Read file content
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            original_content = content
            
            # Perform replacement
            if self.use_regex:
                flags = 0 if self.case_sensitive else re.IGNORECASE
                content, count = re.subn(self.pattern, self.replacement, content, flags=flags)
            else:
                if self.case_sensitive:
                    count = content.count(self.pattern)
                    content = content.replace(self.pattern, self.replacement)
                else:
                    # Case-insensitive replacement without regex
                    pattern_lower = self.pattern.lower()
                    count = 0
                    result = []
                    i = 0
                    content_lower = content.lower()
                    
                    while i < len(content):
                        if content_lower[i:i+len(self.pattern)] == pattern_lower:
                            result.append(self.replacement)
                            count += 1
                            i += len(self.pattern)
                        else:
                            result.append(content[i])
                            i += 1
                    
                    content = ''.join(result)
            
            return count, content if count > 0 else original_content
            
        except Exception as e:
            self.errors.append(f"Error processing {file_path}: {str(e)}")
            return 0, None
    
    def process_files(self) -> dict:
        """
        Process all matching files and perform replacements.
        
        Returns:
            Dictionary containing operation statistics
        """
        files = self.find_files()
        
        print(f"Found {len(files)} file(s) to process...\n")
        
        for file_path in files:
            self.files_processed += 1
            
            print(f"Processing: {file_path}")
            
            # Perform replacement
            count, new_content = self.replace_in_file(file_path)
            
            if count > 0:
                if self.interactive:
                    print(f"  Found {count} occurrence(s). Replace? (y/n): ", end='')
                    response = input().lower()
                    if response != 'y':
                        print("  Skipped.")
                        continue
                
                # Create backup if requested
                if self.backup:
                    if not self.create_backup(file_path):
                        print(f"  Warning: Could not create backup, skipping file.")
                        continue
                
                # Write modified content
                try:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    
                    self.files_modified += 1
                    self.total_replacements += count
                    print(f"  Replaced {count} occurrence(s).")
                    
                except Exception as e:
                    self.errors.append(f"Error writing to {file_path}: {str(e)}")
                    print(f"  Error: {str(e)}")
            else:
                print("  No matches found.")
        
        return self.get_statistics()
    
    def get_statistics(self) -> dict:
        """
        Get operation statistics.
        
        Returns:
            Dictionary containing statistics
        """
        return {
            'files_processed': self.files_processed,
            'files_modified': self.files_modified,
            'total_replacements': self.total_replacements,
            'errors': self.errors
        }


def main():
    """
    Main function to handle command-line interface.
    """
    parser = argparse.ArgumentParser(
        description='Bulk Text Replacer - Find and replace text across multiple files',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  # Replace "old" with "new" in all .txt files
  python bulk_text_replacer.py /path/to/dir "old" "new" -e .txt
  
  # Case-insensitive regex replacement in Python files
  python bulk_text_replacer.py . "foo.*bar" "replaced" -e .py -r -i
  
  # Interactive mode without backup
  python bulk_text_replacer.py /docs "draft" "final" --no-backup --interactive
        ''')
    
    parser.add_argument('directory', help='Root directory to search')
    parser.add_argument('pattern', help='Text pattern to find')
    parser.add_argument('replacement', help='Text to replace with')
    parser.add_argument('-e', '--extension', help='File extension filter (e.g., .txt)')
    parser.add_argument('--no-recursive', action='store_true',
                       help='Do not search subdirectories')
    parser.add_argument('-i', '--ignore-case', action='store_true',
                       help='Case-insensitive matching')
    parser.add_argument('-r', '--regex', action='store_true',
                       help='Treat pattern as regular expression')
    parser.add_argument('--no-backup', action='store_true',
                       help='Do not create backup files')
    parser.add_argument('--interactive', action='store_true',
                       help='Ask for confirmation before each replacement')
    
    args = parser.parse_args()
    
    # Validate directory
    if not os.path.exists(args.directory):
        print(f"Error: Directory '{args.directory}' does not exist.")
        sys.exit(1)
    
    # Create replacer instance
    replacer = BulkTextReplacer(
        directory=args.directory,
        pattern=args.pattern,
        replacement=args.replacement,
        file_extension=args.extension,
        recursive=not args.no_recursive,
        case_sensitive=not args.ignore_case,
        use_regex=args.regex,
        backup=not args.no_backup,
        interactive=args.interactive
    )
    
    # Process files
    print("=" * 60)
    print("Bulk Text Replacer")
    print("=" * 60)
    print(f"Directory: {args.directory}")
    print(f"Pattern: {args.pattern}")
    print(f"Replacement: {args.replacement}")
    print(f"Recursive: {not args.no_recursive}")
    print(f"Case-sensitive: {not args.ignore_case}")
    print(f"Regex: {args.regex}")
    print(f"Backup: {not args.no_backup}")
    print("=" * 60)
    print()
    
    stats = replacer.process_files()
    
    # Print summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Files processed: {stats['files_processed']}")
    print(f"Files modified: {stats['files_modified']}")
    print(f"Total replacements: {stats['total_replacements']}")
    
    if stats['errors']:
        print(f"\nErrors ({len(stats['errors'])}):")
        for error in stats['errors']:
            print(f"  - {error}")
    
    print("=" * 60)


if __name__ == '__main__':
    main()
