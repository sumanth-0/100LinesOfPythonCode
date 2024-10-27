import random

def generate_question(difficulty):
    if difficulty == 'easy':
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(['+', '-'])
    elif difficulty == 'medium':
        num1 = random.randint(10, 50)
        num2 = random.randint(1, 20)
        operator = random.choice(['+', '-', '*'])
    else:  # hard
        num1 = random.randint(20, 100)
        num2 = random.randint(1, 50)
        operator = random.choice(['+', '-', '*', '/'])

    question = f"What is {num1} {operator} {num2}?"
    return question, eval(f"{num1} {operator} {num2}")

def run_quiz():
    score = 0
    num_questions = 5
    difficulty = input("Choose difficulty (easy, medium, hard): ").lower()

    for _ in range(num_questions):
        question, answer = generate_question(difficulty)
        user_answer = input(question + " ")

        try:
            if float(user_answer) == answer:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer is {answer}.")
        except ValueError:
            print("Please enter a valid number.")

    print(f"Your score: {score}/{num_questions}")

# Run the quiz
run_quiz()
