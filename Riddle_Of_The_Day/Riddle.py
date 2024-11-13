import random

# List of riddles, answers, and hints
riddles = [
    {"question": "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?", 
     "answer": "echo", 
     "hint": "You hear me in the mountains"},
    {"question": "I can be cracked, made, told, and played. What am I?", 
     "answer": "joke", 
     "hint": "I often make you laugh"},
    {"question": "I come from a mine and get surrounded by wood always. Everyone uses me. What am I?", 
     "answer": "pencil", 
     "hint": "I help you write"},
    {"question": "The more you take, the more you leave behind. What am I?", 
     "answer": "footsteps", 
     "hint": "You leave these on the ground"},
    {"question": "I have keys but no locks. I have space but no room. You can enter but can't go inside. What am I?", 
     "answer": "keyboard", 
     "hint": "It's part of a computer"},
    {"question": "I can fly without wings. I can cry without eyes. Whenever I go, darkness flies. What am I?", 
     "answer": "cloud", 
     "hint": "You see me in the sky"},
    {"question": "I can be long or short; I can be grown or bought; I can be painted or left bare. What am I?", 
     "answer": "hair", 
     "hint": "It's on your head"},
    {"question": "I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I?", 
     "answer": "map", 
     "hint": "It's used for navigation"},
    {"question": "What can travel around the world while staying in a corner?", 
     "answer": "stamp", 
     "hint": "It's on mail"},
    {"question": "The more you take, the more you leave behind. What am I?", 
     "answer": "footsteps", 
     "hint": "You leave these behind when you walk"},
    {"question": "What has a head, a tail, is brown, and has no legs?", 
     "answer": "penny", 
     "hint": "It's a type of currency"}
]

def get_daily_riddle():
    return random.choice(riddles)

def check_answer(user_answer, correct_answer):
    return user_answer.lower() == correct_answer.lower()

# Main interaction
if __name__ == "__main__":
    daily_riddle = get_daily_riddle()
    print("Today's riddle: " + daily_riddle["question"])
    
    user_attempt = input("Your answer: ")
    attempts = 0
    
    while not check_answer(user_attempt, daily_riddle["answer"]) and attempts < 3:
        attempts += 1
        print("Try again! Here's a hint: " + daily_riddle["hint"])
        user_attempt = input("Your answer: ")
    
    if check_answer(user_attempt, daily_riddle["answer"]):
        print("Correct! Well done.")
    else:
        print("Out of attempts! The correct answer is: " + daily_riddle["answer"])
