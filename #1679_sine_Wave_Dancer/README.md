# Dancing Sine Wave Animation

A simple Python program using `pygame` to create a **moving sine wave with dancing dots**. The dots follow a sine wave and exhibit subtle random vertical movements, giving a lively "dancing" effect.

## Features

- Animated sine wave with moving dots.
- Dots have slight vertical offsets for a dancing effect.
- Adjustable parameters: amplitude, frequency, speed, number of dots, colors.
- Smooth 60 FPS animation.

## How It Works

1. Dots are evenly spaced along the x-axis of the screen.
2. Y-position of each dot is calculated using a sine function with a time-based offset for horizontal motion.
3. Random vertical offsets are added to each dot for the dancing effect.
4. `pygame` renders the dots on a dark background.

## Parameters

- `AMPLITUDE` – wave height.  
- `FREQUENCY` – number of waves across the screen.  
- `SPEED` – horizontal movement speed.  
- `NUM_DOTS` – number of dots along the wave.  
- `DOT_RADIUS` – size of each dot.  
- `BG_COLOR` and `DOT_COLOR` – customize colors.

## Requirements

- Python 3.6+  
- `pygame` (`pip install pygame`)