# Maze Generator 

This project provides a simple **ASCII Maze Generator** implemented in Python.  
It uses **recursive backtracking** to generate a random maze and displays it both in the **terminal (ASCII format)** and **graphically using Matplotlib**.

---

##  Features
- Randomized maze generation using recursive backtracking
- Customizable width, height, and random seed
- ASCII-style visualization in the terminal
- Clean visualization using Matplotlib 
- Deterministic output with seed input (or random as per user)

---

##  Requirements

Install dependencies before running the script:
```bash
pip install matplotlib
```

---

##  Usage

Run the script directly from the terminal:
```bash
python maze.py
```

You will be prompted to enter:
- **Width**: number of maze cells horizontally  
- **Height**: number of maze cells vertically  
- **Seed**: integer seed for deterministic generation (`-1` for random maze)

Example:
```bash
Enter width: 10
Enter height: 6
Enter seed or -1 if random: 42
```

---

## Output Example

### ASCII Maze (in terminal)
```
ASCII Maze:

#####################
S   #       #       #
# ####### ### ##### #
#       #     #   # #
####### # ####### # #
#     # #       # # #
# ##### ####### # # #
# #   #   #       # #
# # # ### ######### #
# # #   #     #   # #
# # # ####### # # # #
#   #           #   E
#####################
```

### Matplotlib View
A neatly formatted ASCII maze is displayed in a pop-up matplotlib window for easy visualization.

---

## How It Works

1. The maze is represented as a 2D grid (`1` for wall, `0` for passage).
2. Recursive carving starts from a random odd-indexed cell.
3. Each recursive step randomly picks a direction and carves a passage.
4. An entrance (`S`) and exit (`E`) are added automatically.

---

