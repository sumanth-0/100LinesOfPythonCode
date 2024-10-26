# Morse Code Dictionary
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
    '8': '---..', '9': '----.', '0': '-----', ' ': '/'
}

def text_to_morse(text):
    return ' '.join(morse_code_dict.get(char.upper(), '') for char in text)

def morse_to_text(morse):
    reversed_dict = {value: key for key, value in morse_code_dict.items()}
    return ''.join(reversed_dict.get(code, '') for code in morse.split(' '))

def main():
    while True:
        choice = input("Type '1' to convert text to Morse code or '2' to convert Morse code to text (or 'q' to quit): ")
        
        if choice == '1':
            text = input("Enter text to convert to Morse code: ")
            print(f"Morse Code: {text_to_morse(text)}")
        elif choice == '2':
            morse = input("Enter Morse code to convert to text: ")
            print(f"Text: {morse_to_text(morse)}")
        elif choice.lower() == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
