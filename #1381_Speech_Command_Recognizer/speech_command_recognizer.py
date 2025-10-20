"""
Speech Command Recognizer (#1381)
Detects simple voice commands: 'start', 'stop', 'exit'.
Responds with text-to-speech and console messages.
"""

import speech_recognition as sr
import pyttsx3

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen to microphone and return recognized text."""
    with sr.Microphone() as source:
        print("\nListening for command...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio).lower()
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Could not understand audio.")
            return ""
        except sr.RequestError:
            print("Speech Recognition service unavailable.")
            return ""

def main():
    speak("Voice command recognizer activated. Say start, stop, or exit.")
    print("Say 'start', 'stop', or 'exit' to control the program.")
    
    while True:
        command = listen()

        if "start" in command:
            speak("Starting process.")
            print("✅ Process started!")

        elif "stop" in command:
            speak("Stopping process.")
            print("⏹️ Process stopped!")

        elif "exit" in command:
            speak("Exiting. Goodbye!")
            print("👋 Program exited.")
            break

        else:
            print("No valid command detected. Try again.")

if __name__ == "__main__":
    main()
