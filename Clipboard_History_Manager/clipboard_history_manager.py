import pyperclip
import json
import os
from datetime import datetime
import time
import threading

class ClipboardHistoryManager:
    def __init__(self, history_file="clipboard_history.json", max_entries=50):
        """Initialize the Clipboard History Manager."""
        self.history_file = history_file
        self.max_entries = max_entries
        self.history = self.load_history()
        self.last_clipboard = ""
        self.running = False
        
    def load_history(self):
        """Load clipboard history from file."""
        if os.path.exists(self.history_file):
            try:
                with open(self.history_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def save_history(self):
        """Save clipboard history to file."""
        with open(self.history_file, 'w', encoding='utf-8') as f:
            json.dump(self.history, f, indent=2, ensure_ascii=False)
    
    def add_to_history(self, text):
        """Add new clipboard entry to history."""
        if text and text.strip():
            entry = {
                "text": text,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "length": len(text)
            }
            # Remove duplicate if exists
            self.history = [h for h in self.history if h["text"] != text]
            # Add to beginning
            self.history.insert(0, entry)
            # Limit history size
            self.history = self.history[:self.max_entries]
            self.save_history()
    
    def monitor_clipboard(self):
        """Monitor clipboard for changes."""
        self.running = True
        print("Clipboard monitoring started...")
        while self.running:
            try:
                current_clipboard = pyperclip.paste()
                if current_clipboard != self.last_clipboard:
                    self.add_to_history(current_clipboard)
                    self.last_clipboard = current_clipboard
                    print(f"New clipboard entry: {current_clipboard[:50]}...")
            except:
                pass
            time.sleep(1)
    
    def stop_monitoring(self):
        """Stop clipboard monitoring."""
        self.running = False
    
    def display_history(self):
        """Display clipboard history."""
        if not self.history:
            print("\nNo clipboard history found.")
            return
        
        print("\n" + "="*60)
        print("CLIPBOARD HISTORY")
        print("="*60)
        for i, entry in enumerate(self.history, 1):
            text_preview = entry["text"][:60].replace('\n', ' ')
            print(f"\n[{i}] Time: {entry['timestamp']}")
            print(f"    Length: {entry['length']} chars")
            print(f"    Preview: {text_preview}...")
        print("="*60)
    
    def get_entry(self, index):
        """Get clipboard entry by index."""
        if 0 <= index < len(self.history):
            return self.history[index]["text"]
        return None
    
    def copy_from_history(self, index):
        """Copy entry from history to clipboard."""
        text = self.get_entry(index - 1)
        if text:
            pyperclip.copy(text)
            print(f"Copied entry #{index} to clipboard.")
            return True
        print("Invalid entry number.")
        return False

if __name__ == "__main__":
    manager = ClipboardHistoryManager()
    print("Clipboard History Manager")
    print("Monitor clipboard for 10 seconds...")
    
    # Start monitoring in background
    thread = threading.Thread(target=manager.monitor_clipboard)
    thread.daemon = True
    thread.start()
    
    # Run for 10 seconds
    time.sleep(10)
    manager.stop_monitoring()
    
    # Display history
    manager.display_history()
