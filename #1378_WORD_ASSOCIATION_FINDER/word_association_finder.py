stopwords_en = set([
    "a", "an", "the", "and", "or", "but", "if", "while", "with", "for", "to", "from", "in", "on",
    "at", "by", "about", "as", "into", "like", "of", "off", "over", "under", "is", "are", "was",
    "were", "be", "been", "being", "that", "which", "who", "whom", "this", "these", "those", "it",
    "its", "he", "she", "his", "her", "they", "them", "their", "you", "your", "we", "us", "our",
    "not", "no", "so", "too", "very", "can", "will", "just", "do", "does", "did", "have", "has",
    "had", "because", "than", "then", "once"
])

def find_associated_words(corpus, target, window=1):
    associated = []

    # Scan through each sentence in the corpus
    for sentence in corpus:
        words = sentence.split()
        for i, word in enumerate(words):
            if word == target:
                start = max(0, i - window)
                end = min(len(words), i + window + 1)
                associated.extend(words[start:i] + words[i+1:end])

    # Filter out stopwords
    associated = [word for word in associated if word not in stopwords_en]
    return associated

def main():
    corpus = []
    print("Enter sentences (type 'END' to finish):")
    while True:
        line = input()
        if line.strip().upper() == 'END':
            break
        corpus.append(line.strip())

    target_word = input("Enter the target word: ")
    window = int(input("Enter the context window size (default 1): "))
    associated_words = find_associated_words(corpus, target_word, window)
    print("Associated words:", associated_words)

if __name__ == "__main__":
    main()