# 😃 Emoji Counter 🎉

A simple Python program to **count emojis** in a text file, log file, or user-pasted text using a Tkinter GUI for file selection 🖱️.

---

## Features ✨

* Detects all standard Unicode emojis using the `emoji` Python library .
* Supports input from:
  * `.txt` files 📄
  * `.log` files 📝
  * Directly pasted text ⌨️
* Uses a **Tkinter file dialog** to select files conveniently .
* Counts both single-character and standard emojis .

---

## Requirements 📦

* Python 3.7 or higher 
* Python packages:
  ```bash
  pip install emoji tk

* Works on Windows, macOS, and Linux  (Tkinter must be installed).

---

## How to Use 📝

1. **Run the script**:

   ```bash
   python emoji_counter.py
   ```
2. **Choose an option** from the menu:

   ```
   1. Text File(.txt) or Log File(.log) 📄
   2. Paste Text ⌨️
   3. Exit ❌
   ```
3. **If Option 1 is selected**:

   * A file dialog will open to select your `.txt` or `.log` file 🗂️.
   * Only files with these extensions are allowed .
4. **If Option 2 is selected**:

   * Paste the text directly into the terminal/console .
5. The program will **output the number of emojis** in the text .

---

## Example 📌

Given the following text in a file or pasted:

```
Hello 😀! I love 🍕 and 🏀.
Family time 👨‍👩‍👧‍👦 is the best ❤️.
```

Output:

```
The Number Of Emojis In The Provided Data Is 6 
```

---

## Notes 

* The program **counts emojis character by character**, so some complex emojis or zero-width joiner sequences are counted individually per character.
* Always use `UTF-8` encoded files for proper emoji support 💾.

