
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
data = pd.read_csv('spam_dataset.csv')  # Dataset should contain 'message' and 'label' (spam/not spam) columns
X = data['message']
y = data['label']

# Vectorize text data
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(X)

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Initialize and train Naive Bayes classifier
model = MultinomialNB()
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"Model Accuracy: {accuracy * 100:.2f}%")
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Function to predict if a new message is spam or not
def predict_spam(message):
    """Predict if a given message is spam or not."""
    message_vector = vectorizer.transform([message])
    return "Spam" if model.predict(message_vector)[0] == 1 else "Not Spam"

# Example Usage
if __name__ == "__main__":
    message = input("Enter a message to classify: ")
    print("Prediction:", predict_spam(message))
