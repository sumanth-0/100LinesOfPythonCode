# 🌀 Python Kaleidoscope

A mesmerizing interactive **kaleidoscope drawing app** built with **Pygame**.  
Move your mouse to draw, and watch your strokes repeat symmetrically to create beautiful geometric patterns!

---

## ✨ Features

- **Real-time drawing:** Click and drag your mouse to draw lines.
- **Kaleidoscopic symmetry:** Your strokes are mirrored and rotated into multiple symmetric wedges.
- **Color cycling:** The hue smoothly shifts as you draw, creating vivid rainbow trails.
- **Dynamic clearing:** Press **`C`** to clear the canvas and start over.
- **Simple controls:** Easy to play with and tweak symmetry or colors.

---

## 🧠 How It Works

The screen is divided into several symmetric wedges (default: **6**).  
Each stroke you draw is mirrored and rotated across these wedges to simulate a kaleidoscope effect.

Core ideas:
- The drawing is relative to the **center of the screen**.
- Each stroke is rotated using `math.cos()` and `math.sin()` transformations.
- Mirrored copies are drawn by inverting the y-coordinate.
- The **HSL color space** is used to smoothly cycle through hues while drawing.

---

## 🕹️ Controls

| Action | Description |
|--------|--------------|
| **Left Mouse Button** | Draw lines |
| **C** | Clear canvas |
| **ESC** | Exit program |
| **Mouse Movement (while holding click)** | Draw symmetrical patterns |

---

## ⚙️ Configuration

You can tweak some variables in the script to change the kaleidoscope behavior:

| Variable | Default | Description |
|-----------|----------|-------------|
| `WIDTH`, `HEIGHT` | `800, 800` | Canvas size |
| `SYMMETRY` | `6` | Number of kaleidoscope wedges |
| `LINE_WIDTH` | `2` | Thickness of drawn lines |
| `BACKGROUND_COLOR` | `(10, 10, 20)` | Dark blue background color |

---
