import re
from collections import Counter

# Hardcoded common stop words
STOP_WORDS = {
    'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'you', 'your', 'yours',
    'he', 'him', 'his', 'she', 'her', 'hers', 'it', 'its', 'they', 'them',
    'their', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those',
    'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has',
    'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and',
    'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by',
    'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during',
    'before', 'after', 'above', 'below', 'up', 'down', 'in', 'on', 'off', 'over',
    'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where',
    'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other',
    'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than',
    'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now'
}

def extract_keywords(caption, max_keywords=5):
    # Clean and tokenize
    caption = caption.lower()
    words = re.findall(r'\b[a-zA-Z]{3,}\b', caption)
    # Remove stop words and count
    filtered_words = [word for word in words if word not in STOP_WORDS]
    word_counts = Counter(filtered_words)
    # Get top keywords
    top_keywords = [word for word, _ in word_counts.most_common(max_keywords)]
    return top_keywords

def suggest_hashtags(caption):
    keywords = extract_keywords(caption)
    hashtags = ['#' + word for word in keywords]
    return hashtags

# Main script
if __name__ == "__main__":
    caption = input("Enter social media caption: ").strip()
    if caption:
        hashtags = suggest_hashtags(caption)
        print("Suggested hashtags:", ' '.join(hashtags))
    else:
        print("No caption provided.")
