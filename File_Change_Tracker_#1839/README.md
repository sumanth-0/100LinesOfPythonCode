# Folder Activity Monitor

> A Python script that **monitors a folder in real-time** and logs whenever files are **added**, **deleted**, or **modified**.

Ideal for developers, system admins, or anyone who wants to **track file system changes** automatically.

---

## Features

* Real-time monitoring of a folder
* Detects file **creation**, **deletion**, and **modification**
* Automatically logs all events with timestamps
* Saves logs to a file: `folder_activity.log`
* Works on **Windows**, **macOS**, and **Linux**
* Lightweight — only requires the `watchdog` library

---

## Example Log Output

When you add, remove, or modify files, a log entry is created automatically:

```
2025-10-31 10:42:11 - File created: /Users/Downloads/photo.jpg
2025-10-31 10:43:08 - File modified: /Users/Downloads/report.pdf
2025-10-31 10:44:22 - File deleted: /Users/Downloads/old_notes.txt
```

---

## How It Works

1. Monitors a target folder using the [`watchdog`](https://pypi.org/project/watchdog/) library.
2. Detects three types of file system events:

   * **Created**
   * **Deleted**
   * **Modified**
3. Records each event with a timestamp in a log file named `folder_activity.log`.
4. Runs continuously until manually stopped with **Ctrl + C**.

---

## Usage

### 1. Clone or Download the Script

Download or copy `folder_monitor.py` to your computer.

### 2. Install the Required Library

Use `pip` to install the `watchdog` library:

```bash
pip install watchdog
```

### 3. Run the Script

Open a terminal or command prompt and execute:

```bash
python folder_monitor.py
```

You’ll be prompted to enter the folder you want to monitor.
If you press Enter without typing anything, it defaults to your **Downloads** folder.

```
=== Folder Activity Monitor ===
Enter the folder path to monitor [/Users/deepak/Downloads]:
```

### 4. View the Log File

All activity is logged in `folder_activity.log` in the same directory as the script.

---

## Configuration

| Option                | Description                                                               |
| --------------------- | ------------------------------------------------------------------------- |
| **Folder to Monitor** | Any valid directory path. Defaults to the user's `Downloads` folder.      |
| **Recursive**         | Set `recursive=True` in the script to monitor subfolders.                 |
| **Log File**          | Automatically created as `folder_activity.log` in the script’s directory. |

---

## Notes

* The script only tracks **file-level changes** by default (not folders).
* Press **Ctrl + C** to stop monitoring gracefully.
* Ensure you have read/write permissions for the folder you monitor.
* For performance, avoid using it on extremely large folders with thousands of files.

---
