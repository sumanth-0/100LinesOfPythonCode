
import random

# Mythology trivia questions with options and answers
questions = [
    {
        "question": "Who is the Greek god of the underworld?",
        "options": ["Zeus", "Apollo", "Hades", "Hermes"],
        "answer": "Hades",
        "fact": "Hades rules the underworld, where souls go after death, according to Greek mythology."
    },
    {
        "question": "In Norse mythology, what is the name of Thor's hammer?",
        "options": ["Mjolnir", "Excalibur", "Brisingr", "Gungnir"],
        "answer": "Mjolnir",
        "fact": "Mjolnir is known as one of the most powerful weapons in Norse mythology."
    },
    {
        "question": "In Egyptian mythology, who is the god of the sun?",
        "options": ["Ra", "Osiris", "Anubis", "Set"],
        "answer": "Ra",
        "fact": "Ra was considered the king of the gods and the god of the sun in ancient Egypt."
    },
    {
        "question": "Which Roman god is the equivalent of the Greek god Ares?",
        "options": ["Mars", "Mercury", "Neptune", "Apollo"],
        "answer": "Mars",
        "fact": "Mars was revered as the god of war in Roman mythology, akin to Ares in Greek culture."
    }
]

# Function to ask a trivia question
def ask_question(question_data):
    print("\n" + question_data["question"])
    for idx, option in enumerate(question_data["options"], 1):
        print(f"{idx}. {option}")
    
    answer = input("Your answer (1-4): ")
    chosen_option = question_data["options"][int(answer) - 1]
    
    if chosen_option == question_data["answer"]:
        print("Correct! 🎉")
    else:
        print(f"Incorrect. The correct answer is {question_data['answer']}.")
    
    # Display fun fact after each question
    print(f"Fun Fact: {question_data['fact']}")

# Start the trivia quiz
def start_quiz():
    print("Welcome to the Mythology Trivia Quiz! Test your knowledge of myths around the world.")
    random.shuffle(questions)
    for question_data in questions:
        ask_question(question_data)

# Run the quiz
if __name__ == "__main__":
    start_quiz()
