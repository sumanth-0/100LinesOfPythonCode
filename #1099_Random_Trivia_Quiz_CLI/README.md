# Random Trivia Quiz CLI

## Description
A command-line trivia quiz application that fetches random questions from the Open Trivia Database API and tracks your score.

## Features
- Fetch trivia questions from Open Trivia Database API
- Choose the number of questions (1-50)
- Select difficulty level (easy, medium, hard, or random)
- Multiple choice questions with shuffled answers
- Real-time feedback on answers
- Final score with performance rating
- Clean and interactive CLI interface

## Requirements
- Python 3.6+
- requests library

## Installation
1. Install required dependencies:
```bash
pip install requests
```

## Usage
Run the script:
```bash
python trivia_quiz.py
```

Follow the prompts to:
1. Enter the number of questions you want (default: 10)
2. Select difficulty level (or press Enter for any difficulty)
3. Answer each question by entering the number corresponding to your choice
4. View your final score and performance rating

## Example
```
============================================================
Welcome to Random Trivia Quiz CLI!
============================================================

How many questions? (1-50, default 10): 5

Difficulty levels: easy, medium, hard (or press Enter for any)
Select difficulty: medium

Fetching questions...

============================================================
Question 1
Category: Science: Computers
Difficulty: Medium
============================================================

What does CPU stand for?

1. Central Process Unit
2. Computer Personal Unit
3. Central Processing Unit
4. Central Processor Unit

Your answer (enter number): 3

✓ Correct!
...
```

## API
This project uses the [Open Trivia Database API](https://opentdb.com/) to fetch trivia questions.

## License
This project is part of the 100 Lines of Python Code repository.

## Issue
Solves Issue #1099 - Random Trivia Quiz CLI
