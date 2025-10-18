"""Color Guess Game - Guess the color from RGB values
Created for issue #1165
A fun game where players guess color names from RGB codes.
"""

import random
import sys

# Color database with RGB values and names
COLORS = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
    "cyan": (0, 255, 255),
    "magenta": (255, 0, 255),
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "orange": (255, 165, 0),
    "purple": (128, 0, 128),
    "pink": (255, 192, 203),
    "brown": (165, 42, 42),
    "gray": (128, 128, 128),
    "lime": (0, 255, 0),
    "navy": (0, 0, 128),
    "teal": (0, 128, 128),
    "maroon": (128, 0, 0),
    "olive": (128, 128, 0),
    "coral": (255, 127, 80),
    "turquoise": (64, 224, 208)
}

class ColorGuessGame:
    def __init__(self):
        self.score = 0
        self.rounds = 0
        self.max_rounds = 10
        
    def display_welcome(self):
        """Display welcome message and game rules."""
        print("\n" + "="*50)
        print("🎨 COLOR GUESS GAME 🎨")
        print("="*50)
        print("\nWelcome! Guess the color name from RGB values.")
        print(f"You'll play {self.max_rounds} rounds.")
        print("RGB format: (Red, Green, Blue) - each 0-255")
        print("="*50 + "\n")
        
    def get_random_color(self):
        """Select a random color from the database."""
        return random.choice(list(COLORS.items()))
        
    def provide_hint(self, rgb):
        """Provide hints based on RGB values."""
        r, g, b = rgb
        hints = []
        
        if r > 200:
            hints.append("High red content")
        if g > 200:
            hints.append("High green content")
        if b > 200:
            hints.append("High blue content")
        if r == g == b:
            hints.append("Equal RGB values (grayscale)")
            
        return ", ".join(hints) if hints else "Mixed color"
        
    def play_round(self):
        """Play a single round of the game."""
        self.rounds += 1
        color_name, rgb_value = self.get_random_color()
        
        print(f"\n--- Round {self.rounds}/{self.max_rounds} ---")
        print(f"RGB Value: {rgb_value}")
        print(f"Hint: {self.provide_hint(rgb_value)}")
        
        guess = input("\nYour guess: ").strip().lower()
        
        if guess == color_name:
            print("✓ Correct! 🎉")
            self.score += 1
            return True
        else:
            print(f"✗ Wrong! The color was '{color_name}'.")
            return False
            
    def display_stats(self):
        """Display game statistics."""
        accuracy = (self.score / self.rounds * 100) if self.rounds > 0 else 0
        print("\n" + "="*50)
        print("📊 GAME STATISTICS")
        print("="*50)
        print(f"Rounds Played: {self.rounds}")
        print(f"Correct Guesses: {self.score}")
        print(f"Accuracy: {accuracy:.1f}%")
        print("="*50 + "\n")

def main():
    game = ColorGuessGame()
    game.display_welcome()
    
    while game.rounds < game.max_rounds:
        try:
            game.play_round()
        except KeyboardInterrupt:
            print("\n\nGame interrupted!")
            break
    
    game.display_stats()
    print("Thanks for playing! 🎨")

if __name__ == "__main__":
    main()
