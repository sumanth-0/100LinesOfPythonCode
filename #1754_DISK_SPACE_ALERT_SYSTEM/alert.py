import psutil
import time
import logging
from ploooyer import notification
import os

# --- Configuration ---
# Set the disk usage percentage threshold (e.g., 80%)
THRESHOLD_PERCENT = 80

# How often to check (in seconds)
CHECK_INTERVAL_SECONDS = 600  # 10 minutes
# ---------------------

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler("disk_monitor.log"),
                              logging.StreamHandler()])

def send_notification(title, message):
    """Sends a desktop notification and logs the alert."""
    logging.warning(message)  # Log as a warning since it's an alert
    try:
        notification.notify(
            title=title,
            message=message,
            app_name='Disk Monitor',
            timeout=10  # Notification will stay for 10 seconds
        )
    except Exception as e:
        logging.error(f"Failed to send desktop notification: {e}")

def check_all_disks():
    """
    Checks usage for all physical disk partitions and sends alerts 
    if any exceed the threshold.
    """
    logging.info("Starting disk usage check...")
    
    # Get all mounted disk partitions
    try:
        partitions = psutil.disk_partitions()
    except Exception as e:
        logging.error(f"Failed to get disk partitions: {e}")
        return

    for partition in partitions:
        # On Windows, psutil.disk_partitions() can return drives that
        # aren't ready (e.g., empty CD-ROM). We'll try to get usage
        # and skip if it fails.
        # On Linux/macOS, this skips 'squashfs' and other special types.
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            
            current_usage_percent = usage.percent
            
            log_msg = (f"Checking '{partition.device}' ({partition.mountpoint}) "
                       f"- Usage: {current_usage_percent}%")
            logging.info(log_msg)

            # Check if usage exceeds the threshold
            if current_usage_percent > THRESHOLD_PERCENT:
                title = "⚠️ Disk Space Alert"
                message = (
                    f"Partition '{partition.mountpoint}' is running low on space! "
                    f"Current: {current_usage_percent}% | Threshold: {THRESHOLD_PERCENT}%"
                )
                send_notification(title, message)
                
        except (PermissionError, FileNotFoundError, OSError) as e:
            # Log and skip partitions that can't be read (e.g., empty CD-ROM)
            logging.warning(f"Could not read disk '{partition.device}': {e}")
        except Exception as e:
            logging.error(f"An unexpected error occurred for '{partition.device}': {e}")

if __name__ == "__main__":
    logging.info("Starting Disk Monitor Service...")
    while True:
        check_all_disks()
        logging.info(f"Check complete. Next check in {CHECK_INTERVAL_SECONDS} seconds.")
        time.sleep(CHECK_INTERVAL_SECONDS)
