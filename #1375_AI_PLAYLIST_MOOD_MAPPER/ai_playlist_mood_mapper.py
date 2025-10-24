import re, warnings
from textblob import TextBlob
from difflib import get_close_matches

# --- Optional: try using transformer-based embeddings for smarter mood detection ---
try:
    from sentence_transformers import SentenceTransformer, util
    model = SentenceTransformer("all-MiniLM-L6-v2")
except Exception:
    model = None
    warnings.warn("sentence-transformers not installed — skipping semantic analysis.")

# --- Base keywords for each mood category ---
MOOD_KEYWORDS = {
    "happy": ["joy", "love", "smile", "dance", "sun", "shine", "vibes", "bright"],
    "sad": ["tears", "alone", "broken", "dark", "lost", "cry", "pain", "empty"],
    "chill": ["vibe", "calm", "night", "breeze", "smooth", "ocean", "relax", "wave"]
}

def clean(text: str) -> str:
    """Lowercase + remove punctuation."""
    return re.sub(r"[^a-z\s]", "", text.lower().strip())

def keyword_score(title: str) -> dict:
    """Score moods by keyword presence and fuzzy matches."""
    words = clean(title).split()
    scores = {m: 0 for m in MOOD_KEYWORDS}
    for word in words:
        for mood, keys in MOOD_KEYWORDS.items():
            if word in keys or get_close_matches(word, keys, cutoff=0.85):
                scores[mood] += 1
    return scores

def sentiment_mood(title: str) -> tuple[str, float]:
    """Use sentiment polarity to guess mood."""
    p = TextBlob(title).sentiment.polarity
    if p > 0.25: return ("happy", p)
    if p < -0.25: return ("sad", abs(p))
    return ("chill", 1 - abs(p))

def semantic_mood(title: str) -> tuple[str, float]:
    """Use transformer model for semantic similarity (optional)."""
    if not model: return (None, 0)
    emb_t = model.encode(title, convert_to_tensor=True)
    sims = {
        m: util.cos_sim(emb_t, model.encode(" ".join(k), convert_to_tensor=True)).item()
        for m, k in MOOD_KEYWORDS.items()
    }
    mood = max(sims, key=sims.get)
    return (mood, round(sims[mood], 2))

def detect_mood(title: str) -> dict:
    """Fuse keyword, sentiment & semantic results into one confident mood."""
    title = title.strip().title()
    kw = keyword_score(title)
    sent_mood, _ = sentiment_mood(title)
    sem_mood, _ = semantic_mood(title)

    # Weighted decision (semantic > sentiment > keywords)
    def weight(m): 
        return (kw[m] + (1 if sent_mood == m else 0) + (2 if sem_mood == m else 0)) * 0.5

    scores = {m: weight(m) for m in MOOD_KEYWORDS}
    best = max(scores, key=scores.get)
    total = sum(scores.values()) or 1
    confidence = round(scores[best] / total, 2)
    if confidence < 0.4: best = "unknown"  # handle uncertain predictions

    return {"title": title, "mood": best, "confidence": confidence}

# --- Run sample tests ---
if __name__ == "__main__":
    songs = [
        "Tears in Heaven",
        "Good Vibes Only",
        "Lost at Midnight",
        "Dancing in the Sun",
        "Ocean Breeze"
    ]
    print("\n🎧 AI Playlist Mood Mapper Results\n" + "-"*40)
    for s in songs:
        r = detect_mood(s)
        print(f"{r['title']:<25} → {r['mood'].upper()} ({r['confidence']*100:.0f}%)")
