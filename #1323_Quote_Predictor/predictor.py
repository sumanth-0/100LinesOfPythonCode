import re

# --- Rule Database ---
# Define unique keywords, phrases, or stylistic elements associated with a celebrity.
# The keys are the celebrity names, and the values are lists of signature phrases/words
# or regex patterns that strongly indicate they are the speaker.
PREDICTION_RULES = {
    "Yoda": [
        r"hmmm", "always in motion", r"\bdo or do not\b", "much to learn", 
        "powerful you have become", "judge me by my size"
    ],
    "Oprah Winfrey": [
        "best life", "aha moment", "live your truth", "what I know for sure",
        "stand in your power"
    ],
    "Dwayne 'The Rock' Johnson": [
        "Jabroni", "candy", "smell what The Rock is cooking", "layeth the smack down",
        "finally"
    ],
    "Taylor Swift": [
        "long list of ex-lovers", "shake it off", "dear John", "karma is", 
        "lover", "haters gonna hate"
    ]
}

# --- Core Prediction Function ---

def predict_celebrity(quote: str) -> str:
    """
    Analyzes a quote against defined rules to predict the celebrity speaker.
    
    Args:
        quote: The text quote to analyze.
    
    Returns:
        The name of the predicted celebrity, or "Unknown Speaker".
    """
    # Normalize the quote for case-insensitive matching
    normalized_quote = quote.lower()
    
    # Track which celebrity gets the most rule hits
    hit_counts = {}

    for celebrity, rules in PREDICTION_RULES.items():
        count = 0
        for rule in rules:
            # Use regular expression search to find the rule pattern in the quote
            if re.search(rule, normalized_quote):
                count += 1
        
        if count > 0:
            hit_counts[celebrity] = count

    # Find the celebrity with the highest hit count
    if hit_counts:
        # max() uses the hit_counts dictionary values (count) to find the key (celebrity)
        # default="" prevents error if hit_counts is empty, although protected by the outer if
        predicted_speaker = max(hit_counts, key=hit_counts.get)
        
        # We only predict if they have at least one hit
        return predicted_speaker

    return "Unknown Speaker"

# --- Execution Examples ---

if __name__ == "__main__":
    
    TEST_QUOTES = [
        "A long time ago, in a galaxy far, far away. Do or do not, there is no try.",
        "You get a car! You get a car! This is your year to live your best life.",
        "The people's champion has finally come back to WrestleMania! Layeth the smack down!",
        "The haters gonna hate, hate, hate, hate, hate. Just shake it off.",
        "This is just a regular sentence with no keywords.",
    ]
    
    print("\n--- Celebrity Quote Predictor (Rule-Based) ---\n")
    
    for i, quote in enumerate(TEST_QUOTES):
        prediction = predict_celebrity(quote)
        
        # Truncate the quote for clean printing
        short_quote = f"'{quote[:50].strip()}...'" if len(quote) > 50 else f"'{quote.strip()}'"
        
        print(f"Quote {i+1}: {short_quote}")
        print(f"Prediction: {prediction}\n")

    print("----------------------------------------------")