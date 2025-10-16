#!/usr/bin/env python3
"""
Mini terminal Task Manager: shows live CPU and RAM usage updates every second.

"""

import time
import shutil
import psutil
import sys
import signal

# Graceful exit on Ctrl-C
def handle_sigint(signum, frame):
    print("\nExiting...")  # newline to move past current line
    sys.exit(0)

signal.signal(signal.SIGINT, handle_sigint)

def make_bar(pct: float, width: int) -> str:
    """
    Return an ASCII horizontal progress bar for percentage pct (0-100)
    width: total width of the bar (characters)
    """
    pct = max(0.0, min(100.0, pct))
    filled = int((pct / 100.0) * width)
    empty = width - filled
    return "█" * filled + " " * empty  # filled block + spaces

def clear_terminal():
    """Clear terminal in a cross-platform way."""
    # ANSI clear screen + move cursor to top-left
    print("\033[2J\033[H", end="")

def human_size(bytes_num: int) -> str:
    """Simple human-readable bytes -> MB/GB string."""
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if bytes_num < 1024:
            return f"{bytes_num:.1f}{unit}"
        bytes_num /= 1024
    return f"{bytes_num:.1f}PB"

def main(refresh_interval: float = 1.0):
    # Warm up CPU percent so first reading is meaningful
    psutil.cpu_percent(interval=0.1)

    while True:
        # Get terminal width to size bars
        term_width = shutil.get_terminal_size((80, 20)).columns
        # Reserve space for labels; bar width is rest (clamped)
        label_space = 30
        bar_width = max(10, term_width - label_space)

        # Fetch metrics
        cpu_pct = psutil.cpu_percent(interval=0.1)  # gives percent over 0.1s sampling
        mem = psutil.virtual_memory()               # returns usage stats
        mem_pct = mem.percent
        used = human_size(mem.used)
        total = human_size(mem.total)

        # Build lines
        cpu_line = f"CPU : {cpu_pct:5.1f}% |{make_bar(cpu_pct, bar_width)}|"
        mem_line = f"RAM : {mem_pct:5.1f}% |{make_bar(mem_pct, bar_width)}|  {used} / {total}"

        
        show_per_core = True #will enable per-core bars
        per_core_lines = []
        if show_per_core:
            per_core = psutil.cpu_percent(interval=0.0, percpu=True)
            for i, p in enumerate(per_core):
                per_core_lines.append(f"core{i:02d}: {p:5.1f}% |{make_bar(p, 20)}|")

        # Print (clear then print)
        clear_terminal()
        print("Mini Task Manager — updates every second. Press Ctrl-C to quit.\n")
        print(cpu_line)
        print(mem_line)
        if show_per_core:
            print()
            for pl in per_core_lines:
                print(pl)

        # Sleep for remaining time (we already spent ~0.1s sampling)
        time.sleep(max(0.0, refresh_interval - 0.1))

if __name__ == "__main__":
    main(refresh_interval=1.0)
