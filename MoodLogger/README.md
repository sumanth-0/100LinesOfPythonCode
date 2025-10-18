
---

# Daily Mood Logger CLI

A simple command-line interface (CLI) tool to log and track your daily mood, with optional notes and password protection.

---

## Features

* Log your **mood once per day**.
* Update existing entries for today or any past date.
* Optional notes for each mood entry.
* View **full mood history**.
* **Password-protected** using a hidden file in your home directory.
* Cross-platform CLI support using `pwinput` (Windows, Linux, macOS, WSL).
* Retro-style CLI display.

---

## Installation

1. Clone the repository or download the code.
2. Install dependencies:

```bash
pip install pwinput
```

3. Run the program:

```bash
python runner.py
```

---

## Usage

1. On first run, you will be asked to **set a password**.
2. Enter the password on subsequent runs to access the logger.
3. Choose from the menu:

```
Options:
1. Log/update today's mood
2. Log/update past day
3. View all history
```

4. Enter your mood and optional notes.
5. View your full mood history if desired.

---

## File Structure

* `runner.py` — Main CLI script.
* `mood_log.csv` — Automatically created CSV file storing moods.
* `~/.mood_pass` — Hidden file storing your password securely.

---

## Resetting the Password

To reset your password:

1. Locate and **delete the hidden password file**:

```bash
rm ~/.mood_pass
```

2. Run `runner.py` again. The program will prompt you to **create a new password**.

⚠️ **Note:** Deleting this file **does not affect your mood logs** — all past entries in `mood_log.csv` will remain intact.

---

## Notes

* Dates must be entered in `YYYY-MM-DD` format if logging past moods.
* Leaving the date blank defaults to **today**.
* Backspace works while typing passwords.
* Optional notes can be left empty.
* Cross-platform asterisk password entry requires `pwinput`.
