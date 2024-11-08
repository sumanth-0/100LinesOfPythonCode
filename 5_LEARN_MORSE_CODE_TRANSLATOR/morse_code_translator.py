MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', 
    '9': '----.', '0': '-----', ' ': '/'
}

def text_to_morse(text):
    return ' '.join(MORSE_CODE_DICT.get(char.upper(), '?') for char in text)

def morse_to_text(morse):
    reverse_dict = {v: k for k, v in MORSE_CODE_DICT.items()}
    return ''.join(reverse_dict.get(code, '?') for code in morse.split())

def morse_quiz():
    sample_text = "HELLO WORLD"
    print("Translate this to Morse Code: HELLO WORLD")
    user_input = input("Your translation: ")
    if user_input.strip() == text_to_morse(sample_text):
        print("Correct!")
    else:
        print(f"Incorrect! Correct Morse Code: {text_to_morse(sample_text)}")

def main():
    print("1. Text to Morse\n2. Morse to Text\n3. Quiz Mode")
    choice = input("Choose an option: ")
    if choice == '1':
        text = input("Enter text to translate: ")
        print(f"Morse Code: {text_to_morse(text)}")
    elif choice == '2':
        morse = input("Enter Morse Code (use spaces between letters): ")
        print(f"Translated Text: {morse_to_text(morse)}")
    elif choice == '3':
        morse_quiz()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
