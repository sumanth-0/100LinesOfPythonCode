# Multilingual Flashcards

## Description
An interactive language learning tool that helps users practice vocabulary in Spanish, French, and German through flashcard-style questions.

## Features
- **3 Languages**: Practice Spanish, French, and German vocabulary
- **Interactive CLI**: User-friendly command-line interface with emoji indicators
- **Multiple Practice Modes**:
  - Practice individual languages
  - Practice all languages together
- **Progress Tracking**: View statistics including total questions, correct answers, and accuracy percentage
- **Random Questions**: Questions are shuffled for better learning

## Requirements
- Python 3.6 or higher
- No external dependencies required (uses only standard library)

## Installation
1. Clone the repository
2. Navigate to the snippet directory:
   ```bash
   cd snippets/multilingual_flashcards
   ```

## Usage
Run the program:
```bash
python flashcards.py
```

Follow the on-screen menu to:
1. Select a language to practice (Spanish, French, or German)
2. Practice all languages together
3. View your learning statistics
4. Exit the program

## Sample Vocabulary
- **Spanish**: hola, gracias, adiós, agua, casa, libro, gato
- **French**: bonjour, merci, au revoir, eau, maison, livre, chat
- **German**: hallo, danke, auf wiedersehen, wasser, haus, buch, katze

## Example Output
```
==================================================
🌍 MULTILINGUAL FLASHCARD LEARNING SYSTEM 🌍
==================================================

Available Languages:
1. Spanish (7 words)
2. French (7 words)
3. German (7 words)
4. Practice All Languages
5. View Statistics
6. Exit

Select an option: 1

📚 Starting Spanish practice (5 questions)

Question 1/5: Translate 'hola' to English
Your answer: hello
✅ Correct!
```

## Author
Created for issue #614 - Make Multilingual Flashcards

## License
Part of the 100LinesOfPythonCode project
