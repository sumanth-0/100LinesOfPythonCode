# Recursive Circle Packer (Python + Pygame)

A **visual generative art tool** that creates **non-overlapping, colorful circles** packed within a canvas using a recursive growth algorithm.  
Each circle grows until it touches another circle or the edge of the canvas, producing intricate and organic patterns.

---

## Features

- 🌈 Generates **vivid, colorful circles** with random hues  
- 🔄 **Automatic circle packing** to maximize canvas coverage  
- ⬆️ Adjustable **maximum number of circles** and **attempts per circle**  
- 🖥️ Real-time **interactive regeneration** using the SPACE key  
- 💻 Built with **Python** and **Pygame**

---

## How It Works

1. Randomly selects a position on the canvas.  
2. Checks for overlap with existing circles or screen edges.  
3. Grows the circle gradually until it touches another circle or the canvas boundary.  
4. Repeats the process until the maximum number of circles or attempts is reached.  

This creates dense, organic circle packing patterns reminiscent of bubble clusters or abstract cellular structures.

---

## Controls

- **SPACE key:** Regenerate the circle packing pattern  
- **Close window:** Exit the program  

---

## Requirements

- Python 3.6+  
- Pygame (`pip install pygame`)  

---

## Customization

You can modify these constants in the script:

- `WIDTH`, `HEIGHT` → Canvas dimensions  
- `BACKGROUND_COLOR` → Canvas background color  
- `MAX_CIRCLES` → Maximum number of circles per generation  
- `MAX_ATTEMPTS` → Maximum attempts to place circles (affects density)  

---

This project is perfect for **generative art enthusiasts, creative coding experiments, and procedural visualizations**.
