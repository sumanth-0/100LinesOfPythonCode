#!/usr/bin/env python3
import os
import sys
import fnmatch


def search_files(directory, pattern, search_type='name'):
    """Search for files by name or extension."""
    matches = []
    
    try:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if search_type == 'extension':
                    if file.lower().endswith(pattern.lower()):
                        matches.append(os.path.join(root, file))
                else:  # name search
                    if fnmatch.fnmatch(file.lower(), pattern.lower()):
                        matches.append(os.path.join(root, file))
    except PermissionError:
        print(f"Permission denied: {directory}")
    except Exception as e:
        print(f"Error searching: {e}")
    
    return matches


def display_results(matches, pattern):
    """Display search results."""
    if not matches:
        print(f"No files found matching '{pattern}'")
        return
    
    print(f"Found {len(matches)} file(s) matching '{pattern}':")
    print("-" * 50)
    
    for i, match in enumerate(matches, 1):
        print(f"{i:3d}. {match}")


def main():
    """Main function."""
    print("Terminal File Search")
    print("=" * 25)
    
    # Get directory
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        directory = input("Enter directory to search (or . for current): ").strip()
        if not directory:
            directory = "."
    
    if not os.path.exists(directory):
        print(f"Directory not found: {directory}")
        return
    
    # Get search pattern
    if len(sys.argv) > 2:
        pattern = sys.argv[2]
    else:
        pattern = input("Enter search pattern (e.g., *.py, test*, file.txt): ").strip()
        if not pattern:
            print("No search pattern provided")
            return
    
    # Determine search type
    if pattern.startswith('.') or (len(sys.argv) > 3 and sys.argv[3] == 'ext'):
        search_type = 'extension'
        if not pattern.startswith('.'):
            pattern = '.' + pattern
    else:
        search_type = 'name'
    
    print(f"\nSearching in: {os.path.abspath(directory)}")
    print(f"Pattern: {pattern} ({search_type})")
    print()
    
    # Search and display
    matches = search_files(directory, pattern, search_type)
    display_results(matches, pattern)


if __name__ == "__main__":
    main()