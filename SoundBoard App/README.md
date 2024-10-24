# Soundboard App
This is a simple Python-based soundboard app built using ```bash tkinter``` for the graphical user interface (GUI) and ```bash pygame``` for sound playback. The app allows users to play predefined sound files by clicking buttons and provides an option to load custom sounds.

## Features
* Predefined Sounds: Three buttons to play specific sound files (```bash click.mp3```, ```bash soundone.mp3```, and ```bash soundtwo.mp3```).
* Custom Sound Loader: A button to load and play a custom sound file selected by the user.
* Simple GUI: A basic interface with buttons for easy interaction.

## Requirements
* Python 3.x
* pygame library for sound handling
* tkinter for GUI (comes pre-installed with Python)

## Installation
1. Install Pygame: Install the required pygame library using pip:
```bash
pip install pygame
```
2. Prepare Sound Files: Create a folder named Sounds in the same directory as the Python script, and place your sound files (click.mp3, soundone.mp3, and soundtwo.mp3) in that folder.

## How to Run the App
1. Save the script as soundboard.py in a directory of your choice.
2. Ensure that the required sound files (click.mp3, soundone.mp3, soundtwo.mp3) are placed in the Sounds folder inside the script’s directory.
3. Run the script:
```bash
python soundboard.py
```

## Usage
* Click Button: Plays the sound click.mp3 from the Sounds folder.
* Sound 1 Button: Plays the sound soundone.mp3 from the Sounds folder.
* Sound 2 Button: Plays the sound soundtwo.mp3 from the Sounds folder.
* Load Sound Button: Allows the user to select and play a custom sound file from their system.

## Example Directory Structure
```bash
/your_project_directory
│
├── soundboard.py
└── Sounds
    ├── click.mp3
    ├── soundone.mp3
    └── soundtwo.mp3
```
## Customization
* You can add more buttons for additional predefined sounds by adding more tk.Button widgets in the script.
* Modify the geometry of the window by changing the root.geometry() value to fit your preferences.

## Troubleshooting
* If you encounter any issues with sound not playing, ensure the sound file paths are correct and that the pygame.mixer has been initialized properly.
* If the app cannot find your sound files, verify that the Sounds folder exists and that the sound files are in the correct location.

## License
This project is open-source and available for modification and use in personal projects.