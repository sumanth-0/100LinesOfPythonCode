import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)

def generate_hashtags(text, num_hashtags=5):
    
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text.lower())
    words = word_tokenize(cleaned_text)
    
    stop_words = set(stopwords.words('english'))
    # Removed some common but less descriptive words
    mandatory_remove = stop_words.union({'what', 'this', 'that', 'with', 'from', 'for', 'you'})

    filtered_words = [
        w for w in words if w not in mandatory_remove and len(w) > 2
    ]
    
    tagged_words = nltk.pos_tag(filtered_words)
    
    # Primary tags: Nouns and Adjectives
    primary_tags = {'NN', 'NNS', 'NNP', 'NNPS', 'JJ', 'JJR', 'JJS'}
    relevant_words = [
        word for word, tag in tagged_words if tag in primary_tags
    ]

    # Fallback: If not enough primary words, include Verbs and Adverbs
    if len(set(relevant_words)) < num_hashtags:
        secondary_tags = {'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'RB', 'RBR', 'RBS'}
        
        existing_words = set(relevant_words)
        for word, tag in tagged_words:
            if tag in secondary_tags and word not in existing_words:
                relevant_words.append(word)
                existing_words.add(word)

    word_counts = Counter(relevant_words)
    # Always selects the top 5 words
    top_words = [word for word, count in word_counts.most_common(num_hashtags)]
    
    hashtags = [f"#{word}" for word in top_words]
    
    return hashtags

if __name__ == "__main__":
    
    while True:
        user_input = input("Enter your text (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        
        # Always call with num_hashtags=5 (default)
        user_hashtags = generate_hashtags(user_input, num_hashtags=5)
        
        print(f"\nGenerated Hashtags (Top 5): {', '.join(user_hashtags)}\n")