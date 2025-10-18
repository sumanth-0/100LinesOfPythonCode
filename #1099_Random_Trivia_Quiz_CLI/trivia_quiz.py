#!/usr/bin/env python3
"""
Random Trivia Quiz CLI
Fetches trivia questions from Open Trivia Database API and displays the user's score.
"""

import requests
import html
import random
import sys
from typing import List, Dict

def fetch_trivia_questions(amount: int = 10, difficulty: str = "") -> List[Dict]:
    """
    Fetch trivia questions from Open Trivia Database API.
    
    Args:
        amount: Number of questions to fetch (default: 10)
        difficulty: Difficulty level (easy, medium, hard, or empty for any)
    
    Returns:
        List of trivia question dictionaries
    """
    url = f"https://opentdb.com/api.php?amount={amount}"
    if difficulty:
        url += f"&difficulty={difficulty}"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get('results', [])
    except requests.RequestException as e:
        print(f"Error fetching questions: {e}")
        sys.exit(1)

def display_question(question_data: Dict, question_num: int) -> bool:
    """
    Display a trivia question and get user's answer.
    
    Args:
        question_data: Dictionary containing question information
        question_num: Current question number
    
    Returns:
        True if answer is correct, False otherwise
    """
    question = html.unescape(question_data['question'])
    correct_answer = html.unescape(question_data['correct_answer'])
    incorrect_answers = [html.unescape(ans) for ans in question_data['incorrect_answers']]
    
    # Combine and shuffle answers
    all_answers = incorrect_answers + [correct_answer]
    random.shuffle(all_answers)
    
    # Display question
    print(f"\n{'='*60}")
    print(f"Question {question_num}")
    print(f"Category: {html.unescape(question_data['category'])}")
    print(f"Difficulty: {question_data['difficulty'].capitalize()}")
    print(f"{'='*60}")
    print(f"\n{question}\n")
    
    # Display answer options
    for i, answer in enumerate(all_answers, 1):
        print(f"{i}. {answer}")
    
    # Get user input
    while True:
        try:
            user_input = input("\nYour answer (enter number): ").strip()
            choice = int(user_input)
            if 1 <= choice <= len(all_answers):
                break
            print(f"Please enter a number between 1 and {len(all_answers)}")
        except ValueError:
            print("Please enter a valid number")
        except KeyboardInterrupt:
            print("\n\nQuiz interrupted!")
            sys.exit(0)
    
    user_answer = all_answers[choice - 1]
    is_correct = user_answer == correct_answer
    
    if is_correct:
        print("\n✓ Correct!")
    else:
        print(f"\n✗ Wrong! The correct answer was: {correct_answer}")
    
    return is_correct

def main():
    """
    Main function to run the trivia quiz.
    """
    print("\n" + "="*60)
    print("Welcome to Random Trivia Quiz CLI!")
    print("="*60)
    
    # Get quiz parameters
    try:
        num_questions = int(input("\nHow many questions? (1-50, default 10): ").strip() or "10")
        num_questions = max(1, min(50, num_questions))
    except ValueError:
        num_questions = 10
    
    print("\nDifficulty levels: easy, medium, hard (or press Enter for any)")
    difficulty = input("Select difficulty: ").strip().lower()
    if difficulty not in ['easy', 'medium', 'hard']:
        difficulty = ""
    
    print("\nFetching questions...")
    questions = fetch_trivia_questions(num_questions, difficulty)
    
    if not questions:
        print("No questions received. Please try again.")
        sys.exit(1)
    
    # Ask questions and track score
    score = 0
    for i, question_data in enumerate(questions, 1):
        if display_question(question_data, i):
            score += 1
    
    # Display final score
    print(f"\n{'='*60}")
    print("Quiz Complete!")
    print(f"{'='*60}")
    print(f"\nYour Score: {score}/{len(questions)} ({score/len(questions)*100:.1f}%)")
    
    if score == len(questions):
        print("Perfect score! You're a trivia master!")
    elif score >= len(questions) * 0.7:
        print("Great job! You know your trivia!")
    elif score >= len(questions) * 0.5:
        print("Not bad! Keep practicing!")
    else:
        print("Better luck next time!")
    print()

if __name__ == "__main__":
    main()
