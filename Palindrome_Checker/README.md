# Palindrome Checker

This program checks if a given string is a palindrome.

## Problem Statement

A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward. The task is to write a Python program that takes a string as input and determines whether it is a palindrome, ignoring case and non-alphanumeric characters.

## Example

If the user enters `"Racecar"`, the output should be:

```
"Racecar" is a palindrome.
```

If the user enters `"Hello"`, the output should be:

```
"Hello" is not a palindrome.
```

## Constraints

- The input string can contain spaces, punctuation, and mixed-case letters.
- The program should be case-insensitive and ignore non-alphanumeric characters.

## Complexity Analysis

- **Time Complexity**: O(L), where L is the length of the input string. This is because we iterate through the string once to clean it and then compare characters from both ends, which takes proportional time to the string's length.
- **Space Complexity**: O(L), where L is the length of the cleaned string. This is due to the creation of a new string to store only the alphanumeric characters.