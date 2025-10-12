# mini_spam_classifier.py
# A simple SMS spam/ham classifier using Naive Bayes

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Sample SMS messages
messages = [
    "Free entry in 2 a wkly comp to win FA Cup final tkts",
    "Upto 20% discount on your next purchase",
    "Hey, are we meeting today?",
    "Call me when you are free",
    "Congratulations! You've won a $1000 gift card",
    "Can we have a call tomorrow?",
    "Win cash now!!! Click here",
    "Don't forget the meeting at 10 AM",
    "You have been selected for a prize",
    "Let's grab lunch today"
]

# Labels: 1 for spam, 0 for ham
labels = [1, 1, 0, 0, 1, 0, 1, 0, 1, 0]

# Convert text to features
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(messages)

# Train Naive Bayes classifier
model = MultinomialNB()
model.fit(X, labels)

# Function to predict new messages
def predict_messages(new_msgs):
    X_new = vectorizer.transform(new_msgs)
    preds = model.predict(X_new)
    for msg, pred in zip(new_msgs, preds):
        label = "Spam" if pred == 1 else "Ham"
        print(f"Message: {msg}\nPrediction: {label}\n")

# Example usage
if __name__ == "__main__":
    test_msgs = [
        "Congratulations, you won a lottery!",
        "Are we meeting for dinner tonight?",
        "Claim your free prize now!"
    ]
    predict_messages(test_msgs)
