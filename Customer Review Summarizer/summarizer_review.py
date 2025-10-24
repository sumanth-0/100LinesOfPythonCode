import nltk
import sys
import re
import heapq
from sklearn.feature_extraction.text import TfidfVectorizer

# --- NLTK Download ---
# Download necessary NLTK data for tokenization and stop words
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', quiet=True)

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords', quiet=True)

try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab', quiet=True)
# --- End NLTK Download ---

# Import NLTK modules
try:
    from nltk.tokenize import sent_tokenize
    from nltk.corpus import stopwords
except ImportError as e:
    print(f"Failed to import NLTK modules: {e}.", file=sys.stderr)
    sys.exit("NLTK modules not available.")

# Load stop words
try:
    stop_words_list = stopwords.words('english')
except Exception as e:
    print(f"NLTK stopwords.words failed: {e}. Using a basic list.", file=sys.stderr)
    # Define a basic list if NLTK fails
    stop_words_list = [
        'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 
        'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 
        'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 
        'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 
        'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 
        'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 
        'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 
        'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 
        'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 
        'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 
        'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 
        'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 
        'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 
        's', 't', 'can', 'will', 'just', 'don', 'should', 'now'
    ]

stop_words = set(stop_words_list)

# --- Sample Customer Reviews ---
reviews = [
    "This product is amazing! I really loved the quality and the customer service was excellent. Highly recommend.",
    "The product was okay, not great. It broke after a few weeks. Customer service was helpful in getting a replacement, but it was a hassle.",
    "I'm very disappointed. The item arrived late and was not as described. Quality is poor. I will be returning it.",
    "Absolutely fantastic purchase! The quality is top-notch, and it exceeded my expectations. Delivery was fast too.",
    "Decent product for the price. It does the job, but don't expect premium quality. Customer service was responsive."
]

# 1. Combine all reviews into a single text
full_text = " ".join(reviews)

# 2. Tokenize into sentences using original text
try:
    original_sentences = sent_tokenize(full_text)
except Exception as e:
    print(f"NLTK sent_tokenize failed: {e}. Falling back to basic split.", file=sys.stderr)
    # Basic split on sentence-ending punctuation as a fallback
    original_sentences = re.split(r'(?<=[.!?])\s+', full_text)

# 3. Create cleaned sentences for TF-IDF analysis
cleaned_sentences = []
for sentence in original_sentences:
    # Lowercase
    s_lower = sentence.lower()
    # Remove all punctuation and numbers
    s_clean = re.sub(r'[^a-zA-Z\s]', '', s_lower)
    # Consolidate whitespace
    s_clean = re.sub(r'\s+', ' ', s_clean).strip()
    cleaned_sentences.append(s_clean)

# 4. Function to calculate sentence scores based on TF-IDF
def get_sentence_scores(sentences_to_score, stop_words):
    """
    Scores sentences based on the sum of TF-IDF scores of their words.
    """
    if not sentences_to_score:
        return {}

    vectorizer = TfidfVectorizer(stop_words=list(stop_words))
    
    try:
        # Vectorize the *cleaned* sentences
        tfidf_matrix = vectorizer.fit_transform(sentences_to_score)
    except ValueError as e: # e.g., all sentences are stop words
        print(f"Error vectorizing sentences: {e}")
        return {}

    sentence_scores = {}
    for i in range(len(sentences_to_score)):
        # Score = sum of TF-IDF scores for words in the sentence
        score = tfidf_matrix[i].sum()
        sentence_scores[i] = score
            
    return sentence_scores

# 5. Get sentence scores
sentence_scores = get_sentence_scores(cleaned_sentences, stop_words)

# 6. Select the top N sentences for the summary
summary_sentences_count = 3 # You can change this number

if sentence_scores:
    # 7. Get indices of top sentences
    top_sentence_indices = heapq.nlargest(
        summary_sentences_count, 
        sentence_scores, 
        key=sentence_scores.get
    )
    
    # Sort indices to maintain the original order
    top_sentence_indices.sort()
    
    # 8. Build summary from *original* sentences
    summary = " ".join([original_sentences[i] for i in top_sentence_indices])
    
    print("--- Original Reviews ---")
    for r in reviews:
        print(f"- {r}")
    print("\n--- Generated Summary (Top {} sentences) ---".format(summary_sentences_count))
    print(summary)
else:
    print("Could not generate summary (no sentences or error).")