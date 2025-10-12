# Mini Trivia Quiz

## Description

A simple and interactive command-line trivia quiz game that tests your knowledge across various categories including geography, science, art, programming, and general knowledge. The game randomly selects questions from a database and provides instant feedback on your answers.

## Features

- **Random Question Selection**: Questions are randomly selected for each game session
- **Multiple Categories**: Includes questions from various topics
- **Score Tracking**: Keeps track of correct answers and displays final score
- **Percentage Calculation**: Shows your performance as a percentage
- **Performance Feedback**: Provides encouraging feedback based on your score
- **Input Validation**: Ensures valid user input with error handling
- **Graceful Exit**: Handles keyboard interrupts (Ctrl+C) gracefully

## How to Run

```bash
python mini_trivia_quiz.py
```

## Usage

1. Run the script using Python 3
2. Read each question carefully
3. Enter your answer as a number (0-3) corresponding to the option
4. Press Enter to submit your answer
5. Receive instant feedback (correct/incorrect)
6. View your final score at the end

## Requirements

- Python 3.x
- No external dependencies required (uses only standard library)

## Sample Output

```
==================================================
Welcome to the Mini Trivia Quiz!
==================================================

Question 1:
What is the capital of France?
0. London
1. Berlin
2. Paris
3. Madrid

Your answer (0-3): 2
✓ Correct!

==================================================
Quiz Complete! Your score: 4/5
Percentage: 80.0%
Excellent work! 🌟
==================================================
```

## Code Structure

- **QUESTIONS**: Database of trivia questions with multiple choice options
- **display_question()**: Displays a question with numbered options
- **get_user_answer()**: Handles user input with validation
- **run_quiz()**: Main quiz logic and score calculation

## Contributing

This project is part of the 100LinesOfPythonCode repository. Feel free to:
- Add more questions to the database
- Suggest new features
- Report bugs or issues

## License

This project follows the license of the parent repository.

## Issue Reference

Resolves issue #785 - Mini Trivia Quiz
