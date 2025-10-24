import random
import time
import sys

# --- Typing animation ---
def type_print(text, delay=0.03):
    """Prints text with a typing animation effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# --- Predefined responses ---
responses = {
    "greeting": [
        "Hello there!",
        "Hi! How are you today?",
        "Good to see you.",
        "Hey! Nice to meet you."
    ],
    "question": [
        "That's a good question.",
        "I'm not entirely sure, but I'll think about it.",
        "Interesting question. What do you think?",
        "That’s something worth exploring further."
    ],
    "joke": [
        "Why did the computer show up late? It had a hard drive.",
        "Why do Java developers wear glasses? Because they can't C#.",
        "I told my AI friend a joke, but it didn’t get it — no sense of humor."
    ],
    "farewell": [
        "Goodbye.",
        "See you later.",
        "Take care.",
        "It was nice talking with you."
    ],
    "unknown": [
        "I'm not sure I understand.",
        "Could you please rephrase that?",
        "I don’t have an answer for that yet.",
        "Let's talk about something else."
    ]
}

# --- Simple input classification ---
def classify_input(user_input):
    text = user_input.lower()
    if any(word in text for word in ["hi", "hello", "hey", "greetings"]):
        return "greeting"
    elif any(word in text for word in ["bye", "goodbye", "see you"]):
        return "farewell"
    elif any(word in text for word in ["joke", "funny"]):
        return "joke"
    elif text.endswith("?"):
        return "question"
    else:
        return "unknown"

# --- Chatbot main loop ---
def chatbot():
    type_print("TinyChatBot initialized. Type 'bye' to exit.\n")
    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue

        category = classify_input(user_input)
        reply = random.choice(responses[category])

        # Simulate typing
        type_print("Bot is typing", delay=0.15)
        for _ in range(3):
            sys.stdout.write(".")
            sys.stdout.flush()
            time.sleep(0.4)
        print()
        time.sleep(0.2)

        type_print(f"Bot: {reply}\n")

        if category == "farewell":
            break

if __name__ == "__main__":
    chatbot()
