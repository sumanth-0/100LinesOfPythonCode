# Dependencies required: requests
# Install requests by running this command in your terminal:
# For Windows: pip install requests
# For macOS/Linux: pip3 install requests

import requests
import random

# Function to fetch questions from the trivia API
def getQuestions():
    url = "https://opentdb.com/api.php?amount=5&type=multiple"
    response = requests.get(url)
    data = response.json()
    questions = data['results']
    
    flashcards = []
    for question in questions:
        flashcards.append({
            "question": question['question'],
            "correct_answer": question['correct_answer'],
            "incorrect_answers": question['incorrect_answers'],
            "difficulty": question['difficulty']
        })
    return flashcards

# Flashcard Quiz Function
def flashCardQuiz():
    flashcards = getQuestions()
    score = 0

    for flashcard in flashcards:
        print(f"\n{flashcard['question']}")
        options = flashcard['incorrect_answers'] + [flashcard['correct_answer']]
        random.shuffle(options)

        for idx, option in enumerate(options):
            print(f"{idx+1}. {option}")

        try:
            answer = int(input("Your answer (1-4): "))
            if options[answer-1] == flashcard['correct_answer']:
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong! The correct answer is: {flashcard['correct_answer']}\n")
        except (ValueError, IndexError):
            print("Invalid input! Please enter a number between 1 and 4.\n")
    
    print(f"Quiz completed! Your score: {score}/{len(flashcards)}\n")

# Main Function to Start the Quiz
def main():
    print('Welcome to the game!!!🔥')
    while True:
        flashCardQuiz()
        b = input('Type "y" to play again or any other key to exit: ')
        if b.lower() != 'y':
            break

# Entry point of the program
if __name__ == '__main__':
    main()
