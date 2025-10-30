import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import re

DEFAULT_PARAGRAPH = """
Natural language processing (NLP) is a subfield of computer science, information 
engineering, and artificial intelligence concerned with the interactions between 
computers and human (natural) languages. As such, NLP is focused on how to 
program computers to process and analyze large amounts of natural language data. 
A key component of this processing is text summarization. Extractive summarization 
techniques rely on selecting key sentences or phrases from the source document 
and combining them to form the summary. This method is generally rule-based and 
is straightforward to implement using frequency counts. Abstractive summarization 
is more complex and involves generating new phrases that capture the core meaning. 
NLP systems are becoming increasingly important in modern data science.
"""

SUMMARY_SIZE = 3 

def summarize_text(text: str, num_sentences: int = SUMMARY_SIZE) -> str:
    sentences = sent_tokenize(text)
    if num_sentences >= len(sentences):
        return text 
    stop_words = set(stopwords.words('english'))
    word_frequencies = {}
    for word in word_tokenize(text):
        word = re.sub(r'[^\w]', '', word).lower()
        if word not in stop_words and len(word) > 1:
            if word not in word_frequencies:
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1
    if not word_frequencies:
        return "Error: Text contained only stop words or was empty."
    max_frequency = max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word] = (word_frequencies[word] / max_frequency)
    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            word = re.sub(r'[^\w]', '', word)
            if word in word_frequencies:
                if sentence not in sentence_scores:
                    sentence_scores[sentence] = word_frequencies[word]
                else:
                    sentence_scores[sentence] += word_frequencies[word]
    ranked_sentences = sorted(sentence_scores.items(), key=lambda item: item[1], reverse=True)
    top_sentences = [sent for sent, score in ranked_sentences[:num_sentences]]
    final_summary = " ".join(
        [sentence for sentence in sentences if sentence in top_sentences]
    )
    return final_summary

if __name__ == "__main__":
    print("\n--- Extractive Text Summarizer ---\n")
    user_input = input("Paste the paragraph you want to summarize here (or press Enter to use the default example):\n")
    if user_input.strip():
        input_text = user_input
        print("\nUsing provided text.")
    else:
        input_text = DEFAULT_PARAGRAPH
        print("\nUsing default example paragraph.")
    summary = summarize_text(input_text, num_sentences=SUMMARY_SIZE)
    input_word_count = len(input_text.split())
    print(f"\nOriginal Paragraph (Length: {input_word_count} words):\n{input_text}\n")
    print(f"\n--- Extracted Summary ({SUMMARY_SIZE} sentences) ---\n")
    print(summary)
    print("\n----------------------------------\n")
