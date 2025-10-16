"""
Desktop Reminder Pop-up
Author: Diya Satish Kumar
A simple Tkinter app to set a timed reminder that pops up after a delay,
optionally playing a short beep sound before displaying.
"""
import time
import threading
import tkinter as tk
from tkinter import messagebox
import os
import platform

def play_sound():
    """Play a short beep sound (works on macOS, Windows, Linux)."""
    system_name = platform.system()
    if system_name == "Windows":
        import winsound
        winsound.Beep(1000, 500)  # frequency, duration(ms)
    elif system_name == "Darwin":          # macOS
        os.system('say "Reminder"')
    else:                                  # Linux / others
        os.system('echo -e "\a"')

def show_popup(reminder, sound_on=True):
    """Create a reminder pop-up window."""
    if sound_on:
        play_sound()
    popup = tk.Tk()
    popup.title("🕒 Reminder!")
    popup.geometry("300x150")
    popup.resizable(False, False)

    tk.Label(
        popup,
        text=reminder,
        font=("Helvetica", 12),
        wraplength=250,
        justify="center"
    ).pack(pady=20)

    tk.Button(popup, text="Dismiss", command=popup.destroy).pack(pady=10)
    popup.mainloop()
def set_reminder(message, delay, sound_on=True):
    """Wait for delay seconds, then show popup."""
    time.sleep(delay)
    show_popup(message, sound_on)
def main():
    print("🕒 DESKTOP REMINDER POP-UP 🕒")
    message = input("Enter reminder message: ").strip()
    if not message:
        print("⚠️ No message entered. Exiting.")
        return
    try:
        delay = float(input("Enter time (in minutes): ")) * 60
    except ValueError:
        print("⚠️ Invalid input. Please enter a number.")
        return

    sound_choice = input("Enable sound alert? (y/n): ").strip().lower()
    sound_on = sound_choice != "n"

    print("✅ Reminder set!")
    threading.Thread(
        target=set_reminder, args=(message, delay, sound_on), daemon=True
    ).start()
if __name__ == "__main__":
    main()