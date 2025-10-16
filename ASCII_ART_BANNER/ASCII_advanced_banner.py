# ASCII Banner Generator with Fonts & Colors (Dependency-Based)
# Requires: pyfiglet (pip install pyfiglet)
# Optional: color output in terminal

import pyfiglet

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

def print_banner(text, font="slant", color="white"):
    """Prints text in chosen ASCII font and color"""
    color_code = COLORS.get(color.lower(), COLORS["white"])
    try:
        ascii_text = pyfiglet.figlet_format(text, font=font)
        print(color_code + ascii_text + COLORS["reset"])
    except Exception as e:
        print(f"Error: {e}. Using default font.")
        print(COLORS["white"] + pyfiglet.figlet_format(text) + COLORS["reset"])

def main():
    print("🌟 Advanced ASCII Banner Generator 🌟")
    print("Choose text, font, and color!\n")

    available_fonts = ["slant", "block", "banner", "digital", "starwars"]
    print("Available fonts:", ", ".join(available_fonts))
    print("Available colors:", ", ".join(COLORS.keys() - {"reset"}), "\n")

    while True:
        try:
            text = input("Enter text (or 'q' to quit): ")
            if text.lower() == 'q':
                print("\nGoodbye! Keep creating! 🌟")
                break

            font = input("Choose font: ").strip().lower()
            if font not in available_fonts:
                print("Invalid font! Using default 'slant'.")
                font = "slant"

            color = input("Choose color: ").strip().lower()
            if color not in COLORS:
                print("Invalid color! Defaulting to white.")
                color = "white"

            print_banner(text, font=font, color=color)

        except Exception as e:
            print(f"Error: {e}. Try again.\n")

if __name__ == "__main__":
    main()
