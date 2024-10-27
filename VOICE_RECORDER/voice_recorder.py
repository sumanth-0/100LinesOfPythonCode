import sounddevice as sd
import wavio

def record_audio(duration, filename):
    print("Recording...")
    audio = sd.rec(int(duration * 44100), samplerate=44100, channels=2, dtype='int16')
    sd.wait()  # Wait until the recording is finished
    wavio.write(filename, audio, 44100, sampwidth=2)  # Save as WAV file
    print(f"Recording saved as '{filename}'")

if __name__ == "__main__":
    record_duration = float(input("Enter duration in seconds: "))
    file_name = input("Enter filename (with .wav extension): ")
    record_audio(record_duration, file_name)
