import os
import sys
from pathlib import Path


def display_tree(directory, prefix="", is_last=True, max_depth=None, current_depth=0):
    """
    Display a folder tree structure in the terminal.
    
    Args:
        directory: Path to the directory to display
        prefix: Prefix string for tree branches
        is_last: Boolean indicating if this is the last item
        max_depth: Maximum depth to traverse (None for unlimited)
        current_depth: Current depth level
    """
    try:
        path = Path(directory)
        
        if not path.exists():
            print(f"Error: Directory '{directory}' does not exist.")
            return
        
        if not path.is_dir():
            print(f"Error: '{directory}' is not a directory.")
            return
        
        # Print current directory
        if current_depth == 0:
            print(f"{path.name}/")
        
        # Check depth limit
        if max_depth is not None and current_depth >= max_depth:
            return
        
        # Get all items in directory
        try:
            items = sorted(path.iterdir(), key=lambda x: (not x.is_dir(), x.name.lower()))
        except PermissionError:
            print(f"{prefix}[Permission Denied]")
            return
        
        # Filter out hidden files (optional - can be modified)
        items = [item for item in items if not item.name.startswith('.')]
        
        # Display each item
        for i, item in enumerate(items):
            is_last_item = i == len(items) - 1
            
            # Create tree characters
            if is_last_item:
                current_prefix = "└── "
                next_prefix = "    "
            else:
                current_prefix = "├── "
                next_prefix = "│   "
            
            # Print item
            if item.is_dir():
                print(f"{prefix}{current_prefix}{item.name}/")
                # Recursively display subdirectory
                display_tree(
                    item, 
                    prefix + next_prefix, 
                    is_last_item, 
                    max_depth, 
                    current_depth + 1
                )
            else:
                # Display file with size
                size = item.stat().st_size
                size_str = format_size(size)
                print(f"{prefix}{current_prefix}{item.name} ({size_str})")
                
    except Exception as e:
        print(f"Error: {e}")


def format_size(size):
    """Format file size in human-readable format."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return f"{size:.1f}{unit}"
        size /= 1024.0
    return f"{size:.1f}PB"


def main():
    """Main function to handle command line arguments."""
    # Default to current directory
    directory = "."
    max_depth = None
    
    # Parse command line arguments
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    
    if len(sys.argv) > 2:
        try:
            max_depth = int(sys.argv[2])
        except ValueError:
            print("Error: Depth must be an integer.")
            sys.exit(1)
    
    print("\n📁 Folder Tree Structure:\n")
    display_tree(directory, max_depth=max_depth)
    print()


if __name__ == "__main__":
    main()
