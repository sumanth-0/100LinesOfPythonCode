#!/usr/bin/env python3
"""
Song Mood Predictor
Predicts the mood of a song (happy/sad/energetic) based on lyrics sentiment analysis.
"""

import re
from collections import Counter
import sys

# Define mood-related keywords
MOOD_KEYWORDS = {
    'happy': [
        'joy', 'happy', 'love', 'smile', 'laugh', 'dancing', 'celebration', 'sunshine',
        'bright', 'fun', 'cheerful', 'excited', 'wonderful', 'amazing', 'fantastic',
        'beautiful', 'lovely', 'sweet', 'party', 'celebrate', 'delight', 'bliss'
    ],
    'sad': [
        'sad', 'cry', 'tears', 'lonely', 'heartbreak', 'pain', 'sorrow', 'lost',
        'broken', 'empty', 'darkness', 'goodbye', 'hurt', 'miss', 'alone', 'regret',
        'grief', 'melancholy', 'despair', 'suffering', 'anguish', 'mourn'
    ],
    'energetic': [
        'run', 'jump', 'power', 'strong', 'energy', 'fire', 'wild', 'alive',
        'fight', 'rise', 'thunder', 'lightning', 'explosive', 'fierce', 'intense',
        'electric', 'adrenaline', 'unstoppable', 'dynamic', 'vigorous', 'action'
    ]
}


def preprocess_lyrics(lyrics):
    """Clean and tokenize lyrics."""
    # Convert to lowercase
    lyrics = lyrics.lower()
    # Remove punctuation and special characters
    lyrics = re.sub(r'[^a-z\s]', '', lyrics)
    # Split into words
    words = lyrics.split()
    return words


def calculate_mood_scores(words):
    """Calculate mood scores based on keyword frequency."""
    mood_scores = {mood: 0 for mood in MOOD_KEYWORDS}
    
    # Count occurrences of mood keywords
    for word in words:
        for mood, keywords in MOOD_KEYWORDS.items():
            if word in keywords:
                mood_scores[mood] += 1
    
    return mood_scores


def predict_mood(lyrics):
    """Predict the mood of a song based on lyrics."""
    words = preprocess_lyrics(lyrics)
    mood_scores = calculate_mood_scores(words)
    
    # Find the mood with the highest score
    predicted_mood = max(mood_scores, key=mood_scores.get)
    max_score = mood_scores[predicted_mood]
    
    # If no mood keywords found, return neutral
    if max_score == 0:
        return 'neutral', mood_scores
    
    return predicted_mood, mood_scores


def display_results(lyrics, mood, scores):
    """Display the prediction results."""
    print("\n" + "="*50)
    print("SONG MOOD PREDICTOR")
    print("="*50)
    print(f"\nLyrics (first 100 chars): {lyrics[:100]}...")
    print(f"\nPredicted Mood: {mood.upper()}")
    print("\nMood Scores:")
    for m, score in scores.items():
        print(f"  {m.capitalize()}: {score}")
    print("="*50 + "\n")


def main():
    """Main function to run the Song Mood Predictor."""
    if len(sys.argv) > 1:
        # Lyrics provided as command-line argument
        lyrics = ' '.join(sys.argv[1:])
    else:
        # Interactive mode
        print("Song Mood Predictor")
        print("Enter song lyrics (press Enter twice to finish):")
        lines = []
        while True:
            try:
                line = input()
                if line == "":
                    break
                lines.append(line)
            except EOFError:
                break
        lyrics = ' '.join(lines)
    
    if not lyrics.strip():
        print("Error: No lyrics provided!")
        return
    
    # Predict mood
    mood, scores = predict_mood(lyrics)
    
    # Display results
    display_results(lyrics, mood, scores)


if __name__ == "__main__":
    main()
