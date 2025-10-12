from datetime import datetime
import time
from pathlib import Path
import signal
import sys

import pygame

# --- Config ---
SOUND_FILE = r"alarm_clock_mp3/alarm-clock-90867.mp3"
RING_SECONDS = 60

try:
    import msvcrt
    HAS_MSVCRT = True
except Exception:
    HAS_MSVCRT = False

def init_audio():
    pygame.mixer.quit()
    pygame.mixer.init(frequency=44100)
    if not pygame.get_init():
        pygame.init()

def stop_audio():
    try:
        pygame.mixer.music.stop()
    except Exception:
        pass
    try:
        pygame.mixer.quit()
    except Exception:
        pass

def sigint_handler(sig, frame):
    print("\nInterrupted. Stopping...")
    stop_audio()
    sys.exit(0)

signal.signal(signal.SIGINT, sigint_handler)

def play_alarm(path: Path, seconds: int):
    init_audio()
    pygame.mixer.music.load(str(path))
    pygame.mixer.music.play(loops=-1)
    t0 = time.time()
    try:
        while True:
            elapsed = time.time() - t0
            remaining = max(0, int(seconds - elapsed))
            print(f"\r🔔 Ringing... {remaining:02d}s left  (Press any key or Ctrl+C to stop)", end="", flush=True)
            if elapsed >= seconds:
                break
            if HAS_MSVCRT and msvcrt.kbhit():
                _ = msvcrt.getwch()
                print("\nStopped by user.")
                break
            time.sleep(0.05)
    except KeyboardInterrupt:
        print("\nInterrupted. Stopping...")
    finally:
        stop_audio()
        print("\nAlarm ended.")

def ring_for_60s():
    path = Path(SOUND_FILE) if Path(SOUND_FILE).is_absolute() else Path(__file__).resolve().parent / SOUND_FILE
    if not path.exists():
        print(f"Sound file not found: {path}")
        return
    print("Wake Up! (ringing 60s)")
    try:
        play_alarm(path, RING_SECONDS)
    except Exception as e:
        print(f"\nPlayback error: {e}")

def set_alarm():
    while True:
        s = input("Enter alarm time (HH:MM:SS): ")
        try:
            h, m, sec = map(int, s.split(":"))
            if not (0 <= h < 24 and 0 <= m < 60 and 0 <= sec < 60):
                raise ValueError
            break
        except ValueError:
            print("Invalid time. Try again (e.g. 07:30:00)")
    print(f"Alarm set for {s}")
    try:
        while True:
            now = datetime.now()
            if now.hour == h and now.minute == m and now.second == sec:
                ring_for_60s()
                break
            time.sleep(0.2)
    except KeyboardInterrupt:
        print("\nCanceled before alarm.")

if __name__ == "__main__":
    set_alarm()
