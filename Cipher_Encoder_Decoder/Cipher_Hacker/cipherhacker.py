import nltk
from nltk.corpus import words
from nltk import word_tokenize
from nltk import pos_tag

# Load the set of English words
english_words = set(words.words())

def decode_caesar(ciphertext, shift):
    decoded = []
    for char in ciphertext:
        if char.isalpha():
            shift_base = ord('a') if char.islower() else ord('A')
            decoded_char = chr((ord(char) - shift_base - shift) % 26 + shift_base)
            decoded.append(decoded_char)
        else:
            decoded.append(char)  # Non-alpha characters remain unchanged
    return ''.join(decoded)

def evaluate_shift(decoded_message):
    tokens = word_tokenize(decoded_message)
    # Count recognized English words
    score = sum(1 for word in tokens if word.lower() in english_words)
    return score

def find_best_shift(ciphertext):
    best_shift = 0
    highest_score = 0

    for shift in range(1, 26):
        decoded_message = decode_caesar(ciphertext, shift)
        score = evaluate_shift(decoded_message)

        if score > highest_score:
            highest_score = score
            best_shift = shift

    return best_shift

if __name__ == "__main__":
    while True:
        mode = input("Enter the type of input (file/text): ").strip().lower()

        if mode == "file":
            filename = input("Enter the name of the file (or press Enter to use 'encoded_file.txt'): ")
            if not filename: 
                filename = 'encoded_file.txt'
            
            try:
                with open(filename, 'r') as file:
                    encoded_text = file.read()
                break  
            except FileNotFoundError:
                print(f"Error: The file '{filename}' was not found. Please try again.")
                
        elif mode == "text":
            encoded_text = input("Enter the text: ")
            break   
            
        else:
            print("Invalid mode selected. Please enter 'file' or 'text'.")



        
    best_shift = find_best_shift(encoded_text)
    print(f'The shift used was: {best_shift}')
    print(f'Decoded message: {decode_caesar(encoded_text,best_shift)}')
