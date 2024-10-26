import random

# defined a dict
responses = {
    "greeting": ["Hello!", "Hi there!", "Hey! How can I help you?"],
    "weather": ["I hope it's sunny wherever you are!", "I'm not sure, but stay prepared!", "Weather's great for a chat with me!"],
    "how are you": ["I'm just code, but I'm doing great!", "I'm here to help you!"],
    "joke": ["Why did the computer break up with the internet? Because it found someone else in cache!",
             "Why do programmers prefer dark mode? Because light attracts bugs!"],
    "goodbye": ["Goodbye!", "See you later!", "Take care!"]
}

# Function to find intent 
def find_intent(user_input):
    user_input = user_input.lower()
    if any(word in user_input for word in ["hello", "hi", "hey"]):
        return "greeting"
    elif "weather" in user_input:
        return "weather"
    elif "how are you" in user_input:
        return "how are you"
    elif "joke" in user_input:
        return "joke"
    elif any(word in user_input for word in ["bye", "goodbye", "see you"]):
        return "goodbye"
    return "unknown"

# Function to respond based on detected intent
def respond(user_input):
    intent = find_intent(user_input)
    if intent in responses:
        return random.choice(responses[intent])
    else:
        return "I'm not sure how to respond to that, but I'm here to chat!"

# Main chatbot interaction
print("Chatbot: Hi! You can chat with me or type 'exit' to end.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    print("Chatbot:", respond(user_input))
