from pyfiglet import Figlet

# Create a Figlet renderer using a specific font.
# You can list available fonts with: Figlet().getFonts()
# 'isometric1' is a blocky 3D-style font.
f = Figlet(font='isometric1')


def text_to_ascii():
    """
    Prompt the user for text, convert it to ASCII art using pyfiglet,
    print the result, and then prompt again.

    Behavior:
    - If the input is an empty string, the function returns (ends the program).
    - Otherwise, the ASCII art is printed and the function calls itself again
      (simple recursion) to keep the loop going.

    Notes:
    - This uses recursion as a quick way to repeat the prompt. For long sessions,
      an iterative loop (while True) is usually safer to avoid deep recursion.
    """
    # Ask the user for input. Leaving it blank exits the program.
    text = input("Please enter the text to be converted to ASCII:\n"
                 "Leave blank to exit.\n- ")

    # If the user pressed Enter without typing anything, stop.
    if text == "":
        exit()
    else:
        # Render the input text as ASCII art and print it.
        print(f.renderText(text))
        # Ask again by calling the function recursively.
        text_to_ascii()


# Start the program by calling the function once.
text_to_ascii()
