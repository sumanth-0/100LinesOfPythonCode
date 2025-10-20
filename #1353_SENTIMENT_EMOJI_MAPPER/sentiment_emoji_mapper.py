sentiment_dict = {
    # Positive
    "good": 2, "great": 3, "excellent": 4, "amazing": 4, "awesome": 4, "fantastic": 3, "happy": 2, "love": 6,
    "like": 2, "enjoy": 2, "satisfied": 2, "superb": 3, "positive": 2, "wonderful": 4, "brilliant": 3, "best": 3,
    "nice": 2, "cool": 2, "fun": 2, "helpful": 2, "success": 3, "perfect": 4, "beautiful": 3, "friendly": 2,
    "recommend": 2, "safe": 2, "healthy": 2, "improve": 2,

    # Negative
    "bad": -2, "worse": -3, "worst": -4, "awful": -4, "terrible": -4, "horrible": -4, "sad": -2, "pain": -2,
    "hate": -5, "dislike": -2, "angry": -2, "upset": -2, "fail": -3, "failure": -3, "problem": -2, "issue": -2,
    "negative": -2, "poor": -2, "weak": -2, "danger": -3, "risky": -2, "unhealthy": -2, "unhappy": -2,
    "lost": -2, "broken": -2, "stress": -2, "miss": -2, "mistake": -2, "complain": -2, "regret": -2,
    "wrong": -2, "annoying": -2, "disgust": -3, "unpleasant": -2, "unfortunate": -2
}

emoji_dict = {
    4: "😍",  # Extremely Positive
    3: "😊",  # Positive
    2: "🙂",  # Neutral
    1: "😐",  # Slightly Negative
    -1: "😟",  # Negative
    -2: "😢",  # Very Negative
    -3: "😡",  # Extremely Negative
}

def get_sentiment_score(text):
    words = text.lower().split()
    score = 0
    for word in words:
        score += sentiment_dict.get(word, 0)
    return score

def map_score_to_emoji(score):
    if score >= 8:
        return emoji_dict[4]
    elif score >= 5:
        return emoji_dict[3]
    elif score >= 1:
        return emoji_dict[2]
    elif score == 0:
        return emoji_dict[1]
    elif score <= -8:
        return emoji_dict[-3]
    elif score <= -5:
        return emoji_dict[-2]
    else:
        return emoji_dict[-1]
    
def analyze_text(text):
    score = get_sentiment_score(text)
    emoji = map_score_to_emoji(score)
    return emoji

if __name__ == "__main__":
    text = input("Enter text to analyze sentiment: ")
    sentiment_emoji = analyze_text(text)
    print(f"Sentiment Emoji: {sentiment_emoji}")