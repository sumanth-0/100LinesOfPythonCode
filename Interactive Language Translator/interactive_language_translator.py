import os
from googletrans import Translator, LANGUAGES

def display_languages():
    print("Available languages:")
    for code, language in LANGUAGES.items():
        print(f"{code}: {language}")

def translate_text(text, dest_language):
    translator = Translator()
    translated = translator.translate(text, dest=dest_language)
    return translated.text

def main():
    print("Welcome to the Interactive Translator!")
    
    while True:
        print("\n1. Display available languages")
        print("2. Translate text")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ")
        
        if choice == '1':
            display_languages()
        elif choice == '2':
            text = input("Enter the text to translate: ")
            display_languages()
            dest_language = input("Enter the language code for translation: ")
            
            if dest_language in LANGUAGES:
                translated_text = translate_text(text, dest_language)
                print(f"Translated Text: {translated_text}")
            else:
                print("Invalid language code. Please try again.")
        elif choice == '3':
            print("Exiting the translator. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
