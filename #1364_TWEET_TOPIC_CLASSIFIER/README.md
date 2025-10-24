Text Classifier

A Python script to classify text into Sports, Politics, or Entertainment using a Naive Bayes model trained on the BBC News dataset.

✨ Features

Live Data: Fetches the BBC News dataset directly from a public URL.

Focused Classification: Filters the dataset to train exclusively on 'sport', 'politics', and 'entertainment' categories.

ML Pipeline: Uses scikit-learn to create a text classification pipeline with TfidfVectorizer and MultinomialNB.

Simple Interface: A minimal, command-line script that trains and predicts with a single command.

⚙️ Setup and Installation

Prerequisites:

Python 3.x

pip (Python package installer)

Install required packages:
This project requires the pandas and scikit-learn libraries.

pip install pandas scikit-learn


🚀 Usage

To run the script, execute the following command in your terminal:

python text_classifier.py


The script will start by downloading the data, training the model, and then it will classify a few example sentences.

🔧 Configuration

You can easily customize the categories used for training by editing the desired_categories list at the top of the text_classifier.py file.

desired_categories: A Python list of categories to filter from the dataset.

Example: ['sport', 'politics', 'entertainment']

📸 Demo Output

Data cleaned. Using only categories: ['sport', 'politics', 'entertainment']
Model trained successfully.

--- Classifying New Texts ---
Text: "Manchester United wins the Premier League"
Predicted Category: Sport

Text: "The president announced new economic policies"
Predicted Category: Politics

Text: "New movie release is breaking box office records"
Predicted Category: Entertainment

Text: "The stock market is fluctuating wildly"
Predicted Category: Politics
