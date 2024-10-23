import re

class PasswordStrengthChecker:
    def __init__(self):
        self.criteria = [
            {"desc": "At least 8 characters long", "regex": r".{8,}", "weight": 1},
            {"desc": "Contains uppercase letters", "regex": r"[A-Z]", "weight": 1},
            {"desc": "Contains lowercase letters", "regex": r"[a-z]", "weight": 1},
            {"desc": "Contains numbers", "regex": r"\d", "weight": 1},
            {"desc": "Contains special characters", "regex": r"[!@#$%^&*(),.?\":{}|<>]", "weight": 1},
            {"desc": "Contains no spaces", "regex": r"^\S+$", "weight": 1},
            {"desc": "At least 12 characters long", "regex": r".{12,}", "weight": 2},
            {"desc": "Contains both upper and lower case letters", "regex": r"(?=.*[a-z])(?=.*[A-Z])", "weight": 2},
        ]
        self.feedback = []

    def evaluate(self, password):
        score = 0
        self.feedback = []
        for criterion in self.criteria:
            if re.search(criterion["regex"], password):
                score += criterion["weight"]
            else:
                self.feedback.append(criterion["desc"])

        max_score = sum(criterion["weight"] for criterion in self.criteria)
        return score, max_score

    def classify(self, score, max_score):
        percentage = (score / max_score) * 100
        if percentage >= 80:
            return "Strong"
        elif percentage >= 50:
            return "Moderate"
        else:
            return "Weak"

    def give_feedback(self):
        if not self.feedback:
            return "Your password meets all criteria!"
        return "Suggestions to improve:\n" + "\n".join(self.feedback)

def get_password_input():
    return input("Enter the password to check: ")

def main():
    checker = PasswordStrengthChecker()
    password = get_password_input()
    
    score, max_score = checker.evaluate(password)
    strength = checker.classify(score, max_score)

    print(f"Password Strength: {strength}")
    print(f"Score: {score}/{max_score}")
    print(checker.give_feedback())

if __name__ == "__main__":
    main()
