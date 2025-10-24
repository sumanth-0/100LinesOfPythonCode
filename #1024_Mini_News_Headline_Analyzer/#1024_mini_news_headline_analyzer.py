import os
import requests
API_KEY = os.getenv("NEWS_API_KEY")
if not API_KEY:
    raise ValueError("Please set the NEWS_API_KEY environment variable")
  # https://newsapi.org
URL = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"

def fetch_headlines():
    response = requests.get(URL)
    data = response.json()
    headlines = [article["title"] for article in data["articles"] if article["title"]]
    return headlines

headlines = fetch_headlines()

def load_words_from_file(filename):
    words = set()
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith(';'):
                continue 
            #to skip comments, metadata and blank lines
            words.add(line.lower())
    return words

pos_words = load_words_from_file("positive-words.txt")
neg_words = load_words_from_file("negative-words.txt")
#using positive and negative word datasets to crosscheck against

def calculate_words(y, pos_words, neg_words):
    num_pos_words = 0
    num_neg_words = 0
    y = y.lower()
    for x in y.split():
        if x in pos_words:
            num_pos_words += 1
        if x in neg_words:
            num_neg_words += 1

    return {
        'num_pos_words': num_pos_words,
        'num_neg_words': num_neg_words
    }

for headline in headlines:
    result = calculate_words(headline.lower(), pos_words, neg_words)
    print(f"'{headline}' → {result}")
#printing headlines with their number of positive and negative words