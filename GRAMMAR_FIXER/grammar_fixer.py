def fix_grammar(text: str) -> str:
    """
    Enhanced grammar fixer:
    - Capitalizes sentence starts and 'I'
    - Adds missing punctuation
    - Normalizes spaces
    - Fixes common contractions
    - Ensures proper spacing after punctuation
    """
    import re

    # Normalize spaces
    text = re.sub(r'\s+', ' ', text.strip())

    # Fix common contractions
    contractions = {
        r'\bdont\b': "don't", r'\bcant\b': "can't", r'\bwont\b': "won't",
        r'\bim\b': "I'm", r'\bive\b': "I've", r'\byoure\b': "you're",
        r'\btheyre\b': "they're", r'\bweve\b': "we've", r'\bits\b': "it's"
    }
    for pattern, replacement in contractions.items():
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)

    # Insert periods before likely sentence starters if no punctuation exists
    if not re.search(r'[.!?]', text):
        sentence_starters = ['it', 'do', 'does', 'did', 'has', 'have', 'was', 'were', 'can', 'could', 'will', 'would', 'should', 'may', 'might', 'must', 'he', 'she', 'they', 'we', 'i']
        question_starters = ['what', 'how', 'when', 'where', 'why', 'who', 'which']
        all_starters = sentence_starters + question_starters
        words = text.split()
        new_words = []
        for i, word in enumerate(words):
            if i > 0 and word.lower() in all_starters and words[i-1].lower() not in all_starters:
                new_words.append('.')
            new_words.append(word)
        text = ' '.join(new_words)



    # Split into sentences
    sentences = re.split(r'([.!?])', text)

    fixed_sentences = []
    for i in range(0, len(sentences), 2):
        sentence = sentences[i].strip()
        if not sentence:
            continue

        # Capitalize first word and lowercase others
        words = sentence.split()
        if words:
            words[0] = words[0][0].upper() + words[0][1:].lower() if len(words[0]) > 1 else words[0].upper()
            for j in range(1, len(words)):
                words[j] = words[j].lower()
            sentence = ' '.join(words)

        # Add punctuation
        words_in_sentence = [w.lower() for w in sentence.split()]
        question_words = ['do', 'does', 'did', 'can', 'could', 'will', 'would', 'should', 'may', 'might', 'must', 'have', 'has', 'am', 'were', 'was', 'what', 'how', 'when', 'where', 'why', 'who', 'which']
        is_question = any(word in question_words for word in words_in_sentence)
        if i + 1 < len(sentences):
            punct = sentences[i + 1]
            if punct == '.' and is_question:
                punct = '?'
        else:
            punct = '?' if is_question else '.'
        fixed_sentences.append(sentence + punct)

    # Join with space and ensure space after punctuation
    result = ' '.join(fixed_sentences)
    result = re.sub(r'([.!?])([A-Z])', r'\1 \2', result)

    return result


if __name__ == "__main__":
    print("=== Grammar Fixer ===")
    text = input("Enter your text:\n> ")
    fixed = fix_grammar(text)
    print("\n--- Fixed Text ---")
    print(fixed)
