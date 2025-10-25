def main():
    print("Indian Language Translator")
    print("This tool translates text between Indian languages using Google Translate.")
    
    try:
        from googletrans import Translator
    except ImportError:
        print("\nError: The 'googletrans' library is missing.")
        print("Please install it by running: pip install googletrans==4.0.0-rc1")
        return

    translator = Translator()
    
    print("\nSupported Indian Languages:")
    indian_languages = {
        'hi': 'Hindi', 'bn': 'Bengali', 'te': 'Telugu', 'mr': 'Marathi',
        'ta': 'Tamil', 'ur': 'Urdu', 'gu': 'Gujarati', 'kn': 'Kannada',
        'ml': 'Malayalam', 'pa': 'Punjabi', 'or': 'Odia', 'as': 'Assamese'
    }
    
    for code, name in indian_languages.items():
        print(f"  {code}: {name}")
    
    print("\nYou can also use 'en' for English.")
    print("Type 'exit' to quit the program.")

    while True:
        text = input("\nEnter the text to translate: ")
        if text.lower() == 'exit':
            break

        src_lang = input("Enter the source language code (e.g., 'en' for English, 'hi' for Hindi): ")
        if src_lang.lower() == 'exit':
            break

        dest_lang = input("Enter the destination language code (e.g., 'hi' for Hindi, 'ta' for Tamil): ")
        if dest_lang.lower() == 'exit':
            break

        print("\nTranslating...")
        
        try:
            result = translator.translate(text, src=src_lang, dest=dest_lang)
            
            print("\n Translation Result ")
            print("Original (" + result.src + "): " + result.origin)
            print("Translated (" + result.dest + "): " + result.text)
            print("\n")

        except Exception as e:
            print("\nSorry, an error occurred.")
            print("Please check your internet connection and the language codes you entered.")
            print("Details: " + str(e))

    print("\nGoodbye!")

if __name__ == "__main__":
    main()