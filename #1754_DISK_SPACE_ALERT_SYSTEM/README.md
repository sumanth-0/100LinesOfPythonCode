# Disk Space Alert System

A simple, cross-platform Python script that monitors disk space on all connected drives and sends a native desktop notification if any drive's usage exceeds a set threshold.

## Features

-   **Monitors All Drives:** Automatically discovers and checks all physical disk partitions (e.g., C:\, D:\ on Windows; / , /home on Linux).
-   **Desktop Alerts:** Uses `plyer` to send native desktop notifications on Windows, macOS, and Linux.
-   **Logging:** Logs all checks and alerts to a `disk_monitor.log` file for review.
-   **Configurable:** Easily set the usage threshold and check frequency.
-   **Lightweight:** Runs in the background with minimal resource usage.

## Requirements

-   Python 3.x
-   `psutil` library
-   `plyer` library

## Installation

1.  **Clone or download** this repository (or just save `disk_monitor.py`).

2.  **Install the required Python libraries** using pip:
    ```bash
    pip install psutil plyer
    ```

## Configuration

Open the `disk_monitor.py` file in a text editor and modify the configuration section at the top:

```python
# --- Configuration ---
# Set the disk usage percentage threshold (e.g., 80%)
THRESHOLD_PERCENT = 80

# How often to check (in seconds)
CHECK_INTERVAL_SECONDS = 600  # 10 minutes
# ---------------------