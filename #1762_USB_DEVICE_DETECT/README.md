# USB Device Detector

This script detects and logs when USB devices are plugged in or removed from the system.

It is cross-platform and supports two different detection methods:
* **Linux:** Uses `pyudev` for real-time, event-based monitoring.
* **Windows:** Uses `WMI` to poll for changes in connected Plug-and-Play (PnP) devices.

All events are logged to the console and to a file named `usb_detector.log`.

## Requirements

-   Python 3.x
-   Platform-specific libraries (see below)

## Installation

1.  **Clone or download** this repository (or just save `usb_detector.py`).

2.  **Install the required Python library** based on your operating system:

    * **On Linux:**
        ```bash
        pip install pyudev
        ```
    * **On Windows:**
        ```bash
        pip install WMI
        ```

## Usage

You must run the script with elevated privileges to allow it to monitor system hardware.

* **On Linux:**
    Run the script with `sudo`.
    ```bash
    sudo python3 usb_detector.py
    ```

* **On Windows:**
    Run your terminal (Command Prompt or PowerShell) as **Administrator**, then run the script.
    ```bash
    python usb_detector.py
    ```

### Log Output

The script will create a `usb_detector.log` file in the same directory. Output will look similar to this: