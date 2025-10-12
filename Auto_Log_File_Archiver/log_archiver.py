#!/usr/bin/env python3
import os
import shutil
import time
from datetime import datetime, timedelta


def get_log_files(directory):
    """Get all log files from directory."""
    log_extensions = ['.log', '.txt', '.out']
    log_files = []
    
    try:
        for file in os.listdir(directory):
            if any(file.lower().endswith(ext) for ext in log_extensions):
                log_files.append(os.path.join(directory, file))
    except PermissionError:
        print(f"Permission denied: {directory}")
    except FileNotFoundError:
        print(f"Directory not found: {directory}")
    
    return log_files


def is_older_than_week(file_path):
    """Check if file is older than a week."""
    try:
        file_time = os.path.getmtime(file_path)
        file_date = datetime.fromtimestamp(file_time)
        week_ago = datetime.now() - timedelta(days=7)
        return file_date < week_ago
    except OSError:
        return False


def archive_logs(log_dir, archive_dir=None):
    """Archive log files older than a week."""
    if not archive_dir:
        archive_dir = os.path.join(log_dir, "archive")
    
    # Create archive directory if it doesn't exist
    os.makedirs(archive_dir, exist_ok=True)
    
    log_files = get_log_files(log_dir)
    archived_count = 0
    
    for log_file in log_files:
        if is_older_than_week(log_file):
            try:
                filename = os.path.basename(log_file)
                archive_path = os.path.join(archive_dir, filename)
                
                # Handle duplicate names by adding timestamp
                if os.path.exists(archive_path):
                    name, ext = os.path.splitext(filename)
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    filename = f"{name}_{timestamp}{ext}"
                    archive_path = os.path.join(archive_dir, filename)
                
                shutil.move(log_file, archive_path)
                print(f"Archived: {filename}")
                archived_count += 1
                
            except Exception as e:
                print(f"Error archiving {log_file}: {e}")
    
    return archived_count


def create_sample_logs(directory):
    """Create sample log files for testing."""
    os.makedirs(directory, exist_ok=True)
    
    # Create recent log
    recent_log = os.path.join(directory, "recent.log")
    with open(recent_log, 'w') as f:
        f.write("Recent log entry\n")
    
    # Create old log (simulate 10 days old)
    old_log = os.path.join(directory, "old.log")
    with open(old_log, 'w') as f:
        f.write("Old log entry\n")
    
    # Set old file timestamp to 10 days ago
    ten_days_ago = time.time() - (10 * 24 * 60 * 60)
    os.utime(old_log, (ten_days_ago, ten_days_ago))
    
    print(f"Created sample logs in: {directory}")


def main():
    """Main function."""
    print("Auto Log File Archiver")
    print("=" * 25)
    
    log_dir = input("Enter log directory (or press Enter for sample): ").strip()
    
    if not log_dir:
        log_dir = "sample_logs"
        create_sample_logs(log_dir)
    
    if not os.path.exists(log_dir):
        print(f"Directory not found: {log_dir}")
        return
    
    archive_dir = input("Enter archive directory (optional): ").strip()
    if not archive_dir:
        archive_dir = None
    
    print(f"\nScanning: {log_dir}")
    archived_count = archive_logs(log_dir, archive_dir)
    
    if archived_count > 0:
        print(f"\nArchived {archived_count} log file(s)")
    else:
        print("\nNo log files to archive")


if __name__ == "__main__":
    main()