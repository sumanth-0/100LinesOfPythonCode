# Word Scramble Game 🎲

A fun, simple Python script that challenges you to unscramble a randomly chosen technical word!

---

## Features

* **Random Word Selection:** Picks a random word from a predefined list of tech terms each time you play.
* **Letter Scrambling:** Uses Python's `random.shuffle()` to thoroughly mix up the letters.
* **Guaranteed Scramble:** Ensures the scrambled word is different from the original word.
* **Case-Insensitive Guessing:** Checks your answer regardless of whether you use uppercase or lowercase letters.
* **Instant Feedback:** Tells you immediately if you guessed correctly or shows you the right answer.

---

## How it Works

1.  A list of technical words (`tech_words`) is defined in the script.
2.  One word is randomly selected from the list using `random.choice()`.
3.  The chosen word's letters are shuffled using `random.shuffle()`.
4.  The scrambled word is displayed to the player.
5.  The player enters their guess.
6.  The script compares the guess to the original word and declares if it's correct or not.

---

## 🔧 Customization

Want to use your own words? It's easy!

1.  Open the `word_scramble.py` file.
2.  Find the list named `tech_words`.
3.  Add or remove words from the list (make sure each word is in quotes `""` and separated by a comma `,`).

# Example:
word_array = ["python", "another_word", "coding", "fun"]
---

## How to Run
1.  Make sure you have Python installed.
2.  Open your terminal or command prompt.
3.  Navigate to the word_scramble_game folder.
4.  Run the script using the command: python word_scramble.py 
5. Follow the prompt to enter your guess!