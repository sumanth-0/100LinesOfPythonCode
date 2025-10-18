import random
import time

def display_welcome():
    """Display welcome message and instructions."""
    print("="*50)
    print("Welcome to the Mini Quiz Show!")
    print("="*50)
    print("\nTest your knowledge with this fun quiz!")
    print("You'll be asked multiple choice questions.")
    print("Choose your answer by typing A, B, C, or D.")
    print("\nLet's get started!\n")
    time.sleep(2)

def get_quiz_questions():
    """Return a list of quiz questions with answers."""
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A) London", "B) Berlin", "C) Paris", "D) Madrid"],
            "answer": "C"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"],
            "answer": "B"
        },
        {
            "question": "What is 7 x 8?",
            "options": ["A) 54", "B) 56", "C) 64", "D) 48"],
            "answer": "B"
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "options": ["A) Charles Dickens", "B) William Shakespeare", "C) Mark Twain", "D) Jane Austen"],
            "answer": "B"
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"],
            "answer": "D"
        },
        {
            "question": "Which programming language is known for web development?",
            "options": ["A) Python", "B) JavaScript", "C) C++", "D) Java"],
            "answer": "B"
        },
        {
            "question": "What year did World War II end?",
            "options": ["A) 1943", "B) 1944", "C) 1945", "D) 1946"],
            "answer": "C"
        },
        {
            "question": "How many continents are there?",
            "options": ["A) 5", "B) 6", "C) 7", "D) 8"],
            "answer": "C"
        },
        {
            "question": "What is the chemical symbol for gold?",
            "options": ["A) Go", "B) Gd", "C) Au", "D) Ag"],
            "answer": "C"
        },
        {
            "question": "Which animal is the fastest on land?",
            "options": ["A) Lion", "B) Cheetah", "C) Leopard", "D) Gazelle"],
            "answer": "B"
        }
    ]
    return random.sample(questions, min(len(questions), 10))

def ask_question(question_data, question_num, total_questions):
    """Display a question and get user's answer."""
    print(f"\nQuestion {question_num}/{total_questions}")
    print("-" * 50)
    print(question_data["question"])
    for option in question_data["options"]:
        print(option)
    
    while True:
        answer = input("\nYour answer (A/B/C/D): ").strip().upper()
        if answer in ["A", "B", "C", "D"]:
            return answer
        print("Invalid input! Please enter A, B, C, or D.")

def display_score(score, total):
    """Display the final score with feedback."""
    print("\n" + "="*50)
    print("QUIZ COMPLETE!")
    print("="*50)
    print(f"\nYour Score: {score}/{total}")
    percentage = (score / total) * 100
    print(f"Percentage: {percentage:.1f}%")
    
    if percentage == 100:
        print("\nPerfect score! You're a genius!")
    elif percentage >= 80:
        print("\nExcellent work! You really know your stuff!")
    elif percentage >= 60:
        print("\nGood job! You passed the quiz!")
    elif percentage >= 40:
        print("\nNot bad, but there's room for improvement!")
    else:
        print("\nKeep practicing! You'll do better next time!")

def main():
    """Main function to run the quiz show."""
    display_welcome()
    questions = get_quiz_questions()
    score = 0
    total_questions = len(questions)
    
    for i, question_data in enumerate(questions, 1):
        user_answer = ask_question(question_data, i, total_questions)
        if user_answer == question_data["answer"]:
            print("✓ Correct!")
            score += 1
        else:
            print(f"✗ Wrong! The correct answer was {question_data['answer']}.")
        time.sleep(1)
    
    display_score(score, total_questions)

if __name__ == "__main__":
    main()
