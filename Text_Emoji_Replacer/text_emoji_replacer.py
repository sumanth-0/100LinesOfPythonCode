"""
Text Emoji Replacer
Replace keywords in text with emojis (e.g., "happy" -> 😊) using a small dictionary.
Uses only Python's built-in libraries - no external dependencies required.
"""

import re
import sys

# Emoji dictionary mapping keywords to emojis (65+ mappings)
EMOJI_DICT = {
    'happy': '😊', 'sad': '😢', 'love': '❤️', 'heart': '❤️', 'fire': '🔥',
    'smile': '😊', 'laugh': '😂', 'cry': '😭', 'angry': '😠', 'cool': '😎',
    'think': '🤔', 'wow': '😮', 'sleep': '😴', 'sick': '🤢', 'scared': '😱',
    'party': '🎉', 'cake': '🎂', 'gift': '🎁', 'music': '🎵', 'star': '⭐',
    'sun': '☀️', 'moon': '🌙', 'cloud': '☁️', 'rain': '🌧️', 'snow': '❄️',
    'flower': '🌸', 'tree': '🌳', 'cat': '🐱', 'dog': '🐶', 'bird': '🐦',
    'fish': '🐟', 'pizza': '🍕', 'burger': '🍔', 'coffee': '☕', 'beer': '🍺',
    'wine': '🍷', 'apple': '🍎', 'banana': '🍌', 'grapes': '🍇', 'car': '🚗',
    'plane': '✈️', 'rocket': '🚀', 'bike': '🚲', 'train': '🚂', 'house': '🏠',
    'building': '🏢', 'school': '🏫', 'hospital': '🏥', 'church': '⛪',
    'phone': '📱', 'computer': '💻', 'camera': '📷', 'book': '📚', 'pen': '✒️',
    'money': '💰', 'dollar': '💵', 'gem': '💎', 'crown': '👑', 'trophy': '🏆',
    'check': '✅', 'cross': '❌', 'warning': '⚠️', 'question': '❓', 'idea': '💡',
    'thumbs up': '👍', 'thumbs down': '👎', 'clap': '👏', 'wave': '👋', 'punch': '👊'
}


def replace_with_emojis(text):
    """
    Replaces keywords in text with corresponding emojis (case-insensitive).
    
    Args:
        text (str): The input text to process
        
    Returns:
        str: Text with keywords replaced by emojis
    """
    result = text
    # Sort by length (longest first) to handle multi-word phrases correctly
    for keyword in sorted(EMOJI_DICT.keys(), key=len, reverse=True):
        pattern = r'\b' + re.escape(keyword) + r'\b'
        result = re.sub(pattern, EMOJI_DICT[keyword], result, flags=re.IGNORECASE)
    return result


def process_file(input_path, output_path=None):
    """Processes a text file and replaces keywords with emojis."""
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            text = f.read()
        
        converted_text = replace_with_emojis(text)
        
        if output_path:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(converted_text)
            print(f"✅ Converted text saved to: {output_path}")
        else:
            print("\n" + "=" * 60)
            print("Converted Text:")
            print("=" * 60)
            print(converted_text)
            print("=" * 60)
        
        return converted_text
        
    except FileNotFoundError:
        print(f"❌ Error: File '{input_path}' not found.")
    except Exception as e:
        print(f"❌ Error: {str(e)}")


def main():
    """Main function to handle user input and text conversion."""
    print("=" * 60)
    print("Text Emoji Replacer 😊")
    print("=" * 60)
    
    if len(sys.argv) > 1:
        # Command-line mode
        output_path = sys.argv[2] if len(sys.argv) > 2 else None
        process_file(sys.argv[1], output_path)
    else:
        # Interactive mode
        choice = input("\n1. Convert text file\n2. Convert text input\nChoose (1/2): ").strip()
        
        if choice == '1':
            input_path = input("Enter input file path: ").strip()
            save = input("Save to file? (y/n): ").strip().lower()
            output_path = input("Enter output file path: ").strip() if save == 'y' else None
            process_file(input_path, output_path)
        else:
            text = input("\nEnter text to convert: ").strip()
            print(f"\nConverted: {replace_with_emojis(text)}")


if __name__ == "__main__":
    main()