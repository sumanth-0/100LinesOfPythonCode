import platform
import time
import logging
try:
    # For Linux
    import pyudev
    LINUX_READY = True
except ImportError:
    LINUX_READY = False
try:
    # For Windows
    import wmi
    WINDOWS_READY = True
except ImportError:
    WINDOWS_READY = False
# -----------------------------------
# --- Configuration ---
# How often to check for changes (in seconds) on Windows.
# Linux uses real-time events, so this is ignored.
POLL_INTERVAL_SECONDS = 2
# ---------------------
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler("usb_detector.log"),
                              logging.StreamHandler()])

def monitor_linux():
    """Uses pyudev to listen for real-time USB events on Linux."""
    logging.info("Starting Linux USB monitor (using pyudev)...")
    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)
    monitor.filter_by(subsystem='usb')

    logging.info("Monitor started. Waiting for events...")
    for device in iter(monitor.poll, None):
        if device.action == 'add':
            logging.info(f"USB Device ADDED: {device.get('ID_MODEL', 'Unknown')} (Vendor: {device.get('ID_VENDOR_ID', 'N/A')})")
        elif device.action == 'remove':
            logging.info(f"USB Device REMOVED: {device.get('ID_MODEL', 'Unknown')} (Vendor: {device.get('ID_VENDOR_ID', 'N/A')})")

def monitor_windows():
    """Uses WMI to poll for USB device changes on Windows."""
    logging.info(f"Starting Windows USB monitor (polling every {POLL_INTERVAL_SECONDS}s)...")
    c = wmi.WMI()
    
    # Get initial set of USB PnP devices
    initial_devices_map = {d.DeviceID: d.Name for d in c.Win32_PnPEntity() if "USB" in (d.Description or "")}
    while True:
        try:
            # Get current set of devices
            current_devices_map = {d.DeviceID: d.Name for d in c.Win32_PnPEntity() if "USB" in (d.Description or "")}
            
            current_ids = set(current_devices_map.keys())
            initial_ids = set(initial_devices_map.keys())

            # Check for added devices
            added_ids = current_ids - initial_ids
            if added_ids:
                for dev_id in added_ids:
                    logging.info(f"USB Device ADDED: {current_devices_map[dev_id]} (ID: {dev_id})")

            # Check for removed devices
            removed_ids = initial_ids - current_ids
            if removed_ids:
                for dev_id in removed_ids:
                    logging.info(f"USB Device REMOVED: {initial_devices_map[dev_id]} (ID: {dev_id})")

            # Update the initial state
            initial_devices_map = current_devices_map
            
        except Exception as e:
            logging.error(f"Error during WMI poll: {e}")
        
        time.sleep(POLL_INTERVAL_SECONDS)
if __name__ == "__main__":
    system = platform.system()
    
    if system == "Linux":
        if not LINUX_READY:
            logging.error("Linux detected, but 'pyudev' library is not installed.")
            logging.error("Please run: pip install pyudev")
        else:
            logging.info("Linux detected. Requires 'sudo' to run.")
            try:
                monitor_linux()
            except Exception as e:
                logging.critical(f"Failed to run Linux monitor. Did you run with 'sudo'? Error: {e}")
                
    elif system == "Windows":
        if not WINDOWS_READY:
            logging.error("Windows detected, but 'WMI' library is not installed.")
            logging.error("Please run: pip install WMI")
        else:
            logging.info("Windows detected. May require 'Administrator' privileges.")
            monitor_windows()
            
    else:
        logging.warning(f"Unsupported platform: {system}. This script only supports Linux and Windows.")