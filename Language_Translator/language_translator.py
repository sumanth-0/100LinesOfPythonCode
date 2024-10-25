from googletrans import Translator

def translate_text(text, dest_lang):
    translator = Translator()
    try:
        # Detect the input language
        detected_lang = translator.detect(text).lang
        print(f"\nDetected language: {detected_lang.upper()}")
        
        # Translate the text
        translated = translator.translate(text, dest=dest_lang)
        print(f"Translated to {dest_lang.upper()}: {translated.text}")
        
    except Exception as e:
        print(f"Error: {str(e)}")

def display_language_codes():
    print("\nCommon Language Codes:")
    print(" - 'en' : English")
    print(" - 'es' : Spanish")
    print(" - 'fr' : French")
    print(" - 'de' : German")
    print(" - 'it' : Italian")
    print(" - 'zh-cn' : Chinese (Simplified)")
    print(" - 'ja' : Japanese")
    print(" - 'ko' : Korean")
    print(" - 'hi' : Hindi")
    print(" - 'ar' : Arabic")
    print(" - 'ru' : Russian")

def main():
    print("Welcome to the Language Translator!")
    
    while True:
        # Get user input
        text = input("\nEnter the text you want to translate (or type 'exit' to quit): ")
        
        if text.lower() == 'exit':
            print("Exiting the translator. Goodbye!")
            break

        # Display common language codes for ease
        display_language_codes()
        
        dest_lang = input("Enter the language code to translate to: ")

        if dest_lang.strip():
            # Perform translation
            translate_text(text, dest_lang)
        else:
            print("Invalid language code. Please try again.")

if __name__ == "__main__":
    main()
