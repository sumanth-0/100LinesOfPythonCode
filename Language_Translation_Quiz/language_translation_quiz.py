import random

# Dictionary of words/phrases for translation
translations = {
    "Hello": "Hola",
    "Thank you": "Gracias",
    "Goodbye": "Adiós",
    "Please": "Por favor",
    "Yes": "Sí",
    "No": "No",
    "Good morning": "Buenos días",
    "Good night": "Buenas noches",
}

def ask_question():
    """Select a random question for the quiz."""
    english_word = random.choice(list(translations.keys()))
    correct_translation = translations[english_word]
    return english_word, correct_translation

def main():
    """Run the language translation quiz."""
    score = 0
    total_questions = 5

    print("Welcome to the Language Translation Quiz!\n")
    for _ in range(total_questions):
        english_word, correct_translation = ask_question()
        user_answer = input(f"What is the translation of '{english_word}' in Spanish? ")

        if user_answer.strip().lower() == correct_translation.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect! The correct answer is '{correct_translation}'.\n")

    print(f"You scored {score} out of {total_questions}.")

if __name__ == "__main__":
    main()
