import matplotlib.pyplot as plt

from transformers import pipeline

sentiment_analyzer = pipeline("sentiment-analysis")

def analyze_paragraphs_advanced(text):
    paragraphs = [p.strip() for p in text.split('\n') if p.strip()]
    scores = []
    for i, p in enumerate(paragraphs):
        analysis = sentiment_analyzer(p)[0]
        label = analysis.get('label', '')
        score = analysis.get('score', 0.0)
        # Map model output to polarity in range [-1, 1]
        if label.upper().startswith('POS'):
            polarity = score
        elif label.upper().startswith('NEG'):
            polarity = -score
        else:
            polarity = 0.0
        scores.append(polarity)
        print(f"Paragraph {i+1}: {label} ({score:.2f}) -> polarity {polarity:.2f}")
    return paragraphs, scores

def visualize_sentiment(paragraphs, scores):
    plt.figure(figsize=(10, 5))
    colors = ['green' if score > 0 else 'red' if score < 0 else 'gray' for score in scores]
    plt.bar(range(1, len(scores)+1), scores, color=colors)
    plt.axhline(0, color='black', linewidth=0.8)
    plt.title("Paragraph Sentiment Analysis")
    plt.xlabel("Paragraph Number")
    plt.ylabel("Sentiment Polarity (-1 Negative, +1 Positive)")
    plt.xticks(range(1, len(scores)+1))
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    sample_text = """
    I absolutely love sunny days. They make me feel so energized and happy!
    However, the rain yesterday was quite irritating and ruined my plans.
    Overall, I believe every day brings something valuable if you look for it.
    """
    paragraphs, scores = analyze_paragraphs_advanced(sample_text)
    visualize_sentiment(paragraphs, scores)
    visualize_sentiment(paragraphs, scores)
