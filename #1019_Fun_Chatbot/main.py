"""
Fun & Informative Chatbot
A predefined chatbot that responds to user input in fun and informative ways.
"""

import random
import re
from datetime import datetime


class FunChatbot:
    """A chatbot with predefined responses for various topics."""
    
    def __init__(self):
        """Initialize the chatbot with response patterns and data."""
        self.name = "BuddyBot"
        self.user_name = None
        
        # Greeting patterns
        self.greetings = {
            'patterns': ['hello', 'hi', 'hey', 'greetings', 'good morning', 'good afternoon', 'good evening'],
            'responses': [
                "Hello there! 👋 How can I brighten your day?",
                "Hi! 😊 What's on your mind?",
                "Hey! Great to see you! What would you like to chat about?",
                "Greetings, human! 🤖 Ready for some conversation?"
            ]
        }
        
        # Farewell patterns
        self.farewells = {
            'patterns': ['bye', 'goodbye', 'see you', 'farewell', 'exit', 'quit'],
            'responses': [
                "Goodbye! Have an amazing day! 🌟",
                "See you later! Stay awesome! 👋",
                "Farewell, friend! Come back soon! 😊",
                "Bye! Remember, you're awesome! ✨"
            ]
        }
        
        # Fun facts
        self.facts = [
            "🐙 Octopuses have three hearts!",
            "🍯 Honey never spoils. Archaeologists have found 3000-year-old honey that's still edible!",
            "🌙 A day on Venus is longer than a year on Venus!",
            "🐌 Snails can sleep for up to 3 years!",
            "🍌 Bananas are berries, but strawberries aren't!",
            "🦒 Giraffes have the same number of neck bones as humans - seven!",
            "🔥 Hot water freezes faster than cold water (Mpemba effect)!",
            "🐝 Bees can recognize human faces!",
            "🌊 The Pacific Ocean is larger than all land masses combined!"
        ]
        
        # Jokes
        self.jokes = [
            "Why don't scientists trust atoms? Because they make up everything! 😄",
            "What do you call a bear with no teeth? A gummy bear! 🐻",
            "Why did the scarecrow win an award? He was outstanding in his field! 🌾",
            "What do you call fake spaghetti? An impasta! 🍝",
            "Why don't eggs tell jokes? They'd crack up! 🥚",
            "What did one ocean say to the other? Nothing, they just waved! 🌊",
            "Why did the math book look sad? It had too many problems! 📚"
        ]
        
        # Motivational quotes
        self.motivations = [
            "💪 You're capable of amazing things! Keep going!",
            "🌟 Every day is a new opportunity to be awesome!",
            "🚀 Believe in yourself - you've got this!",
            "✨ Your potential is limitless!",
            "🎯 Small steps lead to big achievements!"
        ]
        
        # Response patterns
        self.patterns = {
            'name': {
                'patterns': ['my name is', 'i am', "i'm", 'call me'],
                'response': self.handle_name
            },
            'how are you': {
                'patterns': ['how are you', 'how do you do', 'how are things'],
                'responses': [
                    "I'm doing great! Thanks for asking! 😊 How about you?",
                    "Fantastic! Ready to chat! 🤖 How are you?",
                    "I'm excellent! What brings you here today?"
                ]
            },
            'what is your name': {
                'patterns': ['what is your name', 'who are you', 'your name'],
                'responses': [
                    f"I'm {self.name}, your friendly chatbot! 🤖",
                    f"They call me {self.name}! Nice to meet you!",
                    f"I'm {self.name}, here to chat and have fun!"
                ]
            },
            'time': {
                'patterns': ['what time', 'current time', 'time now'],
                'response': self.get_time
            },
            'date': {
                'patterns': ['what date', 'today\'s date', 'current date'],
                'response': self.get_date
            },
            'fact': {
                'patterns': ['tell me a fact', 'fun fact', 'interesting fact', 'fact'],
                'response': self.get_fact
            },
            'joke': {
                'patterns': ['tell me a joke', 'make me laugh', 'joke', 'funny'],
                'response': self.get_joke
            },
            'motivate': {
                'patterns': ['motivate me', 'inspire me', 'motivation', 'inspiration'],
                'response': self.get_motivation
            },
            'help': {
                'patterns': ['help', 'what can you do', 'commands'],
                'response': self.show_help
            },
            'weather': {
                'patterns': ['weather', 'temperature'],
                'responses': [
                    "I can't check the weather, but I hope it's beautiful wherever you are! ☀️",
                    "Weather info isn't my strong suit, but every day is a good day with the right attitude! 🌤️"
                ]
            },
            'love': {
                'patterns': ['i love you', 'love you'],
                'responses': [
                    "Aww! I appreciate you too! 💙",
                    "You're sweet! Thanks for the love! 😊",
                    "Love is in the air! 💕"
                ]
            }
        }
    
    def handle_name(self, user_input):
        """Extract and remember user's name."""
        # Try to extract name after patterns
        for pattern in ['my name is', 'i am', "i'm", 'call me']:
            if pattern in user_input:
                name = user_input.split(pattern)[1].strip().split()[0]
                self.user_name = name.capitalize()
                return f"Nice to meet you, {self.user_name}! 😊 I'm {self.name}!"
        return "Nice to meet you! 😊"
    
    def get_time(self, user_input=None):
        """Return current time."""
        current_time = datetime.now().strftime("%I:%M %p")
        return f"⏰ The current time is {current_time}"
    
    def get_date(self, user_input=None):
        """Return current date."""
        current_date = datetime.now().strftime("%B %d, %Y")
        return f"📅 Today is {current_date}"
    
    def get_fact(self, user_input=None):
        """Return a random fun fact."""
        return random.choice(self.facts)
    
    def get_joke(self, user_input=None):
        """Return a random joke."""
        return random.choice(self.jokes)
    
    def get_motivation(self, user_input=None):
        """Return a motivational message."""
        return random.choice(self.motivations)
    
    def show_help(self, user_input=None):
        """Show available commands."""
        help_text = """
🤖 Here's what I can do:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• Say 'hello' to greet me
• Ask 'what is your name' to know me
• Say 'my name is [name]' to introduce yourself
• Ask 'what time' or 'what date' for current info
• Say 'tell me a fact' for interesting facts
• Say 'tell me a joke' for some humor
• Say 'motivate me' for inspiration
• Say 'how are you' to check on me
• Say 'bye' when you want to leave
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Just chat naturally! I'll do my best to respond! 😊
        """
        return help_text.strip()
    
    def get_response(self, user_input):
        """Generate a response based on user input."""
        user_input = user_input.lower().strip()
        
        # Check for greetings
        for pattern in self.greetings['patterns']:
            if pattern in user_input:
                return random.choice(self.greetings['responses'])
        
        # Check for farewells
        for pattern in self.farewells['patterns']:
            if pattern in user_input:
                response = random.choice(self.farewells['responses'])
                return response, True  # True indicates exit
        
        # Check for pattern matches
        for category, data in self.patterns.items():
            for pattern in data['patterns']:
                if pattern in user_input:
                    if 'response' in data:
                        # Call the function
                        return data['response'](user_input)
                    elif 'responses' in data:
                        return random.choice(data['responses'])
        
        # Default responses if no match
        default_responses = [
            "That's interesting! Tell me more! 🤔",
            "I'm not sure about that, but I'm here to chat! 😊",
            "Hmm, that's a new one! Can you rephrase?",
            "I'm still learning! Try asking me for a joke or fact! 🤖",
            f"Interesting point{', ' + self.user_name if self.user_name else ''}! What else is on your mind?"
        ]
        return random.choice(default_responses)
    
    def start(self):
        """Start the chatbot conversation."""
        print("\n" + "=" * 70)
        print(f"🤖 Welcome to {self.name} - Your Fun & Informative Chatbot!")
        print("=" * 70)
        print(f"\nHi! I'm {self.name}! Type 'help' to see what I can do.")
        print("Type 'bye' to exit.\n")
        
        while True:
            try:
                user_input = input("You: ").strip()
                
                if not user_input:
                    print(f"{self.name}: Please say something! 😊\n")
                    continue
                
                response = self.get_response(user_input)
                
                # Check if it's a farewell (tuple with exit flag)
                if isinstance(response, tuple):
                    print(f"{self.name}: {response[0]}\n")
                    break
                
                print(f"{self.name}: {response}\n")
                
            except KeyboardInterrupt:
                print(f"\n\n{self.name}: Goodbye! 👋\n")
                break
            except Exception as e:
                print(f"{self.name}: Oops! Something went wrong. Let's continue! 😊\n")


def main():
    """Main function to run the chatbot."""
    chatbot = FunChatbot()
    chatbot.start()


if __name__ == "__main__":
    main()
