"""
Tiny Chatbot with Memory
A chatbot that remembers the last user input and references it in responses.
Uses only Python's built-in libraries - no external dependencies required.
"""

import random
import re

# Response templates that can reference previous input
RESPONSES = {
    'greeting': [
        "Hello! How can I help you today?",
        "Hi there! What's on your mind?",
        "Hey! Nice to meet you!"
    ],
    'farewell': [
        "Goodbye! Have a great day!",
        "See you later!",
        "Take care! Bye!"
    ],
    'thanks': [
        "You're welcome!",
        "Happy to help!",
        "No problem at all!"
    ],
    'memory': [
        "Earlier you mentioned '{memory}'. Tell me more about that!",
        "I remember you said '{memory}'. How's that going?",
        "You were talking about '{memory}' before. Interesting!",
        "Going back to '{memory}', what else can you tell me?"
    ],
    'default': [
        "That's interesting! Tell me more.",
        "I see. What else is on your mind?",
        "Hmm, I understand. Go on!",
        "Fascinating! Continue..."
    ]
}

# Keywords for pattern matching
PATTERNS = {
    'greeting': r'\b(hello|hi|hey|greetings)\b',
    'farewell': r'\b(bye|goodbye|see you|farewell|exit|quit)\b',
    'thanks': r'\b(thanks|thank you|thx|appreciate)\b',
    'memory': r'\b(remember|earlier|before|previous|you said)\b'
}


class TinyChatbot:
    """Simple chatbot with memory of last user input."""
    
    def __init__(self):
        self.last_input = None
        self.conversation_count = 0
    
    def detect_intent(self, user_input):
        """Detects user intent based on keywords."""
        user_input_lower = user_input.lower()
        for intent, pattern in PATTERNS.items():
            if re.search(pattern, user_input_lower):
                return intent
        return 'default'
    
    def get_response(self, user_input):
        """Generates a response based on user input and memory."""
        self.conversation_count += 1
        intent = self.detect_intent(user_input)
        
        # Use memory responses if chatbot has previous input and user asks about it
        if intent == 'memory' and self.last_input:
            response = random.choice(RESPONSES['memory']).format(memory=self.last_input)
        else:
            response = random.choice(RESPONSES.get(intent, RESPONSES['default']))
        
        # Store current input as memory for next interaction
        self.last_input = user_input
        return response
    
    def chat(self):
        """Main chat loop."""
        print("=" * 60)
        print("🤖 Tiny Chatbot with Memory 🤖")
        print("=" * 60)
        print("\nI remember what you say! Try asking me to recall it later.")
        print("Type 'bye' or 'quit' to exit.\n")
        
        while True:
            user_input = input("You: ").strip()
            
            if not user_input:
                print("Bot: Please say something!\n")
                continue
            
            # Check for farewell intent
            if re.search(PATTERNS['farewell'], user_input.lower()):
                print(f"Bot: {random.choice(RESPONSES['farewell'])}\n")
                print(f"We had {self.conversation_count} exchanges. Thanks for chatting!")
                break
            
            # Generate and display response
            response = self.get_response(user_input)
            print(f"Bot: {response}\n")


def main():
    """Main function to run the chatbot."""
    bot = TinyChatbot()
    bot.chat()


if __name__ == "__main__":
    main()