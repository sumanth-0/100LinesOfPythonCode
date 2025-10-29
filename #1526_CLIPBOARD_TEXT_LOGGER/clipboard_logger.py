import pyperclip
import time
import os
from datetime import datetime

# --- Configuration ---
LOG_DIR = r"C://Users//Rachit//100LinesOfPythonCode//#1526_CLIPBOARD_TEXT_LOGGER"
LOG_FILE = os.path.join(LOG_DIR, "clipboard_history.log")  # The file to save history to
CHECK_INTERVAL = 1                # Time to wait between checks (in seconds)
# ---------------------

def write_to_log(content):
    """Appends the given content to the log file with a timestamp."""
    try:
        # Create the directory if it doesn't exist
        os.makedirs(LOG_DIR, exist_ok=True)
        
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            # Use a clear timestamp format
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"--- Logged on {timestamp} ---\n")
            f.write(content + "\n\n")
    except IOError as e:
        print(f"Error: Could not write to log file {LOG_FILE}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    """Main function to monitor the clipboard."""
    print("Clipboard Logger Started.")
    print(f"Monitoring clipboard every {CHECK_INTERVAL} second(s).")
    print(f"History will be saved to: {os.path.abspath(LOG_FILE)}")
    print("Press Ctrl+C to stop.")
    
    recent_content = ""
    try:
        # Get initial content to avoid logging it on the first run
        recent_content = pyperclip.paste()
    except pyperclip.PyperclipException as e:
        print(f"Error accessing clipboard. Is a display environment running? {e}")
        print("Will retry...")

    try:
        while True:
            try:
                current_content = pyperclip.paste()
                
                # Check if content is new, not empty, and different from the previous
                if current_content != recent_content and current_content.strip():
                    print("New clipboard content detected. Logging...")
                    write_to_log(current_content)
                    recent_content = current_content
                    
            except pyperclip.PyperclipException:
                # This can happen if the clipboard is temporarily unavailable
                print("Error reading clipboard. Retrying...")
            
            # Wait for the defined interval
            time.sleep(CHECK_INTERVAL)
            
    except KeyboardInterrupt:
        print("\nLogger stopped successfully. Goodbye!")

if __name__ == "__main__":
    main()