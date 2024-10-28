import random

def load_questions():
    """Load trivia questions from a predefined set."""
    return {
        "Science": [
            {"question": "What is the chemical symbol for water?", "answer": "H2O"},
            {"question": "What planet is known as the Red Planet?", "answer": "Mars"},
        ],
        "Geography": [
            {"question": "What is the capital of France?", "answer": "Paris"},
            {"question": "Which river is the longest in the world?", "answer": "Nile"},
        ],
        "History": [
            {"question": "Who was the first President of the United States?", "answer": "George Washington"},
            {"question": "In which year did the Titanic sink?", "answer": "1912"},
        ],
    }

def ask_question(question):
    """Ask a trivia question and return if the user answered correctly."""
    user_answer = input(f"{question['question']} ")
    return user_answer.strip().lower() == question['answer'].lower()

def play_game():
    """Play the trivia game."""
    questions = load_questions()
    score = 0
    total_questions = 0

    for category, qs in questions.items():
        print(f"\nCategory: {category}")
        random.shuffle(qs)  # Randomize question order
        for question in qs:
            total_questions += 1
            if ask_question(question):
                print("Correct!")
                score += 1
            else:
                print("Wrong! The correct answer was:", question['answer'])

    print(f"\nGame Over! Your score: {score}/{total_questions}")

if __name__ == "__main__":
    play_game()
