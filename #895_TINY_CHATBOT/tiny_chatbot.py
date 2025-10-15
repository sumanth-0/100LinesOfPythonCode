import random
import time

# --- Tiny Chatbot for Hacktoberfest 2025 ---
# Author: Diya Satish Kumar
# Description: Responds to user input with predefined or random replies.

responses = {
    "hello": [
        "Hey there! 👋",
        "Hi! How’s your day going?",
        "Hello! Ready to chat? 😊"
    ],
    "how are you": [
        "I'm just code, but feeling great!",
        "Doing awesome, thanks for asking!",
        "All systems running smoothly 🚀"
    ],
    "bye": [
        "Goodbye! See you soon 👋",
        "Bye! Take care!",
        "See ya! Keep coding 💻"
    ],
    "joke": [
        "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
        "I told my computer I needed a break... it said 'No problem — I’ll go to sleep!' 😴",
        "There are only 10 kinds of people in the world — those who understand binary and those who don’t."
    ],
    "default": [
        "Hmm... I’m not sure I understand 🤔",
        "Interesting! Tell me more.",
        "Could you say that another way?"
    ]
}

def chatbot_reply(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses["default"])

def type_out(text):
    """Print with typing animation for fun."""
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.02)
    print()

def main():
    print("=" * 50)
    print("🤖 Tiny Chatbot — by Diya Satish Kumar")
    print("Type 'bye' to end the chat.")
    print("=" * 50)

    while True:
        user_input = input("\nYou: ")
        if user_input.strip().lower() == "bye":
            type_out(random.choice(responses["bye"]))
            break
        reply = chatbot_reply(user_input)
        type_out(f"Bot: {reply}")

if __name__ == "__main__":
    main()