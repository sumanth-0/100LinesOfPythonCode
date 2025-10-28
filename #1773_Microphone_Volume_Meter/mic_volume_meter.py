"""
mic_volume_meter.py
Simple real-time microphone volume meter (issue #1773).
Dependencies: sounddevice, numpy
Run: python mic_volume_meter.py
"""

import sys
import queue
import numpy as np
import sounddevice as sd

SAMPLE_RATE = 44100
BLOCKSIZE = 1024
q = queue.Queue()

def audio_callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    # compute per-block amplitude (RMS-like)
    amp = np.sqrt(np.mean(indata**2))
    q.put(amp)

def meter_bar(level, width=40):
    level = max(0.0, min(level, 1.0))
    filled = int(level * width)
    return "[" + "#" * filled + "-" * (width - filled) + "]"

def main():
    print("Starting microphone volume meter — press Ctrl+C to stop")
    with sd.InputStream(channels=1, callback=audio_callback,
                        samplerate=SAMPLE_RATE, blocksize=BLOCKSIZE):
        try:
            while True:
                try:
                    amp = q.get(timeout=1.0)
                except queue.Empty:
                    continue
                # simple normalization (tweak multiplier for sensitivity)
                norm = amp * 10.0
                if norm > 1.0:
                    norm = 1.0
                print(f"\r{meter_bar(norm)} {norm:.2f}", end="", flush=True)
        except KeyboardInterrupt:
            print("\nStopped.")

if __name__ == "__main__":
    main()
