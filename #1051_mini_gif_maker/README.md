# Simple GIF Maker

A small Tkinter-based GUI application to create animated GIFs from image files.

This repository contains a simple desktop app that lets you add images, reorder them, set frame duration and loop count, and export the result as an animated GIF.

Features
- Add multiple image files (PNG, JPEG, BMP).
- Reorder frames (move up/down) and remove selected frames.
- Set frame duration (milliseconds) and loop count (0 = infinite).
- Export to an animated GIF.

Dependencies
- Python 3.8+ (tested with 3.10+)
- Pillow (PIL) for image processing
- tkinter (part of the Python standard library, may need platform-specific installation)

Installation
1. Create a virtual environment (recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
python3 -m pip install -r requirements.txt
```

Running the app

```bash
python3 main.py
```

A small window will open. Click 'Add Images' to select your files, rearrange or remove frames as needed, adjust the duration and looping options, then click 'Save GIF' to export your animation.

