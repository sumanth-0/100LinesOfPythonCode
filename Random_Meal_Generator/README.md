
# Meal Selector CLI Tool

A command-line tool to help you decide what to eat today! This program randomly selects an appetizer, main course, and dessert from a variety of options and displays them in a visually appealing format. Perfect for those indecisive moments when you’re unsure what to eat.

---

## Features

- **Randomized Meal Selection**: The tool picks a random appetizer, main course, and dessert from predefined lists, offering a unique combination each time.
- **Colorful Output**: Using the `colorama` library, the output is formatted with color, making the meal suggestion visually appealing..
- **Cross-Platform Compatibility**: Works on Windows, Mac, and Linux, thanks to `colorama`.

## Sample Output

```
========Today's Meal Suggestion========
Appetizer: Garlic Bread
Main Course: Sushi
Dessert: Brownie
=======================================
           Enjoy your meal!
```

---

## Getting Started

### Prerequisites

- Python 3.6 or above
- `colorama` library

### Installation

1. **Clone the Repository** (optional if you want to customize or save locally):
   ```bash
   git clone <repository_url>
   cd meal-selector-cli
   ```

2. **Install `colorama`**: 
   Install the color library that enables the styled command-line output:
   ```bash
   pip install colorama
   ```

3. **[Download Meal Selector CLI Tool](https://github.com/your-repository/meal-selector-cli-tool/archive/refs/heads/main.zip)**

### Usage

To run the program, simply execute the script from your terminal:

```bash
python meal_selector.py
```

Each time you run it, the program will generate a new meal suggestion!

---

## Code Explanation

The program uses the following components:

1. **Imports and Initialization**:
   - `random` for selecting random items.
   - `colorama` for color formatting in the command-line output. The `init(autoreset=True)` function ensures that styles reset automatically after each print statement, making it platform-compatible.

2. **Data**:
   - Three lists (`appetizers`, `main_courses`, and `desserts`) store different meal options. These lists can be easily extended to add more choices.

3. **`pick_meal()` Function**:
   - A simple function that randomly picks an item from each list and returns the selected items as a tuple.

4. **Displaying the Output**:
   - The program prints each part of the meal (appetizer, main course, dessert) with labels and colors for a more engaging experience.

---

## Customization

Feel free to modify the lists in the code to include your favorite dishes or additional meal options. Simply add more strings to the `appetizers`, `main_courses`, and `desserts` lists to personalize the tool.

Example:
```python
# Adding items to the main_courses list
main_courses = ["Spaghetti Bolognese", "Grilled Chicken", "Vegetable Stir Fry", "Sushi", "Fried Rice", "Paneer Tikka"]
```

---

## Troubleshooting

1. **Color Not Displaying**:
   - Make sure the `colorama` library is installed. You can check by running:
     ```bash
     pip show colorama
     ```
   - If the problem persists, try using a different terminal or command-line tool.

2. **Adding More Items**:
   - Ensure each item is a string and separated by a comma in the list. 

---

## Acknowledgments

Thanks to the Python community for their continuous support, and to the developers of `colorama` for providing an easy-to-use library for command-line color formatting.

---
