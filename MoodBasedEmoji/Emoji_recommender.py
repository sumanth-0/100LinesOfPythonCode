import re

# Mood words to emoji mappings (expandable)
MOOD_EMOJIS = {
    'happy': '😊', 'joy': '😄', 'excited': '🎉', 'love': '❤️', 'great': '👍',
    'amazing': '✨', 'awesome': '🚀', 'fun': '😂', 'laugh': '🤣', 'smile': '😀',
    'sad': '😢', 'depressed': '😔', 'down': '😞', 'hurt': '💔', 'cry': '😭',
    'angry': '😠', 'mad': '🤬', 'furious': '🔥', 'hate': '👎', 'frustrated': '😤',
    'surprised': '😲', 'shocked': '⚡', 'wow': '🤯', 'fear': '😱', 'scared': '👻',
    'calm': '😌', 'relaxed': '🧘', 'peace': '☮️', 'chill': '❄️', 'tired': '😴',
    'bored': '😑', 'confused': '🤔', 'puzzled': '🧐', 'grateful': '🙏', 'blessed': '🌟'
}

def detect_moods(text):
    """Detect mood words in text (case-insensitive)."""
    text_lower = text.lower()
    words = re.findall(r'\b\w+\b', text_lower)
    detected = set()
    for word in words:
        if word in MOOD_EMOJIS:
            detected.add(word)
    return list(detected)

def recommend_emojis(text, num_suggestions=3):
    """Recommend emojis based on detected moods."""
    moods = detect_moods(text)
    if not moods:
        return ['🤷'] * num_suggestions  # Default neutral if no moods detected
    
    # Get unique emojis for detected moods
    emojis = [MOOD_EMOJIS[mood] for mood in moods]
    # If more than num_suggestions, pick random or first
    if len(emojis) > num_suggestions:
        emojis = emojis[:num_suggestions]
    elif len(emojis) < num_suggestions:
        # Pad with neutral
        emojis.extend(['🤷'] * (num_suggestions - len(emojis)))
    return emojis

def main():
    print("Emoji Mood Recommender")
    text = input("Enter text: ").strip()
    if not text:
        print("No text provided.")
        return
    
    emojis = recommend_emojis(text)
    print(f"\nDetected moods: {detect_moods(text)}")
    print("Recommended emojis:", ' '.join(emojis))

if __name__ == "__main__":
    main()
