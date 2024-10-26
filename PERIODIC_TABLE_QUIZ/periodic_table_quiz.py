import random

# Sample periodic table data (add more elements as desired)
periodic_table = [
    {"name": "Hydrogen", "symbol": "H", "atomic_number": 1},
    {"name": "Helium", "symbol": "He", "atomic_number": 2},
    {"name": "Lithium", "symbol": "Li", "atomic_number": 3},
    {"name": "Carbon", "symbol": "C", "atomic_number": 6},
    {"name": "Oxygen", "symbol": "O", "atomic_number": 8},
    {"name": "Neon", "symbol": "Ne", "atomic_number": 10},
    {"name": "Iron", "symbol": "Fe", "atomic_number": 26},
    {"name": "Gold", "symbol": "Au", "atomic_number": 79},
]

def quiz():
    score = 0
    print("Welcome to the Periodic Table Quiz!")
    print("Answer the following questions or type 'exit' to quit.\n")
    
    for _ in range(5):  # 5 questions per quiz
        element = random.choice(periodic_table)
        question_type = random.choice(["name", "symbol", "atomic_number"])

        if question_type == "name":
            answer = input(f"What is the symbol for {element['name']}? ")
            if answer.lower() == element["symbol"].lower():
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect! The correct answer is {element['symbol']}.")

        elif question_type == "symbol":
            answer = input(f"Which element has the symbol {element['symbol']}? ")
            if answer.lower() == element["name"].lower():
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect! The correct answer is {element['name']}.")

        elif question_type == "atomic_number":
            answer = input(f"What is the atomic number of {element['name']}? ")
            if answer == str(element["atomic_number"]):
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect! The correct answer is {element['atomic_number']}.")

        print()  # Line break between questions

    print(f"Quiz over! Your score: {score}/5")
    print("Thanks for playing!")

if __name__ == "__main__":
    quiz()
