"""
This script monitors a specified folder in real-time and logs whenever 
files are added, removed, or modified. It helps track file system changes 
for auditing, debugging, or automation purposes.

Example:
    - A new file 'report.pdf' added → Logged as "File created"
    - An existing file deleted → Logged as "File deleted"
    - A file updated → Logged as "File modified"

The script writes all events to a log file named 'folder_activity.log'
inside the same directory as this script.

Dependencies:
    - watchdog (install via pip)
        pip install watchdog

"""

import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path


class FolderEventHandler(FileSystemEventHandler):
    """
    Custom event handler that logs file system changes.

    Methods:
        on_created(event): Triggered when a file/folder is created.
        on_deleted(event): Triggered when a file/folder is deleted.
        on_modified(event): Triggered when a file/folder is modified.
    """

    def on_created(self, event):
        """Logs when a file or folder is created."""
        if not event.is_directory:
            logging.info(f"File created: {event.src_path}")

    def on_deleted(self, event):
        """Logs when a file or folder is deleted."""
        if not event.is_directory:
            logging.info(f"File deleted: {event.src_path}")

    def on_modified(self, event):
        """Logs when a file or folder is modified."""
        if not event.is_directory:
            logging.info(f"File modified: {event.src_path}")


def monitor_folder(folder_path: str) -> None:
    """
    Monitors the given folder and logs file events (create, delete, modify).

    Args:
        folder_path (str): Path to the folder to be monitored.

    Returns:
        None
    """
    folder = Path(folder_path)

    # Validate folder path
    if not folder.is_dir():
        print(f"Error: '{folder_path}' is not a valid directory.")
        return

    # Set up logging configuration
    logging.basicConfig(
        filename="folder_activity.log",
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    print(f"Monitoring started for folder: {folder.resolve()}")
    print("Watching for file additions, deletions, and modifications...")
    print("Press Ctrl + C to stop monitoring.\n")

    # Create an event handler and observer
    event_handler = FolderEventHandler()
    observer = Observer()
    observer.schedule(event_handler, str(folder), recursive=False)

    # Start the observer
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\n Monitoring stopped by user.")
    observer.join()


if __name__ == "__main__":
    # Default folder to monitor (user's Downloads folder)
    default_folder = Path.home() / "Downloads"

    print("=== Folder Activity Monitor ===")
    folder_input = input(f"Enter the folder path to monitor [{default_folder}]: ").strip()
    folder_to_monitor = folder_input if folder_input else str(default_folder)

    # Start monitoring
    monitor_folder(folder_to_monitor)
