import sounddevice as sd
import soundfile as sf
import customtkinter
import time
import threading
import os

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.geometry("500x300")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=15, padx=60, fill="both", expand=True)

running, startTime, hasRun = False, 0, False

if not os.path.exists("recordings"):
    os.makedirs("recordings")


def record_audio_until_stop():
    audio_data, rate = [], 44100  # List to safe audio data, sample rate
    while running:
        # Recording block for 1 second
        block = sd.rec(int(rate), samplerate=rate, channels=1)
        sd.wait()
        audio_data.extend(block)

    current_time = time.localtime()
    formatted_time = os.path.join("recordings", time.strftime("%d.%m.%Y-%H-%M-%S", current_time) + ".wav")
    try:
        sf.write(formatted_time, audio_data, rate)
        print("Recording finished and saved to", formatted_time)
    except Exception as e:
        print(f"Error saving audio file: {e}")


def update_timer():
    if running:
        elapsed_time = time.time() - startTime  # Berechne die verstrichene Zeit
        timerLabel.configure(text=f"{elapsed_time:.1f} Sekunden")  # Aktualisiere das Label
        root.after(100, update_timer)  # Aktualisiere alle 100 Millisekunden


def start():
    global startButton, stopButton, textField, startTime, running, timerLabel, hasRun
    if hasRun:
        timerLabel.pack_forget()
    startButton.pack_forget()
    textField.pack_forget()
    running, startTime, hasRun = True, time.time(), True
    update_timer()
    timerLabel.pack(pady=10, padx=10)
    stopButton.pack(pady=12, padx=10)
    t1 = threading.Thread(target=record_audio_until_stop)
    t1.start()


def stop():
    global startButton, stopButton, textField, running
    running = False
    stopButton.pack_forget()
    textField.pack(pady=12, padx=10)
    startButton.pack(pady=12, padx=10)

def open_folder():
    try:
        os.startfile(os.path.join(os.getcwd(), "recordings"))
    except AttributeError:
        os.system(f'open "{os.path.join(os.getcwd(), "recordings")}"')
    except Exception as e:
        print(f"Could not open folder: {e}")


label = customtkinter.CTkLabel(master=frame, text="Voice Recorder")
label.pack(pady=12, padx=10)

startButton = customtkinter.CTkButton(master=frame, text="Start", fg_color="green", hover_color="darkgreen",
                                      command=start)
startButton.pack(pady=12, padx=10)

openFolderButton = customtkinter.CTkButton(master=frame, text="Open Folder", command=open_folder)
openFolderButton.pack(pady=10, padx=10, side="bottom")

stopButton = customtkinter.CTkButton(master=frame, text="Stop", fg_color="red", hover_color="darkred", command=stop)
textField = customtkinter.CTkLabel(master=frame, text="Saved audio file")
timerLabel = customtkinter.CTkLabel(master=frame, text="0.0 Sekunden")

root.mainloop()
