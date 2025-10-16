import random

def create_stylized_art(text, symbol="*"):
    """
    Converts input text into a stylized pattern using repeated letters 
    or symbols.
    """
    art_output = []
    text = text.upper() # Use uppercase for consistent block art

    for char in text:
        # 1. Base pattern (using the character itself)
        char_pattern = f"{char * 3} {char} {char * 3}"
        
        # 2. Border/Styling pattern (using the chosen symbol)
        # Randomly choose a styling option for variety
        style_choice = random.randint(1, 3)
        
        if style_choice == 1:
            line = f"{symbol*2} {char_pattern} {symbol*2}"
        elif style_choice == 2:
            line = f"<{char_pattern}>"
        else:
            line = f"|{char}| {char_pattern} |{char}|"
            
        art_output.append(line)
        
    return "\n".join(art_output)

# Example Usage
if __name__ == "__main__":
    user_text = input("Enter text to stylize: ")
    
    # Simple output
    print("\n--- Stylized Output ---")
    print(create_stylized_art(user_text, symbol="#"))
    print("-----------------------\n")