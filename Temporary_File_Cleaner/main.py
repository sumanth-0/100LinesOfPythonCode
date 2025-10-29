import os
import argparse
import time
from pathlib import Path

def parse_args():
    """
    Parse command-line arguments for the temporary file cleaner.
    Returns:
        argparse.Namespace: Contains path, mode, days, and dry_run options.
    """
    parser = argparse.ArgumentParser(description="Temporary File Cleaner")
    
    # Positional argument: directory path to clean
    parser.add_argument(
        "path", type=str, help="Path to the directory to clean"
    )
    
    # Optional argument: mode to calculate file age
    parser.add_argument(
        "--mode",
        type=str,
        choices=["created", "modified", "both"],
        default="both",
        help="Use file creation date, last modified date, or both for cleaning"
    )
    
    # Optional argument: age threshold in days
    parser.add_argument(
        "--days",
        type=int,
        required=True,
        help="Delete files older than this many days"
    )
    
    # Optional argument: dry-run mode to preview files without deleting
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show files that would be deleted without actually deleting"
    )
    
    return parser.parse_args()

def file_age_in_days(file_path, mode):
    """
    Calculate the age of a file in days based on the selected mode.
    Returns:
        float: File age in days.
    """
    now = time.time()  # Current timestamp in seconds
    if mode == "created":
        file_time = os.path.getctime(file_path)  # Creation time
    elif mode == "modified":
        file_time = os.path.getmtime(file_path)  # Last modified time
    elif mode == "both":
        # Use the older of creation or modification time
        file_time = min(os.path.getctime(file_path), os.path.getmtime(file_path))
    else:
        raise ValueError("Invalid mode")
    
    return (now - file_time) / (24 * 3600)   # Convert age from seconds to days

def clean_temp_files(path, mode, days_threshold, dry_run=False):
    """
    Delete files older than the specified number of days in the given path.
    Args:
        path (str or Path): Directory to scan.
        mode (str): 'created', 'modified', or 'both'.
        days_threshold (int): Minimum file age in days for deletion.
        dry_run (bool): If True, only show files without deleting.
    """
    path = Path(path)
    
    if not path.exists() or not path.is_dir():
        print(f"Error: Path {path} does not exist or is not a directory.")
        return

    deleted_files = []

    for file in path.rglob("*"):
        if file.is_file():
            age_days = file_age_in_days(file, mode)
        
            if age_days >= days_threshold:  # If the file is older than the threshold
                if dry_run:
                    print(f"[DRY-RUN] Would delete: {file} ({age_days:.1f} days old)")  # Print file instead of deleting
                else:
                    try:
                        file.unlink()
                        deleted_files.append(file)
                        print(f"Deleted: {file} ({age_days:.1f} days old)")
                    except Exception as e:
                        print(f"Error deleting {file}: {e}")

    print(f"\nTotal files deleted: {len(deleted_files)}")   # Summary of deleted files

if __name__ == "__main__":
    args = parse_args()
    clean_temp_files(args.path, args.mode, args.days, args.dry_run) # Start cleaning based on provided arguments