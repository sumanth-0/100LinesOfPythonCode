# 🕰️ Focus Timer CLI

A simple, zero-dependency terminal timer to help you focus.

---

### What is this?

This is a lightweight Python script that runs in your terminal. It helps you track work sessions and breaks, showing you how much productive time you've logged when you're done. No distractions, no fancy UI, just pure focus.

### Core Features

* ** Focus Mode**: Set a timer for deep work.
* ** Break Mode**: Set a timer for a quick break.
* ** Time Summary**: Shows your total focused time at the end.
* ** Keyboard Control**: Simple `f`, `b`, `q` commands.
* ** No Installation**: Just needs Python 3.

---

### Get Started

1.  **Save the Code**: Save the script on your computer as `focus.py`.

2.  **Run it from your terminal**:
    ```sh
    python3 focus.py
    ```

---

### How It Works

The interface is minimal. You're asked for an action, then the time in minutes.

> ```
> --- Focus & Break Timer ---
>
> Action? (f)ocus, (b)reak, (q)uit: f
> Enter duration for Focus (minutes): 25
> Focus: 24:59 
> ```
>
> When the timer finishes, it will ask for your next action. When you're ready to finish your work session:
>
> ```
> Action? (f)ocus, (b)reak, (q)uit: q
>
> --------------------------
> Total Productive Time: 0:25:00
> Goodbye.
> ```

---
*License: MIT*