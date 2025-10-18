# 🎨 Geometric Pattern Generator (Turtle Graphics)

This Python script uses the **turtle graphics** library to draw beautiful **spiral-like geometric patterns** made of repeating shapes such as triangles, squares, and more.  
Each pattern is drawn in random colors to create colorful, mesmerizing designs.

---

## 🧩 How It Works

- The user is asked to enter:
  1. How many times the cursor should move (i.e., how many shapes to draw)
  2. The number of sides of the shape (for example, 3 = triangle, 4 = square)

- The turtle then:
  - Draws a polygon based on the number of sides.
  - Slightly rotates after each shape to form a **spiral pattern**.
  - Uses **random colors** for each shape.

**Example:**
How many times should the cursor move? 50
Enter the number of sides for the shape (e.g. 3 for triangle, 4 for square etc.): 4

This will create a spiral pattern made of 50 squares.

---

## 🛠️ Prerequisites

- Python 3.x must be installed on your system.
- The `turtle` module is included with Python by default (no need to install separately).
- The `random` module is also built-in.

---

## 🚀 How to Run

1. Save the script (e.g. `pattern.py`) and this `README.md` in the same folder.
2. Open your terminal or command prompt.
3. Run the script using:

   ```bash
   python pattern.py
4. Enter the required inputs.

---

📸 Output

You’ll see a colorful spiral pattern window open.
Try different inputs for number of moves and number of sides to get new designs each time!

Example results:

3 sides → triangle flower pattern 🌺

4 sides → square spiral pattern 🌀

5+ sides → star-like patterns ⭐

---

💡 Tips

* Increase the number of moves for denser, more detailed spirals.
* Try using turtle.bgcolor("white") if you prefer light backgrounds.
* To save the screen, you can take a screenshot after the drawing finishes.

---

Language: Python 🐍
Modules Used: turtle, random

---
