# Word Association Finder

A simple Python tool to find words associated with a target word in a user-provided text corpus. The program scans sentences, finds the target word, and extracts nearby words (context window), filtering out common English stopwords.

---

## Features

- Accepts multiple sentences as input from the user.
- Finds all words appearing near a specified target word.
- Adjustable context window size (number of words before/after the target).
- Filters out common English stopwords for cleaner results.
- Runs entirely in the terminal.

---

## How It Works

1. The user enters sentences one by one (type `END` to finish).
2. The user specifies the target word to search for.
3. The user sets the context window size (how many words before/after to include).
4. The program scans all sentences, finds the target word, and collects associated words within the window.
5. Stopwords are removed from the results.
6. The associated words are printed to the console.

---

## Usage

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Run the program:
   ```bash
   python word_association_finder.py
   ```
4. Enter sentences (type `END` to finish).
5. Enter the target word and context window size.
6. View the associated words.

---