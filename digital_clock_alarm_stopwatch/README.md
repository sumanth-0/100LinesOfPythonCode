# Digital Clock, Alarm & Stopwatch ⏰

### 📌 Overview
This is a simple **terminal-based Python project** that combines:
1. 🕒 **Clock** — Displays the current system time.
2. ⏰ **Alarm** — Lets you set a custom alarm time.
3. ⏳ **Stopwatch** — Counts elapsed time in HH:MM:SS format.

All features are implemented in a single file under **100 lines**, following open-source contribution guidelines.

---

### ⚙️ Features
- Works completely in the **terminal** (no GUI or external modules).
- Cross-platform: runs on **Windows, macOS, and Linux**.
- Clean menu with user-friendly navigation.
- Uses **match-case** (Python 3.10+).

---

### ▶️ How to Run
1. Open the terminal and navigate to the folder containing the file.
2. Run the following command:
   ```bash
   python clock_alarm_stopwatch.py

🧠 Code Logic Summary

clear() → clears the console output for a fresh display.

show_clock() → shows real-time system clock.

set_alarm() → triggers a simple text-based alarm at the set time.

stopwatch() → counts time until manually stopped.

main() → provides a menu and controls program flow.