# Binary Search Guessing Game (GUI)

This is a small desktop application built with Python's built-in `tkinter` module. It's a game designed to help users practice the logic of a binary search.

## Description

The game generates a secret random number between 1 and 100. The user then has a limited number of 7 guesses to find the number. After each guess, the app will provide a hint:
* **"Too LOW"**
* **"Too HIGH"**

The user must use these hints to "zero in" on the correct number, just like a binary search algorithm. 7 guesses is the mathematical minimum required to find any number between 1-100 (since $2^7 = 128$).

## Features

* Full graphical user interface (GUI).
* Random number generation for endless replayability.
* "Too HIGH" / "Too LOW" hints to guide the user.
* Tracks the number of guesses remaining.
* "Reset" button to start a new game at any time.

## How to Run

1.  Ensure you have Python 3 installed (which includes `tkinter`).
2.  Run the script from your terminal:
    ```sh
    python binary_search_game.py
    ```
3.  A GUI window will pop up to play the game.

## Modules Used

* **`tkinter`**: (Python's built-in GUI library)
* **`random`**: (Built-in module for generating the secret number)