
#  Slash-Style ASCII Banner Generator 
# ASCII mapping for A-Z and 0-9 (slash-style)
SLASH_ART = {
    "A": ["   /\\   ", "  /  \\  ", " /----\\ ", "/      \\", "/      \\"],
    "B": ["|----\\ ", "|     |", "|----/ ", "|     \\", "|-----/"],
    "C": [" /----\\", "/      ", "|      ", "\\      ", " \\----/"],
    "D": ["|----\\ ", "|     |", "|     |", "|     |", "|----/ "],
    "E": ["|-----", "|     ", "|---- ", "|     ", "|-----"],
    "F": ["|-----", "|     ", "|---- ", "|     ", "|     "],
    "G": [" /----\\", "/      ", "|  ---|", "\\     |", " \\---/ "],
    "H": ["|    |", "|    |", "|----|", "|    |", "|    |"],
    "I": ["-----", "  |  ", "  |  ", "  |  ", "-----"],
    "J": ["     |", "     |", "     |", "|    |", " \\--/ "],
    "K": ["|   /", "|  / ", "|-/  ", "|  \\ ", "|   \\"],
    "L": ["|     ", "|     ", "|     ", "|     ", "|-----"],
    "M": ["|\\    /|", "| \\  / |", "|  \\/  |", "|      |", "|      |"],
    "N": ["|\\    |", "| \\   |", "|  \\  |", "|   \\ |", "|    \\|"],
    "O": [" /----\\ ", "/      \\", "|      |", "\\      /", " \\----/ "],
    "P": ["|----\\ ", "|     |", "|----/ ", "|      ", "|      "],
    "Q": [" /----\\ ", "/      \\", "|      |", "\\    / ", " \\--\\  "],
    "R": ["|----\\ ", "|     |", "|----/ ", "|   \\ ", "|    \\"],
    "S": [" /----\\", "|      ", " \\---\\ ", "      |", " \\---/"],
    "T": ["-----", "  |  ", "  |  ", "  |  ", "  |  "],
    "U": ["|    |", "|    |", "|    |", "|    |", " \\--/ "],
    "V": ["\\    /", " \\  / ", "  \\/  ", "  ||  ", "  ||  "],
    "W": ["|      |", "|      |", "|  /\\  |", "| /  \\ |", "|/    \\|"],
    "X": ["\\    /", " \\  / ", "  ||  ", " /  \\ ", "/    \\"],
    "Y": ["\\   /", " \\ / ", "  |  ", "  |  ", "  |  "],
    "Z": ["-----", "   / ", "  /  ", " /   ", "-----"],
    "0": [" /--\\ ", "/    \\", "|    |", "\\    /", " \\--/ "],
    "1": ["  |  ", " ||  ", "  |  ", "  |  ", " ||| "],
    "2": [" /--\\ ", "     |", "  /-- ", " |    ", " ---- "],
    "3": [" /--\\ ", "     |", "  --< ", "     |", " \\--/ "],
    "4": ["|   | ", "|   | ", " ----|", "     |", "     |"],
    "5": [" ---- ", "|     ", " ---\\ ", "     |", " ---/ "],
    "6": [" /--\\ ", "|     ", "| ---\\", "|    |", " \\--/ "],
    "7": ["-----", "    /", "   / ", "  /  ", " /   "],
    "8": [" /--\\ ", "|    |", " \\--/ ", "|    |", " \\--/ "],
    "9": [" /--\\ ", "|    |", " \\--/ ", "     |", " \\--/ "],
    " ": ["      ", "      ", "      ", "      ", "      "]
}

# ANSI color codes
COLORS = {
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "magenta": "\033[95m",
    "cyan": "\033[96m",
    "white": "\033[97m",
    "reset": "\033[0m"
}

def print_slash_banner(text, char_color="white"):
    """Prints text in slash-style ASCII banner with optional color"""
    color_code = COLORS.get(char_color.lower(), COLORS["white"])
    text = text.upper()
    for i in range(5):
        line = ""
        for char in text:
            art = SLASH_ART.get(char, SLASH_ART[" "])[i]
            line += color_code + art + COLORS["reset"] + "  "
        print(line)
    print("\n")

def main():
    print("🌟 Slash-Style ASCII Banner Generator 🌟")
    print("Type your text and see it in a stylish slash-style banner!")
    print("You can choose a color: red, green, yellow, blue, magenta, cyan, white\n")

    while True:
        try:
            user_input = input("Enter text (or 'q' to quit): ")
            if user_input.lower() == 'q':
                print("\nGoodbye! Keep creating! 🌟")
                break
            color_input = input("Choose color: ").strip().lower()
            if color_input not in COLORS:
                print("Invalid color! Defaulting to white.\n")
                color_input = "white"
            print_slash_banner(user_input, char_color=color_input)
        except Exception as e:
            print(f"Error: {e}. Try again!\n")

if __name__ == "__main__":
    main()
