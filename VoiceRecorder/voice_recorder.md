# Voice Recorder

This Python program provides a simple voice recording application with a graphical user interface (GUI) built using the customtkinter library. The program allows users to start and stop recordings, view the duration of the recording in real-time, and save the audio files in a designated "recordings" folder. Users can also open the folder where recordings are stored directly from the application.

## Features
- Start and stop audio recordings with a button click.
- Display recording duration in real-time.
- Save audio files in .wav format in a "recordings" folder.
- Open the folder containing recordings directly from the application.

## How It Works

### Components

**Audio Recording:**
- The program utilizes the `sounddevice` library to record audio in real time.
- Recorded audio is stored in memory until the user stops the recording.
- Upon stopping, the audio data is saved as a .wav file, named with a timestamp for easy identification.

**Timer Display:**
- A timer is displayed on the interface, updating every 100 milliseconds to show the recording duration.
- The timer resets each time a new recording is started.

**Open Folder Button:**
- The application includes a button to open the folder where audio recordings are saved.
- This folder is automatically created in the application's root directory if it does not exist.

## User Interface

The program uses `customtkinter` to create a modern and visually appealing GUI with the following components:
- **Voice Recorder Label:** Title label displayed at the top of the window.
- **Start Button:** Initiates audio recording and starts the timer.
- **Stop Button:** Stops recording, saves the audio, and resets the timer.
- **Open Folder Button:** Opens the "recordings" folder, allowing users to access saved audio files.
- **Timer Display:** Displays the duration of the current recording in seconds.

## Requirements
- Python 3.x
- `sounddevice` library for recording audio (`pip install sounddevice`)
- `soundfile` library for saving audio files (`pip install soundfile`)
- `customtkinter` library for the GUI (`pip install customtkinter`)

## How to Run
1. Install the required libraries if they are not already installed:
   ```bash
   pip install sounddevice soundfile customtkinter
   
2. Run the program by executing the Python script in the terminal:
    ```bash
    python voice_recorder.py