# Flickering Fire Animation

> A mesmerizing real-time **fire simulation** built with **Python + Pygame** using dynamic color gradients and flickering flame physics.

This project creates a realistic, animated fire effect that continuously flickers and rises upward — just like a campfire. The effect is fully procedural and random, using color intensity and pixel propagation to simulate natural flame motion.

---

## Features

* Realistic flickering flame animation
* Smooth color gradients (red → orange → yellow → white)
* Procedural randomness for natural movement
* Rising flame simulation
* Cross-platform: Works on **Windows**, **macOS**, and **Linux**
* Built using pure Python + Pygame (no extra graphics required)

---

## How It Works

1. **Color Gradient Generation:**
   A palette of 256 RGB colors transitions from **dark red** (cool areas) to **bright white** (hot spots).

2. **Pixel Intensity Simulation:**
   Each pixel holds a heat value (0–255). The base of the fire randomly flickers with high intensities.

3. **Upward Propagation:**
   Each pixel copies brightness from the pixel below, gradually fading to simulate rising flames.

4. **Random Decay:**
   Random decreases in brightness and horizontal drift add a natural flicker effect.

5. **Scaling:**
   The fire is rendered in a low-resolution grid for speed, then smoothly scaled up to fill the screen.

---

## Example Output

When you run the program, a live animation window appears like this:

*Flickering fire rising and glowing dynamically across the screen.*

*(Screenshot not included here — but you’ll see a lively flame effect that changes continuously.)*

---

## Usage

### 1. Clone or Download

Download the file **`fire_animation.py`** to your computer.

### 2. Install Dependencies

Install **Pygame** (required for graphics):

```bash
pip install pygame
```

### 3. Run the Program

Run the script in your terminal or command prompt:

```bash
python fire_animation.py
```

### 4. Exit

Press `ESC` or close the window to quit.

---

## Requirements

| Component    | Version / Details                           |
| ------------ | ------------------------------------------- |
| **Python**   | 3.6 or later                                |
| **Library**  | `pygame` (install via `pip install pygame`) |
| **Platform** | Windows / macOS / Linux                     |

---

## Project Structure

```
fire_animation.py     # Main script containing fire simulation logic
README.md             # Documentation (this file)
```

---
