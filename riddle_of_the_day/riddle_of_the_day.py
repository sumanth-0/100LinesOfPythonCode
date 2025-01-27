import random

class RiddleOfTheDay:
    def __init__(self):
        self.riddles = [
            {
                "question": "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?",
                "answer": "echo",
                "hints": [
                    "You can hear it in the mountains.",
                    "It often comes back when you call out."
                ]
            },
            {
                "question": "What has keys but can't open locks?",
                "answer": "piano",
                "hints": [
                    "It’s a musical instrument.",
                    "It has a black and white appearance."
                ]
            },
            {
                "question": "What has to be broken before you can use it?",
                "answer": "egg",
                "hints": [
                    "It's often used in cooking.",
                    "You would crack it open."
                ]
            }
        ]

    def get_random_riddle(self):
        return random.choice(self.riddles)

    def play(self):
        riddle = self.get_random_riddle()
        print("Riddle of the Day:")
        print(riddle["question"])
        
        attempts = 3
        
        while attempts > 0:
            answer = input("Your answer (or type 'hint' for a hint): ").strip().lower()
            
            if answer == riddle["answer"]:
                print("Correct! 🎉")
                break
            elif answer == "hint":
                if riddle["hints"]:
                    print("Hint:", riddle["hints"].pop(0))
                else:
                    print("No more hints available!")
            else:
                attempts -= 1
                print(f"Wrong answer! You have {attempts} attempts left.")
        
        if attempts == 0:
            print("Sorry, you're out of attempts. The answer was:", riddle["answer"])

def main():
    riddle_game = RiddleOfTheDay()
    riddle_game.play()

if __name__ == "__main__":
    main()
