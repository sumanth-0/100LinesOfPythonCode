#!/usr/bin/env python3
"""
Terminal Clipboard Manager
A command-line tool for managing clipboard history with copy, paste, list, and clear operations.
"""

import os
import sys
import json
import argparse
import pyperclip
from datetime import datetime
from pathlib import Path


class ClipboardManager:
    """Manages clipboard history and operations."""
    
    def __init__(self, history_file=None):
        """Initialize the clipboard manager."""
        if history_file:
            self.history_file = Path(history_file)
        else:
            self.history_file = Path.home() / '.clipboard_history.json'
        self.history = self._load_history()
    
    def _load_history(self):
        """Load clipboard history from file."""
        if self.history_file.exists():
            try:
                with open(self.history_file, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return []
        return []
    
    def _save_history(self):
        """Save clipboard history to file."""
        try:
            with open(self.history_file, 'w') as f:
                json.dump(self.history, f, indent=2)
        except IOError as e:
            print(f"Error saving history: {e}")
    
    def copy(self, text):
        """Copy text to clipboard and add to history."""
        try:
            pyperclip.copy(text)
            entry = {
                'text': text,
                'timestamp': datetime.now().isoformat(),
                'length': len(text)
            }
            self.history.insert(0, entry)
            # Keep only last 100 entries
            self.history = self.history[:100]
            self._save_history()
            print(f"✓ Copied {len(text)} characters to clipboard")
            return True
        except Exception as e:
            print(f"Error copying to clipboard: {e}")
            return False
    
    def paste(self):
        """Paste content from clipboard."""
        try:
            content = pyperclip.paste()
            if content:
                print(content)
                return content
            else:
                print("Clipboard is empty")
                return None
        except Exception as e:
            print(f"Error pasting from clipboard: {e}")
            return None
    
    def list_history(self, limit=10):
        """List clipboard history."""
        if not self.history:
            print("No clipboard history found")
            return
        
        print(f"\nClipboard History (showing last {min(limit, len(self.history))} entries):\n")
        print("-" * 80)
        
        for idx, entry in enumerate(self.history[:limit], 1):
            timestamp = entry.get('timestamp', 'Unknown')
            length = entry.get('length', 0)
            text = entry.get('text', '')
            
            # Format timestamp
            try:
                dt = datetime.fromisoformat(timestamp)
                formatted_time = dt.strftime('%Y-%m-%d %H:%M:%S')
            except:
                formatted_time = timestamp
            
            # Truncate text for display
            display_text = text[:60] + '...' if len(text) > 60 else text
            display_text = display_text.replace('\n', '\\n')
            
            print(f"{idx}. [{formatted_time}] ({length} chars)")
            print(f"   {display_text}")
            print("-" * 80)
    
    def clear_history(self):
        """Clear all clipboard history."""
        self.history = []
        self._save_history()
        print("✓ Clipboard history cleared")
    
    def get_entry(self, index):
        """Get a specific entry from history."""
        try:
            if 0 <= index < len(self.history):
                return self.history[index]
            else:
                print(f"Invalid index. History contains {len(self.history)} entries.")
                return None
        except Exception as e:
            print(f"Error retrieving entry: {e}")
            return None
    
    def copy_from_history(self, index):
        """Copy a specific entry from history to clipboard."""
        entry = self.get_entry(index)
        if entry:
            text = entry.get('text', '')
            try:
                pyperclip.copy(text)
                print(f"✓ Copied entry {index + 1} to clipboard")
                return True
            except Exception as e:
                print(f"Error copying from history: {e}")
                return False
        return False


def main():
    """Main function to handle command-line interface."""
    parser = argparse.ArgumentParser(
        description='Terminal Clipboard Manager - Manage your clipboard history',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s copy "Hello World"       Copy text to clipboard
  %(prog)s paste                    Paste from clipboard
  %(prog)s list                     Show clipboard history
  %(prog)s list -n 20               Show last 20 entries
  %(prog)s recall 3                 Copy 3rd history entry to clipboard
  %(prog)s clear                    Clear all history
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Copy command
    copy_parser = subparsers.add_parser('copy', help='Copy text to clipboard')
    copy_parser.add_argument('text', help='Text to copy to clipboard')
    
    # Paste command
    subparsers.add_parser('paste', help='Paste content from clipboard')
    
    # List command
    list_parser = subparsers.add_parser('list', help='List clipboard history')
    list_parser.add_argument('-n', '--number', type=int, default=10,
                             help='Number of entries to display (default: 10)')
    
    # Recall command
    recall_parser = subparsers.add_parser('recall', help='Copy entry from history to clipboard')
    recall_parser.add_argument('index', type=int, help='Entry index to recall (1-based)')
    
    # Clear command
    subparsers.add_parser('clear', help='Clear clipboard history')
    
    # Parse arguments
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    # Initialize clipboard manager
    manager = ClipboardManager()
    
    # Execute command
    if args.command == 'copy':
        manager.copy(args.text)
    elif args.command == 'paste':
        manager.paste()
    elif args.command == 'list':
        manager.list_history(args.number)
    elif args.command == 'recall':
        # Convert 1-based index to 0-based
        manager.copy_from_history(args.index - 1)
    elif args.command == 'clear':
        manager.clear_history()
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == '__main__':
    main()
