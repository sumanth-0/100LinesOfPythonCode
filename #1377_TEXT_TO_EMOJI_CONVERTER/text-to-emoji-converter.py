import re


emoji_map = {
    'love': '❤️',
    'heart': '❤️',
    'happy': '😊',
    'joy': '😁',
    'sad': '😢',
    'cry': '😭',
    'laugh': '😂',
    'funny': '🤣',
    'angry': '😠',
    'cool': '😎',
    'fire': '🔥',
    'lit': '🔥',
    'star': '⭐',
    'sun': '☀️',
    'moon': '🌙',
    'smile': '😃',
    'grin': '😄',
    'wow': '😲',
    'surprised': '😮',
    'party': '🎉',
    'celebrate': '🥳',
    'cake': '🎂',
    'pizza': '🍕',
    'burger': '🍔',
    'coffee': '☕',
    'tea': '🍵',
    'cat': '🐱',
    'dog': '🐶',
    'bird': '🐦',
    'tree': '🌲',
    'flower': '🌸',
    'rose': '🌹',
    'gift': '🎁',
    'money': '💰',
    'coin': '🪙',
    'check': '✅',
    'cross': '❌',
    'music': '🎵',
    'dance': '💃',
    'sleep': '😴',
    'dream': '💭',
    'phone': '📱',
    'computer': '💻',
    'game': '🎮',
    'book': '📖',
    'pen': '🖊️',
    'rain': '🌧️',
    'snow': '❄️',
    'cloud': '☁️',
    'car': '🚗',
    'bus': '🚌',
    'train': '🚆',
    'plane': '✈️',
    'food': '🍽️',
    'water': '💧',
    'fireworks': '🎆',
    'ball': '⚽',
    'trophy': '🏆',
    'hand': '🤚',
    'clap': '👏',
    'wave': '👋',
    'ok': '👌',
    'thumbs': '👍',
    'sadness': '😔',
    'hug': '🤗',
    'kiss': '😘',
    'baby': '👶',
    'family': '👨‍👩‍👧‍👦',
    'friend': '🫂',
    'rainbow': '🌈',
    'earth': '🌍',
    'starry': '🌌',
    'night': '🌃',
    'city': '🏙️',
    'work': '💼',
    'study': '📚',
    'school': '🏫',
    'house': '🏠',
    'home': '🏡',
    'hospital': '🏥'
}
def replace_words_with_emojis(text):
    """
    Replace common words with their emoji equivalents.
    Case-insensitive replacement while preserving the rest of the text.
    """
   
    result = text
    for word, emoji in emoji_map.items():
        pattern = r'\b' + re.escape(word) + r'\b'
        result = re.sub(pattern, emoji, result, flags=re.IGNORECASE)
    
    return result


def main():
    print("=== Word to Emoji Replacer ===\n")

    
    sample_texts = [
        "I love pizza and coffee!",
        "Happy birthday! Here's a cake and a gift.",
        "The fire is so cool, it's lit!",
        "My dog and cat make me smile with love.",
        "Let's celebrate and dance under the moon and stars!",
        "The rain and rainbow look so beautiful today!"
    ]

    print("Examples:")
    for text in sample_texts:
        converted = replace_words_with_emojis(text)
        print(f"Original:  {text}")
        print(f"Converted: {converted}\n")

    
    print("\n--- Interactive Mode ---")
    print("Enter text to convert (or 'quit' to exit):\n")

    while True:
        user_input = input("> ")
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break

        if user_input.strip():
            result = replace_words_with_emojis(user_input)
            print(f"✨ {result}\n")


if __name__ == "__main__":
    main()
