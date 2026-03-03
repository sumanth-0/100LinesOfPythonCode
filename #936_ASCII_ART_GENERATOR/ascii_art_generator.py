# ascii_art_generator.py
# Renders any text as large ASCII block letters
# Author: Your Name

LETTERS = {
    'A': ["  #  ", " # # ", "#####", "#   #", "#   #"],
    'B': ["#### ", "#   #", "#### ", "#   #", "#### "],
    'C': [" ####", "#    ", "#    ", "#    ", " ####"],
    'D': ["#### ", "#   #", "#   #", "#   #", "#### "],
    'E': ["#####", "#    ", "#### ", "#    ", "#####"],
    'F': ["#####", "#    ", "#### ", "#    ", "#    "],
    'G': [" ####", "#    ", "# ###", "#   #", " ####"],
    'H': ["#   #", "#   #", "#####", "#   #", "#   #"],
    'I': ["#####", "  #  ", "  #  ", "  #  ", "#####"],
    'J': ["#####", "   # ", "   # ", "#  # ", " ##  "],
    'K': ["#   #", "#  # ", "###  ", "#  # ", "#   #"],
    'L': ["#    ", "#    ", "#    ", "#    ", "#####"],
    'M': ["#   #", "## ##", "# # #", "#   #", "#   #"],
    'N': ["#   #", "##  #", "# # #", "#  ##", "#   #"],
    'O': [" ### ", "#   #", "#   #", "#   #", " ### "],
    'P': ["#### ", "#   #", "#### ", "#    ", "#    "],
    'Q': [" ### ", "#   #", "# # #", "#  # ", " ## #"],
    'R': ["#### ", "#   #", "#### ", "#  # ", "#   #"],
    'S': [" ####", "#    ", " ### ", "    #", "#### "],
    'T': ["#####", "  #  ", "  #  ", "  #  ", "  #  "],
    'U': ["#   #", "#   #", "#   #", "#   #", " ### "],
    'V': ["#   #", "#   #", "#   #", " # # ", "  #  "],
    'W': ["#   #", "#   #", "# # #", "## ##", "#   #"],
    'X': ["#   #", " # # ", "  #  ", " # # ", "#   #"],
    'Y': ["#   #", " # # ", "  #  ", "  #  ", "  #  "],
    'Z': ["#####", "   # ", "  #  ", " #   ", "#####"],
    ' ': ["     ", "     ", "     ", "     ", "     "],
}

def render_ascii_art(text: str) -> str:
    """Convert a string to large ASCII block letters."""
    text = text.upper()
    
    # Each letter has 5 rows
    rows = ["", "", "", "", ""]
    
    for char in text:
        if char in LETTERS:
            letter_rows = LETTERS[char]
        else:
            letter_rows = ["?????"] * 5  # Unsupported character
        
        for i in range(5):
            rows[i] += letter_rows[i] + "  "  # Add spacing between letters
    
    return "\n".join(rows)

def main():
    print("=" * 50)
    print("  🎨 ASCII Art Text Generator")
    print("  Type your text below (letters only)")
    print("  Type 'quit' to exit")
    print("=" * 50)
    
    while True:
        user_input = input("\nEnter text: ").strip()
        
        if user_input.lower() == 'quit':
            print("Thanks for using ASCII Art Generator! 👋")
            break
        
        if not user_input:
            print("⚠️  Please enter some text.")
            continue
        
        print("\n" + render_ascii_art(user_input) + "\n")

if __name__ == "__main__":
    main() 