# Digital Waterfall (Matrix-Style Animation)

This project is a **Matrix-inspired digital waterfall animation** implemented in Python using `pygame`. The animation features streams of characters falling down the screen with glowing heads, reminiscent of the iconic visual from the *Matrix* movie series.

## Features

- **Random Character Streams:** Streams of alphanumeric and special characters fall from the top of the screen.  
- **Glowing Heads:** The leading character of each stream is highlighted for a dynamic effect.  
- **Variable Speeds & Lengths:** Each stream moves at a different speed and length to create a natural flowing effect.  
- **Interactive & Lightweight:** Runs smoothly at 30 FPS with adjustable parameters.

## How It Works

1. **Grid-Based Layout:** The screen is divided into columns based on the font size. Each column may spawn a stream.  
2. **Stream Logic:** Each stream keeps track of its vertical position, length, speed, and character list.  
3. **Animation:** Characters are updated every frame, and new streams spawn randomly. Characters also change randomly to simulate a flowing effect.  
4. **Rendering:** Uses `pygame`'s font rendering to draw colored text on the screen.  

## Controls

- Close the window to exit the program.

## Requirements

- Python 3.6 or higher  
- `pygame` (`pip install pygame`)  

## Customization

- **FONT_SIZE:** Change the size of the characters.  
- **FALL_SPEED:** Adjust the speed at which streams fall.  
- **SPAWN_CHANCE:** Control the likelihood of new streams spawning.  
- **CHARS:** Customize the set of characters used in the streams.  
- **COLORS:** Modify `STREAM_COLOR` and `HEAD_COLOR` for different visual effects.  
