
import time

class EscapeRoom:
    def __init__(self):
        self.puzzles = {
            "Puzzle 1": ("What has keys but can't open locks? (Answer: Piano)", "piano"),
            "Puzzle 2": ("I speak without a mouth and hear without ears. What am I? (Answer: Echo)", "echo"),
            "Puzzle 3": ("What can travel around the world while staying in a corner? (Answer: Stamp)", "stamp"),
        }
        self.time_limit = 300  # 5 minutes
        self.start_time = None

    def start_game(self):
        print("Welcome to the Virtual Escape Room!")
        self.start_time = time.time()
        for puzzle, (question, answer) in self.puzzles.items():
            print(f"\n{puzzle}: {question}")
            user_answer = input("Your answer: ").strip().lower()
            if self.check_answer(user_answer, answer):
                print("Correct!")
            else:
                print(f"Wrong! The correct answer was: {answer}")

            if self.check_time():
                print("Time's up! You couldn't escape in time.")
                return
        print("Congratulations! You've solved all the puzzles and escaped!")

    def check_answer(self, user_answer, correct_answer):
        return user
