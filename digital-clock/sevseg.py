# sevseg.py
# Version simplifiée pour afficher des chiffres en 7 segments ASCII

DIGITS = {
    '0': [" _ ",
          "| |",
          "|_|"],
    '1': ["   ",
          "  |",
          "  |"],
    '2': [" _ ",
          " _|",
          "|_ "],
    '3': [" _ ",
          " _|",
          " _|"],
    '4': ["   ",
          "|_|",
          "  |"],
    '5': [" _ ",
          "|_ ",
          " _|"],
    '6': [" _ ",
          "|_ ",
          "|_|"],
    '7': [" _ ",
          "  |",
          "  |"],
    '8': [" _ ",
          "|_|",
          "|_|"],
    '9': [" _ ",
          "|_|",
          " _|"]
}

def getSevSegStr(number, minWidth=1):
    """Retourne une chaîne ASCII représentant le nombre (entier ou chaîne)."""
    numStr = str(number).rjust(minWidth, '0')
    lines = ["", "", ""]
    for digit in numStr:
        seg = DIGITS.get(digit, ["   ", "   ", "   "])
        for i in range(3):
            lines[i] += seg[i] + " "
    return "\n".join(lines)
