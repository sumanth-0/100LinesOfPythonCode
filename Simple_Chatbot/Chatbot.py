import random

def get_chatbot_response(user_input):
    text = user_input.lower()

    if "hello" in text or "hi" in text or "hey" in text:
        responses = ["Hello! How can I help you?", "Hi there! What's up?", "Hey! Good to see you."]
        return random.choice(responses)

    elif "how are you" in text or "how's it going" in text:
        responses = ["I'm just a bot, but I'm functioning perfectly!", "I'm doing well, thank you for asking!"]
        return random.choice(responses)

    elif "what is your name" in text or "who are you" in text:
        return "I am a simple rule-based chatbot created in Python."

    elif "what can you do" in text or "help" in text:
        return "I can respond to basic greetings and questions. Try asking 'who are you' or 'how are you'."

    else:
        responses = [
            "I'm sorry, I don't understand that.",
            "I'm not sure what you mean. Can you rephrase?",
            "My apologies, I can't respond to that. Try asking for 'help'."
        ]
        return random.choice(responses)

def main():
    print("Welcome to the Rule-Based Chatbot!")
    print("Type 'exit', 'quit', or 'bye' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Bot: Goodbye! Have a great day!")
            break
        
        response = get_chatbot_response(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    main()