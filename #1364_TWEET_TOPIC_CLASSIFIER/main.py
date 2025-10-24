import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split

try:
    df = pd.read_csv("https://storage.googleapis.com/dataset-uploader/bbc/bbc-text.csv")
    desired_categories = ['sport', 'politics', 'entertainment']
    df = df[df['category'].isin(desired_categories)].copy()

    print(f"Data cleaned. Using only categories: {df['category'].unique().tolist()}")

    df['category'] = df['category'].str.capitalize()
    texts = df['text'].tolist()
    labels = df['category'].tolist()
except Exception as e:
    print(f"Failed to load data. Using fallback sample data. Error: {e}")
    texts = [
        "What a goal by Messi! Unbelievable skill.",
        "The election results are coming in tonight.",
        "New movie trailer just dropped, looks amazing!",
        "Big game tonight between the Lakers and the Celtics.",
        "The prime minister is giving a speech on the new policy.",
        "Red carpet fashion at the Oscars was stunning."
    ]
    labels = ["Sports", "Politics", "Entertainment", "Sports", "Politics", "Entertainment"]

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'\@\w+|\#','', text)
    text = re.sub(r'[^a-z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

preprocessed_texts = [preprocess_text(text) for text in texts]

X_train, X_test, y_train, y_test = train_test_split(
    preprocessed_texts, labels, test_size=0.2, random_state=42, stratify=labels
)

model = make_pipeline(TfidfVectorizer(stop_words='english'), MultinomialNB())

model.fit(X_train, y_train)

def classify_text(text):
    cleaned_text = preprocess_text(text)
    prediction = model.predict([cleaned_text])
    return prediction[0]

if __name__ == "__main__":
    print("Model trained on the BBC News dataset.")
    print("-" * 30)

    new_text_1 = "The latest Marvel movie is breaking box office records!"
    new_text_2 = "The senator debated the new healthcare law on the senate floor."
    new_text_3 = "What a fantastic dunk by LeBron James in the final quarter!"
    new_text_4 = "The peace treaty was signed by world leaders this morning."

    print(f"Text: '{new_text_1}'")
    print(f"Predicted Category: {classify_text(new_text_1)}\n")

    print(f"Text: '{new_text_2}'")
    print(f"Predicted Category: {classify_text(new_text_2)}\n")

    print(f"Text: '{new_text_3}'")
    print(f"Predicted Category: {classify_text(new_text_3)}\n")

    print(f"Text: '{new_text_4}'")
    print(f"Predicted Category: {classify_text(new_text_4)}\n")