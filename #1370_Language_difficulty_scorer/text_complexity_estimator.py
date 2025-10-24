import re

class TextComplexityEstimator:
    def __init__(self, text):
        self.text = text
        self.sentences = self._split_sentences()
        self.words = self._split_words()

    def _split_sentences(self):
        return re.split(r'[.!?]+', self.text.strip())

    def _split_words(self):
        return re.findall(r'\b\w+\b', self.text.lower())

    def avg_sentence_length(self):
        sentences = [s for s in self.sentences if s.strip()]
        if not sentences:
            return 0
        return len(self.words) / len(sentences)

    def vocab_richness(self):
        unique_words = set(self.words)
        return len(unique_words) / len(self.words) if self.words else 0

    def calculate_complexity_score(self):
        length_score = self.avg_sentence_length() / 20
        vocab_score = (1 - self.vocab_richness()) * 2
        return min(10, round((length_score + vocab_score) * 5, 2))

    def complexity_level(self, score):
        if score < 3.5:
            return "🟢 Simple"
        elif score < 7:
            return "🟡 Moderate"
        else:
            return "🔴 Complex"

    def analyze(self):
        score = self.calculate_complexity_score()
        print("\n📖 TEXT COMPLEXITY ANALYSIS 📖")
        print("-" * 40)
        print(f"Total Sentences: {len(self.sentences)}")
        print(f"Total Words: {len(self.words)}")
        print(f"Average Sentence Length: {self.avg_sentence_length():.2f} words")
        print(f"Vocabulary Richness: {self.vocab_richness():.2f}")
        print(f"Complexity Score (0-10): {score}")
        print(f"Complexity Level: {self.complexity_level(score)}")
        print("-" * 40)

if __name__ == "__main__":
    print("🧠 Text Complexity Estimator 🧠")
    text = input("\nEnter your text:\n> ")
    estimator = TextComplexityEstimator(text)
    estimator.analyze()
