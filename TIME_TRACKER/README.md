# Break Reminder (Python)

A simple cross-platform Python script that tracks how long your system has been running and reminds you to take a short break every hour.  
Works on **Windows, macOS, and Linux** — no external libraries required.

---

## 🚀 Features
- Tracks system uptime in real time  
- Sends a **notification every hour** to remind you to rest  
- Lightweight and under **100 lines of code**  
- Uses only the **Python standard library**  
- Works silently in the background (optional)

---

## 🧩 Requirements
- **Python 3.8+**
- Works on:
  - Windows 10 / 11  
  - macOS  
  - Linux (with `notify-send`)

---

## 💻 Installation

1. Download or copy the file `break_reminder.py`.
2. Make sure Python is installed and added to PATH.
3. Open a terminal or command prompt.
4. Run the script:

   ```
   python break_reminder.py
   ```

You should see:

```
Break reminder started! You'll get notified every hour.

System on for 0h 5m
```

After an hour of uptime, a notification will appear:
> You’ve been working for an hour! Time to take a short break ☕

---

## ⚙️ Run Silently (Optional)
If you don’t want the console window to stay open:
1. Rename the file to `break_reminder.pyw`.
2. Run it using:
   ```
   pythonw break_reminder.pyw
   ```
3. Or add it to **Task Scheduler** → “Run at logon” for automatic startup.

---

## 🧠 How It Works
- Retrieves system uptime:
  - Windows → `GetTickCount64`
  - Linux → `/proc/uptime`
  - macOS → `sysctl kern.boottime`
- Every 3600 seconds, displays a platform-specific notification.
- Checks uptime every 30 seconds to avoid heavy resource use.

