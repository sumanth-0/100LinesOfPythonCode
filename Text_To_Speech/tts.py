from gtts import gTTS
import os
from playsound import playsound

def text_to_speech(text):
    """Converts text to speech and plays it."""
    tts = gTTS(text=text, lang='en')
    audio_file = 'output.mp3'
    tts.save(audio_file)
    playsound(audio_file)

def main():
    choice = input("Would you like to input text (t) or a file (f)? ").strip().lower()

    if choice == 't':
        user_input = input("Enter the text to be read aloud: ")
        text_to_speech(user_input)
    elif choice == 'f':
        file_path = input("Enter the path to the text file: ")
        try:
            with open(file_path, 'r') as file:
                text = file.read()
                text_to_speech(text)
        except FileNotFoundError:
            print("File not found. Please check the path and try again.")
    else:
        print("Invalid choice. Please select 't' for text or 'f' for file.")

if __name__ == "__main__":
    main()
