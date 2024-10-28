import demoji

def convert_text_to_emoji(text):
    """Convert text to emojis using the demoji module."""
    return demoji.replace(text)

def main():
    """Run the words to emoji generator."""
    print("Welcome to the Words to Emoji Generator!")
    
    while True:
        user_input = input("\nEnter text to convert to emojis (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        emoji_text = convert_text_to_emoji(user_input)
        print("Converted Text:", emoji_text)

if __name__ == "__main__":
    demoji.download()  # Download demoji mapping data
    main()
