#!/usr/bin/env python3
"""Emoji Translator - Convert text to emojis and vice versa!"""
import sys
import re

# Comprehensive emoji dictionary
EMOJI_DICT = {
    # Emotions
    'love': '❤️', 'heart': '❤️', 'like': '👍', 'happy': '😊', 'sad': '😢', 'angry': '😠',
    'laugh': '😂', 'smile': '😊', 'cry': '😭', 'cool': '😎', 'wink': '😉', 'kiss': '😘',
    'excited': '🤩', 'worried': '😟', 'surprised': '😲', 'thinking': '🤔',
    # Food
    'pizza': '🍕', 'burger': '🍔', 'fries': '🍟', 'coffee': '☕', 'tea': '🍵', 'beer': '🍺',
    'wine': '🍷', 'cake': '🎂', 'cookie': '🍪', 'apple': '🍎', 'banana': '🍌', 'taco': '🌮',
    'sushi': '🍣', 'ramen': '🍜', 'bread': '🍞', 'cheese': '🧀', 'egg': '🥚', 'chicken': '🍗',
    # Nature
    'sun': '☀️', 'moon': '🌙', 'star': '⭐', 'cloud': '☁️', 'rain': '🌧️', 'snow': '❄️',
    'fire': '🔥', 'water': '💧', 'tree': '🌳', 'flower': '🌸', 'rose': '🌹', 'earth': '🌍',
    # Animals
    'cat': '🐱', 'dog': '🐶', 'bird': '🐦', 'fish': '🐟', 'monkey': '🐵', 'lion': '🦁',
    'tiger': '🐯', 'bear': '🐻', 'panda': '🐼', 'koala': '🐨', 'frog': '🐸', 'pig': '🐷',
    # Activities
    'party': '🎉', 'music': '🎵', 'dance': '💃', 'football': '⚽', 'basketball': '🏀',
    'game': '🎮', 'movie': '🎬', 'book': '📚', 'gift': '🎁', 'celebrate': '🎊',
    # Objects
    'phone': '📱', 'computer': '💻', 'car': '🚗', 'plane': '✈️', 'rocket': '🚀', 'home': '🏠',
    'key': '🔑', 'money': '💰', 'crown': '👑', 'trophy': '🏆', 'clock': '🕐', 'bell': '🔔',
    # People & Body
    'king': '🤴', 'queen': '👸', 'baby': '👶', 'boy': '👦', 'girl': '👧', 'man': '👨',
    'woman': '👩', 'family': '👨‍👩‍👧‍👦', 'hand': '✋', 'ok': '👌', 'yes': '👍', 'no': '👎',
    # Symbols
    'check': '✅', 'cross': '❌', 'warning': '⚠️', 'stop': '🛑', 'question': '❓',
    'exclamation': '❗', 'plus': '➕', 'minus': '➖', 'multiply': '✖️', 'hundred': '💯',
}

def text_to_emoji(text):
    """Convert text to emojis."""
    result = text.lower()
    for word, emoji in sorted(EMOJI_DICT.items(), key=lambda x: len(x[0]), reverse=True):
        result = re.sub(r'\b' + re.escape(word) + r'\b', emoji, result, flags=re.IGNORECASE)
    return result

def emoji_to_text(text):
    """Convert emojis back to text."""
    result = text
    reverse_dict = {v: k for k, v in EMOJI_DICT.items()}
    for emoji, word in reverse_dict.items():
        result = result.replace(emoji, f'[{word}]')
    return result

def interactive_mode():
    """Run interactive emoji translator."""
    print("\n✨ Welcome to Emoji Translator! ✨")
    print("Commands: 'quit' to exit, 'reverse' to toggle mode, 'help' for help\n")
    mode = 'text2emoji'
    
    while True:
        mode_display = "Text→Emoji" if mode == 'text2emoji' else "Emoji→Text"
        user_input = input(f"[{mode_display}] Enter text: ").strip()
        
        if not user_input:
            continue
        if user_input.lower() == 'quit':
            print("👋 Goodbye!")
            break
        elif user_input.lower() == 'reverse':
            mode = 'emoji2text' if mode == 'text2emoji' else 'text2emoji'
            print(f"🔄 Switched to {mode_display} mode!")
            continue
        elif user_input.lower() == 'help':
            print("\n📖 Help: Enter text to convert to emojis or vice versa.")
            print("   Sample words: love, pizza, happy, cat, party, sun, etc.")
            print("   Type 'reverse' to switch modes, 'quit' to exit.\n")
            continue
        
        if mode == 'text2emoji':
            result = text_to_emoji(user_input)
        else:
            result = emoji_to_text(user_input)
        
        print(f"✨ Result: {result}\n")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Command-line argument mode
        input_text = ' '.join(sys.argv[1:])
        print(text_to_emoji(input_text))
    else:
        # Interactive mode
        interactive_mode()
