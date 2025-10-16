## Word Frequency Counter

This Python script reads a text file, counts the frequency of each word, and displays the top 10 most common words.

### How It Works

1. **Read the File**  
   The script opens the specified text file and reads its entire content into memory. It converts all text to lowercase to ensure that word counting is case-insensitive (e.g., "The" and "the" are treated as the same word).

2. **Extract Words Using Regular Expressions**  
   Using a regular expression (`\b[\w']+\b`), it extracts all words from the text. This pattern matches sequences of letters, digits, underscores, and apostrophes, so words like "don't" are correctly captured.

3. **Count Word Frequencies**  
   The extracted words are counted using Python’s `collections.Counter` class, which efficiently calculates how many times each word appears.

4. **Display the Top 10 Words**  
   The script retrieves and prints the 10 most common words along with their counts.

### Usage

To use this script, call the `top_10_word_frequencies` function with the path to your text file:

```python
top_10_word_frequencies('yourfile.txt')