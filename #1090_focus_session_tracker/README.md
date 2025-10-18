# ⏳ Productive Time & Break Tracker CLI

A simple command-line tool to track your productive sessions and breaks with a live countdown timer. Stay focused, manage your time, and review your work/break balance—all from your terminal!

---

## ⚙️ Features

-   Interactive terminal menu
-   Live countdown timer for work and break sessions
-   Stop any session early by pressing ENTER
-   Automatic session logging and summary
-   No external dependencies (uses only Python standard library)
-   Under 100 lines of code

---

## 🚀 Usage

1.  Run the script:

    ```bash
    python focus.py
    ```

2.  Follow the menu prompts:
    - Enter the desired duration (in minutes) for work or break.
    - Watch the countdown timer update in real time.
    - Press ENTER to stop a session early, or let it finish automatically.

---

## 🧠 Example

```
--- Productive Time Tracker ---
1. Start productive time
2. Start break
3. Show summary
4. Exit
Choose an option: 1
Wanted productive time (minutes): 25
Productive time started.
Time left: 0:25:00 (Press ENTER to stop)
... (timer counts down) ...
Time is up!
Productive time recorded: 0:25:00
```

---

## 🧰 Tech

-   **Python 3** (no extra libraries required)

---

## 💡 Notes

This project is great for learning about:
- Terminal input/output
- Countdown timers and time management
- Handling user input asynchronously in the terminal
- Building simple, interactive CLI utilities

---