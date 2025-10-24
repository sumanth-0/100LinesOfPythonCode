import re

def analyze_tone(email_text):
    email = email_text.lower().strip()

    # Define keyword sets
    friendly_words = {"hi", "hello", "thanks", "thank you", "cheers", "have a great day", "hope you're well"}
    rude_words = {"stupid", "idiot", "nonsense", "terrible", "useless", "hate", "worst"}
    formal_phrases = {"dear", "sincerely", "regards", "best wishes", "to whom it may concern", "please find attached"}

    # Basic counts
    friendly_score = sum(word in email for word in friendly_words)
    rude_score = sum(word in email for word in rude_words)
    formal_score = sum(word in email for word in formal_phrases)

    # Check punctuation and tone indicators
    if re.search(r'!', email):
        friendly_score += 1
    if re.search(r'\bplease\b', email):
        formal_score += 1
    if re.search(r'\bnow\b|\bimmediately\b', email):
        rude_score += 1

    # Grammar cues
    if "dear" in email and "regards" in email:
        formal_score += 2
    if "sorry" in email or "appreciate" in email:
        friendly_score += 1

    # Decide tone
    scores = {"Friendly": friendly_score, "Rude": rude_score, "Formal": formal_score}
    dominant = max(scores, key=scores.get)

    # Handle ties
    if len([v for v in scores.values() if v == scores[dominant]]) > 1:
        dominant = "Mixed"

    print(f"\nEmail tone analysis:")
    print("-" * 25)
    print(f"Friendly score: {friendly_score}")
    print(f"Rude score: {rude_score}")
    print(f"Formal score: {formal_score}")
    print(f"\n➡️ The email sounds: {dominant}")

# Example usage
if __name__ == "__main__":
    sample_email = """Dear John,
I hope you're well! Please find attached the document.
Best regards,
Alice"""
    analyze_tone(sample_email)
