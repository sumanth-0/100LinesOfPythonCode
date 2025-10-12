#!/usr/bin/env python3
"""
Mini Trivia Quiz
A simple command-line trivia quiz game with random questions from various categories.
"""

import random
import sys

# Trivia questions database
QUESTIONS = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Berlin", "Paris", "Madrid"],
        "answer": 2
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Venus", "Mars", "Jupiter", "Saturn"],
        "answer": 1
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["Michelangelo", "Leonardo da Vinci", "Raphael", "Donatello"],
        "answer": 1
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic", "Indian", "Arctic", "Pacific"],
        "answer": 3
    },
    {
        "question": "In which year did World War II end?",
        "options": ["1943", "1944", "1945", "1946"],
        "answer": 2
    },
    {
        "question": "What is the smallest prime number?",
        "options": ["0", "1", "2", "3"],
        "answer": 2
    },
    {
        "question": "Which programming language is known for its use in data science?",
        "options": ["Java", "C++", "Python", "Ruby"],
        "answer": 2
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["Go", "Gd", "Au", "Ag"],
        "answer": 2
    }
]

def display_question(question_num, question_data):
    """Display a question with its options."""
    print(f"\nQuestion {question_num}:")
    print(question_data["question"])
    for i, option in enumerate(question_data["options"]):
        print(f"{i}. {option}")

def get_user_answer():
    """Get and validate user's answer."""
    while True:
        try:
            answer = input("\nYour answer (0-3): ")
            answer = int(answer)
            if 0 <= answer <= 3:
                return answer
            else:
                print("Please enter a number between 0 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        except (KeyboardInterrupt, EOFError):
            print("\n\nQuiz interrupted. Goodbye!")
            sys.exit(0)

def run_quiz(num_questions=5):
    """Main quiz function."""
    print("=" * 50)
    print("Welcome to the Mini Trivia Quiz!")
    print("=" * 50)
    
    # Select random questions
    quiz_questions = random.sample(QUESTIONS, min(num_questions, len(QUESTIONS)))
    score = 0
    
    for i, question in enumerate(quiz_questions, 1):
        display_question(i, question)
        user_answer = get_user_answer()
        
        if user_answer == question["answer"]:
            print("✓ Correct!")
            score += 1
        else:
            correct_answer = question["options"][question["answer"]]
            print(f"✗ Wrong! The correct answer was: {correct_answer}")
    
    # Display final results
    print("\n" + "=" * 50)
    print(f"Quiz Complete! Your score: {score}/{len(quiz_questions)}")
    percentage = (score / len(quiz_questions)) * 100
    print(f"Percentage: {percentage:.1f}%")
    
    if percentage >= 80:
        print("Excellent work! 🌟")
    elif percentage >= 60:
        print("Good job! 👍")
    else:
        print("Keep practicing! 📚")
    print("=" * 50)

if __name__ == "__main__":
    run_quiz()
