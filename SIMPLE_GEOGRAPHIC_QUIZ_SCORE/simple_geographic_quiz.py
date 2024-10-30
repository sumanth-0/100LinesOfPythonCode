
import random

class GeographicQuiz:
    def __init__(self):
        self.locations = {
            "Australia": "path/to/australia_outline.png",
            "Canada": "path/to/canada_outline.png",
            "Brazil": "path/to/brazil_outline.png",
            "India": "path/to/india_outline.png",
            "China": "path/to/china_outline.png"
        }

    def start_quiz(self):
        score = 0
        for country, outline in random.sample(list(self.locations.items()), len(self.locations)):
            print(f"Guess the country from the outline: {outline}")
            answer = input("Your guess: ")
            if answer.strip().lower() == country.lower():
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer is {country}.")
        print(f"Your total score: {score}/{len(self.locations)}")

def main():
    quiz = GeographicQuiz()
    quiz.start_quiz()

if __name__ == "__main__":
    main()
