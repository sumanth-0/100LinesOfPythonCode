import random
import time
from typing import List, Tuple

# Color database with RGB values
COLORS = {
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'yellow': (255, 255, 0),
    'purple': (128, 0, 128),
    'orange': (255, 165, 0),
    'pink': (255, 192, 203),
    'brown': (165, 42, 42),
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'gray': (128, 128, 128),
    'cyan': (0, 255, 255),
    'magenta': (255, 0, 255),
    'lime': (0, 255, 0),
    'navy': (0, 0, 128)
}

def display_welcome():
    """Display welcome message and game instructions."""
    print("\n" + "="*50)
    print("    🎨 WELCOME TO THE COLOR GUESS GAME! 🎨")
    print("="*50)
    print("\nRules:")
    print("- I'll show you RGB values")
    print("- You guess the color name")
    print("- Get points for correct answers")
    print("- Type 'quit' to exit\n")

def get_color_hint(rgb: Tuple[int, int, int]) -> str:
    """Generate a hint based on RGB values."""
    r, g, b = rgb
    hints = []
    if r > 200: hints.append("high red")
    if g > 200: hints.append("high green")
    if b > 200: hints.append("high blue")
    if r < 50 and g < 50 and b < 50: hints.append("very dark")
    if r > 200 and g > 200 and b > 200: hints.append("very light")
    return ", ".join(hints) if hints else "moderate values"

def play_round(color_list: List[str]) -> Tuple[bool, str]:
    """Play one round of the game."""
    correct_color = random.choice(color_list)
    rgb = COLORS[correct_color]
    
    print(f"\n🎯 RGB: {rgb}")
    print(f"💡 Hint: {get_color_hint(rgb)}")
    
    guess = input("\nYour guess: ").lower().strip()
    
    if guess == 'quit':
        return False, ''
    
    if guess == correct_color:
        print("✅ Correct! Well done!")
        return True, correct_color
    else:
        print(f"❌ Wrong! The correct answer was: {correct_color}")
        return False, correct_color

def main():
    """Main game loop."""
    display_welcome()
    
    color_list = list(COLORS.keys())
    score = 0
    rounds = 0
    
    while True:
        result, color = play_round(color_list)
        
        if color == '':  # User quit
            break
        
        rounds += 1
        if result:
            score += 1
        
        print(f"\n📊 Score: {score}/{rounds}")
        
        continue_game = input("\nPlay another round? (yes/no): ").lower().strip()
        if continue_game not in ['yes', 'y']:
            break
    
    print("\n" + "="*50)
    print(f"    🏆 GAME OVER! Final Score: {score}/{rounds}")
    if rounds > 0:
        percentage = (score / rounds) * 100
        print(f"    Accuracy: {percentage:.1f}%")
    print("="*50)
    print("Thanks for playing! 🎨\n")

if __name__ == "__main__":
    main()
