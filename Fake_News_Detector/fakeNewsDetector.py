# Import necessary libraries
import numpy as np
import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import nltk

# Download stopwords if not already present
nltk.download('stopwords')

# Load dataset
news_dataset = pd.read_csv('Fake_News_Detector/train.csv')

# Fill missing values
news_dataset = news_dataset.fillna('')

# Combine 'author' and 'title' columns into 'content'
news_dataset['content'] = news_dataset['author'] + ' ' + news_dataset['title']

# Separate data and labels
X = news_dataset['content']
Y = news_dataset['label']

# Initialize PorterStemmer for stemming
port_stem = PorterStemmer()

# Function to clean and stem text
def preprocess_text(text):
    # Remove non-alphabetic characters, convert to lowercase, and split
    stemmed_content = re.sub('[^a-zA-Z]', ' ', text).lower().split()
    # Stem words and remove stopwords
    stemmed_content = [port_stem.stem(word) for word in stemmed_content if word not in stopwords.words('english')]
    return ' '.join(stemmed_content)

# Apply preprocessing to content
X = X.apply(preprocess_text)

# Convert textual data to numerical data using TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

# Use Logistic Regression as the model
model = LogisticRegression()
model.fit(X_train, Y_train)

# Evaluate the model on training data
train_accuracy = accuracy_score(model.predict(X_train), Y_train)
print(f'Training Accuracy: {train_accuracy:.2f}')

# Evaluate the model on test data
test_accuracy = accuracy_score(model.predict(X_test), Y_test)
print(f'Test Accuracy: {test_accuracy:.2f}')

# Predict a sample from test data
sample_test = X_test[4]
prediction = model.predict(sample_test)

# Output prediction result
if prediction[0] == 0:
    print('The news is Real')
else:
    print('The news is Fake')

# Print the actual label for comparison
print(f'Actual label: {Y_test.iloc[4]}')
