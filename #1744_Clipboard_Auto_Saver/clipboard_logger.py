import pyperclip # External library for cross-platform clipboard access
import time      # Standard library for sleep function
import os        # Standard library for file operations

# --- Configuration ---
# Name of the file where copied text will be saved.
# Corrected to use 'data.txt' as requested.
OUTPUT_FILENAME = "data.txt" 
# Time in seconds to wait between checking the clipboard
CHECK_INTERVAL = 2 
# ---------------------

def initialize_log_file(filename):
    """Initializes the log file and writes a header if the file is new/empty."""
    try:
        # 'a' mode (append) creates the file if it doesn't exist
        with open(filename, 'a', encoding='utf-8') as f:
            # Check file size. If it's new (0 bytes), write a header.
            if os.path.getsize(filename) == 0:
                f.write("--- Clipboard History Log ---\n")
                f.write(f"Start Time: {time.ctime()}\n")
                f.write("-----------------------------\n")
    except IOError as e:
        print(f"Error initializing file: {e}")
        # Exit if file can't be opened/created due to permissions/issues
        exit(1)

def monitor_clipboard():
    """Continuously monitors the clipboard and logs new, unique content."""
    
    # 1. Setup
    initialize_log_file(OUTPUT_FILENAME)
    print(f"Clipboard monitoring started. Output: {OUTPUT_FILENAME}")
    print(f"Checking every {CHECK_INTERVAL} seconds. Press Ctrl+C to stop.")
    
    # Stores the last seen clipboard content to detect changes.
    last_clipboard_content = "" 

    # 2. Main Loop
    try:
        while True:
            # Get the current content from the clipboard
            current_clipboard_content = pyperclip.paste().strip() 
            
            # Check if content has changed AND is not an empty string
            if current_clipboard_content and (current_clipboard_content != last_clipboard_content):
                
                # A. Log the change and format the entry
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                log_entry = f"[{timestamp}] {current_clipboard_content}\n"
                
                # B. Write to file (opens and closes the file safely)
                with open(OUTPUT_FILENAME, 'a', encoding='utf-8') as f:
                    f.write(log_entry)
                
                # C. Provide console feedback, truncating long entries
                print(f"Saved: '{current_clipboard_content[:50]}{'...' if len(current_clipboard_content) > 50 else ''}'")
                
                # D. Update the 'last seen' content for the next check
                last_clipboard_content = current_clipboard_content
                
            # Wait for the specified interval before checking again
            time.sleep(CHECK_INTERVAL)

    # 3. Cleanup/Exit handlers
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user (Ctrl+C).")
    except pyperclip.PyperclipException as e:
        # Handles errors if the system lacks a required clipboard utility
        print(f"\n[ERROR] Pyperclip access failed: {e}")
        print("Ensure you have 'xclip' or 'xsel' installed on Linux systems.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    # Prerequisite: pip install pyperclip
    monitor_clipboard()