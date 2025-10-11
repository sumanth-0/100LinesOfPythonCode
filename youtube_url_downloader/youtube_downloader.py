"""
YouTube Video Downloader (Robust Version)
- Download video or audio using pytube
- Handles common YouTube errors and retry mechanism
"""

import os
import time

try:
    from pytube import YouTube
except ImportError:
    print("pytube not installed. Install it with 'pip install pytube'")
    exit()

# Downloads folder in current directory
DOWNLOAD_FOLDER = os.path.join(os.getcwd(), "downloads")
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

def fetch_video(url, retries=3):
    """
    Fetch YouTube object with retry mechanism
    """
    for attempt in range(retries):
        try:
            yt = YouTube(url)
            return yt
        except Exception as e:
            print(f"⚠️ Attempt {attempt+1} failed: {e}")
            time.sleep(1)
    print("❌ Failed to fetch video info. Check URL or update pytube.")
    return None

def download_video(url):
    yt = fetch_video(url)
    if not yt:
        return
    print(f"\n🎥 Video Title: {yt.title}")
    choice = input("Download as (v)ideo or (a)udio? [v/a]: ").strip().lower()
    
    if choice == "v":
        try:
            stream = yt.streams.get_highest_resolution()
            print(f"Downloading video to {DOWNLOAD_FOLDER} ...")
            stream.download(DOWNLOAD_FOLDER)
            print("✅ Video downloaded successfully!")
        except Exception as e:
            print("❌ Download failed:", e)
    elif choice == "a":
        try:
            stream = yt.streams.filter(only_audio=True).first()
            out_file = stream.download(DOWNLOAD_FOLDER)
            base, ext = os.path.splitext(out_file)
            new_file = base + ".mp3"
            os.rename(out_file, new_file)
            print(f"✅ Audio downloaded successfully as {new_file}")
        except Exception as e:
            print("❌ Audio download failed:", e)
    else:
        print("Invalid choice. Cancelled.")

def main():
    print("\n📥 YouTube Video Downloader")
    while True:
        print("\nMenu:")
        print("1️⃣  Download YouTube Video/Audio")
        print("2️⃣  Exit")
        choice = input("Choose an option (1-2): ").strip()
        if choice == "1":
            url = input("Enter YouTube video URL: ").strip()
            if url:
                download_video(url)
            else:
                print("URL cannot be empty.")
        elif choice == "2":
            print("Goodbye! 🎬")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
