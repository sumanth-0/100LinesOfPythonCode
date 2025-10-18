from textblob import TextBlob

def analyze_mood(sentence):
    analysis = TextBlob(sentence)
    if analysis.sentiment.polarity > 0.1:
        return "Happy 😊"
    elif analysis.sentiment.polarity < -0.1:
        return "Sad 😢"
    else:
        return "Neutral 😐"

sentences_to_test = [
    "I am incredibly happy and excited about this new project!",
    "This is a wonderful and amazing day.",
    "The weather is cloudy today.",
    "I feel terrible and my heart is broken.",
    "He completely failed the exam and felt miserable.",
    "This document contains the required information."
]

print("--- Mood Summary ---")
for sentence in sentences_to_test:
    mood = analyze_mood(sentence)
    print(f"Sentence: '{sentence}'")
    print(f"Mood: {mood}\n")