import random

class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

def create_flashcards():
    return [
        Flashcard("What is the capital of France?", "Paris"),
        Flashcard("What is 2 + 2?", "4"),
        Flashcard("What is the largest planet in our solar system?", "Jupiter"),
        Flashcard("What is the chemical symbol for water?", "H2O"),
        Flashcard("Who wrote 'Romeo and Juliet'?", "William Shakespeare")
    ]

def quiz_user(flashcards):
    random.shuffle(flashcards)
    score = 0

    for flashcard in flashcards:
        user_answer = input(f"Q: {flashcard.question} ")
        if user_answer.strip().lower() == flashcard.answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {flashcard.answer}")

    print(f"\nYour final score is: {score}/{len(flashcards)}")

def main():
    flashcards = create_flashcards()
    print("Welcome to the Flashcard Quizzer!")
    quiz_user(flashcards)

if __name__ == "__main__":
    main()
