# ⏰ Python Alarm Clock

A simple and elegant alarm clock script written in Python.  
You can set a specific time in `HH:MM:SS` format, and it will play an MP3 alarm sound for **60 seconds** when the time is reached.

---

## 🚀 Features

- Set an alarm using a simple console input.
- Plays any MP3 sound for 60 seconds using `pygame`.
- Optionally press any key to stop the alarm early (Windows).
- Displays a countdown while ringing.

---

## 🧩 Requirements

- Python **3.8+**
- `pygame` (for MP3 playback)

---

## 📦 Installation

1. Clone or download this repository.

2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. 
    Place your alarm sound file (e.g., alarm-clock-90867.mp3) anywhere on your computer and update the SOUND_FILE path in the script:
    
        SOUND_FILE = r"C:/Users/Downloads/alarm-clock-90867.mp3"

  Default alarm sound file is given.

4. ▶️ Usage

    Run the script:

        python alarm_clock.py

    Enter the time when prompted:

        Enter alarm time (HH:MM:SS): 07:30:00

    At the specified time, the alarm will ring for 60 seconds.

    During playback:

        Press any key to stop the alarm early (Windows).

        Or press Ctrl + C to exit cleanly.

5. ⚙️ Configuration

    You can adjust these constants at the top of the script:

        SOUND_FILE = r"C:/path/to/your/sound.mp3"

        RING_SECONDS = 60  # duration in seconds

🧠 Notes

- If your MP3 doesn’t play, try re-saving it with a tool like Audacity or ffmpeg:

        ffmpeg -i old.mp3 -acodec libmp3lame -ar 44100 new.mp3


- Works best on Windows with local MP3 files.

- For macOS/Linux, you can use python-vlc instead of pygame.

6. 📸 Example Output

        pygame 2.6.1 (SDL 2.28.4, Python 3.13.0)
        Hello from the pygame community. https://www.pygame.org/contribute.html
        Enter alarm time (HH:MM:SS): 00:15:00
        Alarm set for 00:15:00
        Wake Up! (ringing 60s)
        🔔 Ringing... 58s left  (Press any key or Ctrl+C to stop)


🧾 License

MIT License © 2025 Parth Kandharkar