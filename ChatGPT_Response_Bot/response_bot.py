#!/usr/bin/env python3
"""
ChatGPT Style Random Response Bot
A simple chatbot that provides randomized responses similar to ChatGPT style.
Supports multiple conversation modes and CLI interface.

Author: GitHub Contributor
Issue: #680 - ChatGPT Style Random Response Bot
"""

import random
import sys
import re
import time
from datetime import datetime
from typing import List, Dict

class ChatGPTStyleBot:
    """A ChatGPT-style response bot with multiple conversation modes."""
    
    def __init__(self):
        """Initialize the bot with predefined responses and conversation modes."""
        self.conversation_history = []
        self.user_name = "User"
        self.bot_name = "Assistant"
        self.current_mode = "friendly"
        
        # Different response categories for various contexts
        self.responses = {
            "greetings": [
                "Hello! How can I assist you today?",
                "Hi there! I'm here to help with whatever you need.",
                "Greetings! What would you like to discuss?",
                "Good day! How may I be of service?",
                "Hey! What's on your mind today?",
                "Hello! I'm ready to help you with any questions."
            ],
            "questions": [
                "That's an interesting question! Let me think about that...",
                "Great question! Here's what I think:",
                "I appreciate you asking! My perspective is:",
                "That's a thoughtful inquiry. In my view:",
                "Excellent question! I'd say that:",
                "I'm glad you asked! From my understanding:"
            ],
            "programming": [
                "Programming is fascinating! Here's my take on that:",
                "That's a great coding question! Let me help:",
                "I love discussing programming! Here's what I suggest:",
                "Coding challenges are fun to solve! Here's an approach:",
                "Programming concepts can be tricky, but here's how I see it:",
                "That's a solid technical question! My thoughts:"
            ],
            "compliments": [
                "Thank you so much! That really means a lot to me.",
                "I appreciate the kind words! You're very thoughtful.",
                "That's incredibly nice of you to say! Thank you.",
                "Your words are very encouraging! I'm grateful.",
                "Thank you for the compliment! You've made my day."
            ],
            "goodbyes": [
                "Goodbye! It was great chatting with you!",
                "Take care! Don't hesitate to reach out again.",
                "Farewell! Hope to talk with you soon.",
                "See you later! Have a wonderful day!",
                "Until next time! Stay curious and keep learning."
            ],
            "general": [
                "That's really interesting! I'd love to explore that further.",
                "I see what you mean. Let me elaborate on that thought.",
                "You raise a good point! Here's another perspective:",
                "That's worth considering! I think about it this way:",
                "Interesting observation! My take on this is:",
                "You've touched on something important there!",
                "That's a valid concern. Let me address that:",
                "I appreciate you sharing that perspective!"
            ]
        }
        
        # Different conversation modes
        self.modes = {
            "friendly": "I'm in friendly mode - casual and warm responses!",
            "professional": "I'm in professional mode - formal and structured responses.",
            "creative": "I'm in creative mode - imaginative and expressive responses!",
            "technical": "I'm in technical mode - detailed and analytical responses.",
            "humorous": "I'm in humorous mode - witty and playful responses!"
        }
    
    def detect_intent(self, user_input: str) -> str:
        """Detect the intent/category of user input."""
        user_input_lower = user_input.lower().strip()
        
        # Greeting patterns
        if any(greeting in user_input_lower for greeting in 
               ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"]):
            return "greetings"
        
        # Question patterns
        if user_input.endswith('?') or any(q_word in user_input_lower for q_word in 
                                           ["what", "how", "why", "when", "where", "who", "can you"]):
            return "questions"
        
        # Programming-related patterns
        if any(prog_word in user_input_lower for prog_word in 
               ["code", "programming", "python", "function", "variable", "algorithm", "debug"]):
            return "programming"
        
        # Compliment patterns
        if any(comp_word in user_input_lower for comp_word in 
               ["thank", "thanks", "great", "awesome", "amazing", "excellent", "wonderful"]):
            return "compliments"
        
        # Goodbye patterns
        if any(bye_word in user_input_lower for bye_word in 
               ["bye", "goodbye", "see you", "farewell", "quit", "exit"]):
            return "goodbyes"
        
        return "general"
    
    def generate_response(self, user_input: str) -> str:
        """Generate a contextual response based on user input."""
        intent = self.detect_intent(user_input)
        base_response = random.choice(self.responses[intent])
        
        # Add mode-specific modifications
        if self.current_mode == "professional":
            base_response = f"I understand your inquiry. {base_response}"
        elif self.current_mode == "creative":
            base_response = f"*sparkles with creativity* {base_response}"
        elif self.current_mode == "humorous":
            base_response = f"{base_response} *winks* 😄"
        elif self.current_mode == "technical":
            base_response = f"Analyzing your input... {base_response}"
        
        return base_response
    
    def change_mode(self, mode: str) -> str:
        """Change the conversation mode of the bot."""
        if mode in self.modes:
            self.current_mode = mode
            return f"Mode changed! {self.modes[mode]}"
        else:
            available_modes = ", ".join(self.modes.keys())
            return f"Invalid mode. Available modes: {available_modes}"
    
    def get_stats(self) -> str:
        """Get conversation statistics."""
        total_exchanges = len(self.conversation_history)
        return f"""Conversation Stats:
- Total exchanges: {total_exchanges}
- Current mode: {self.current_mode}
- Bot name: {self.bot_name}
- User name: {self.user_name}"""
    
    def chat(self, user_input: str) -> str:
        """Main chat method to process user input and generate response."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        # Store conversation history
        self.conversation_history.append({
            "timestamp": timestamp,
            "user": user_input,
            "bot_response": None
        })
        
        # Check for special commands
        if user_input.startswith("/mode "):
            mode = user_input[6:].strip()
            response = self.change_mode(mode)
        elif user_input == "/stats":
            response = self.get_stats()
        elif user_input == "/modes":
            modes_list = "\n".join([f"- {mode}: {desc}" for mode, desc in self.modes.items()])
            response = f"Available modes:\n{modes_list}"
        elif user_input == "/help":
            response = self.get_help()
        else:
            response = self.generate_response(user_input)
        
        # Update conversation history with bot response
        self.conversation_history[-1]["bot_response"] = response
        
        return response
    
    def get_help(self) -> str:
        """Display help information."""
        return """ChatGPT Style Response Bot - Help

Commands:
- /mode [mode_name] : Change conversation mode
- /modes : List available modes
- /stats : Show conversation statistics
- /help : Show this help message
- /quit or /exit : End conversation

Modes: friendly, professional, creative, technical, humorous

Just type anything to start chatting!"""

def main():
    """Main function to run the ChatGPT Style Response Bot CLI."""
    bot = ChatGPTStyleBot()
    
    print("=" * 60)
    print("   ChatGPT Style Random Response Bot")
    print("   Issue #680 - 100 Lines of Python Code")
    print("=" * 60)
    print("Type '/help' for commands or just start chatting!")
    print("Type '/quit' or '/exit' to end the conversation.\n")
    
    while True:
        try:
            # Get user input
            user_input = input(f"{bot.user_name}: ").strip()
            
            # Check for quit commands
            if user_input.lower() in ["/quit", "/exit", "quit", "exit"]:
                print(f"\n{bot.bot_name}: {random.choice(bot.responses['goodbyes'])}")
                break
            
            # Skip empty input
            if not user_input:
                continue
            
            # Add typing delay for realism
            print(f"\n{bot.bot_name}: ", end="", flush=True)
            time.sleep(0.5)  # Simulate thinking time
            
            # Generate and display response
            response = bot.chat(user_input)
            print(response)
            print()  # Empty line for readability
            
        except KeyboardInterrupt:
            print(f"\n\n{bot.bot_name}: Goodbye! Thanks for chatting!")
            break
        except EOFError:
            print(f"\n{bot.bot_name}: Conversation ended. Take care!")
            break

if __name__ == "__main__":
    main()
