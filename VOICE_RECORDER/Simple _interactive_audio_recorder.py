import sounddevice as sd
import wavio
import os
import time

def list_input_devices():
    try:
        devices = sd.query_devices()
        print("Available audio devices:")
        for i, dev in enumerate(devices):
            print(f"{i}: {dev['name']} (max input channels: {dev.get('max_input_channels', 0)})")
    except Exception as e:
        print("Could not query devices:", e)

def record_audio(duration, filename, samplerate=44100, channels=2, dtype='int16', device=None):
    if not filename.lower().endswith('.wav'):
        filename += '.wav'
    try:
        frames = int(duration * samplerate)
        print(f"Recording for {duration} seconds (samplerate={samplerate}, channels={channels})...")
        start = time.time()
        audio = sd.rec(frames, samplerate=samplerate, channels=channels, dtype=dtype, device=device)
        sd.wait()
        elapsed = time.time() - start
        # Ensure output directory exists
        out_dir = os.path.dirname(os.path.abspath(filename))
        if out_dir and not os.path.exists(out_dir):
            os.makedirs(out_dir, exist_ok=True)
        wavio.write(filename, audio, samplerate, sampwidth=2)
        print(f"Recording saved as '{filename}' ({elapsed:.2f}s)")
    except KeyboardInterrupt:
        print("\nRecording cancelled by user.")
    except Exception as e:
        print("Recording failed:", e)

if __name__ == "__main__":
    try:
        print("Press Enter to see available input devices or type 'skip' to continue with default device.")
        if input().strip().lower() != 'skip':
            list_input_devices()

        device_input = input("Enter device index to use (or press Enter for default): ").strip()
        device = int(device_input) if device_input != '' else None

        record_duration = float(input("Enter duration in seconds: ").strip())
        file_name = input("Enter filename (with or without .wav extension) [default: recording.wav]: ").strip() or "recording.wav"

        sr_input = input("Enter sample rate (default 44100): ").strip()
        samplerate = int(sr_input) if sr_input else 44100

        ch_input = input("Enter number of channels (1=mono,2=stereo) (default 2): ").strip()
        channels = int(ch_input) if ch_input else 2

        record_audio(record_duration, file_name, samplerate=samplerate, channels=channels, device=device)
    except ValueError:
        print("Invalid numeric input. Exiting.")
    except Exception as e:
        print("Error:", e)
