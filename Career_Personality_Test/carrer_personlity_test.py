def ask_question(question, options):
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    while True:
        try:
            choice = int(input("Choose an option (1-4): "))
            if 1 <= choice <= 4:
                return choice
            else:
                print("Invalid choice. Please choose a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    questions = [
        ("What do you enjoy doing in your free time?", 
         ["Reading books", "Playing sports", "Coding", "Painting"]),
        ("Which of these subjects did you enjoy the most in school?", 
         ["Literature", "Physical Education", "Mathematics", "Art"]),
        ("What type of work environment do you prefer?", 
         ["Quiet and focused", "Active and dynamic", "Structured and logical", "Creative and flexible"]),
        ("Which of these activities do you find most fulfilling?", 
         ["Writing", "Team sports", "Solving puzzles", "Creating art"])
    ]

    career_paths = {
        1: "Writer or Editor",
        2: "Athlete or Coach",
        3: "Software Developer or Engineer",
        4: "Artist or Designer"
    }

    scores = [0, 0, 0, 0]

    for question, options in questions:
        choice = ask_question(question, options)
        scores[choice - 1] += 1

    max_score = max(scores)
    suggested_careers = [career_paths[i + 1] for i, score in enumerate(scores) if score == max_score]

    print("\nBased on your answers, you might enjoy a career as a:")
    for career in suggested_careers:
        print(f"- {career}")

if __name__ == "__main__":
    main()