"""
Product Review Emotion Detector (anger, joy, trust)

Usage:
  python detector.py "I loved the product but shipping was terrible!"
  python detector.py -f reviews.txt

Design:
- Tiny lexicon for anger/joy/trust with simple stemming-like variants
- Negation scope handling (flip/attenuate for next few tokens)
- Emphasis handling: exclamation marks and ALL CAPS boost weight
- Outputs per-emotion scores and dominant label

Note: This file intentionally stays <100 lines, well-commented, and dependency-free.
"""

import sys, re, math, argparse

# Minimal lexicon; extend as needed while keeping file concise.
LEXICON = {
    "anger": {
        "angry","rage","furious","annoy","irritat","hate","terrible","awful","worst","mad",
        "disgust","frustrat","hate","outrag","livid","furor"
    },
    "joy": {
        "joy","delight","love","happy","wonderful","amazing","great","fantastic","pleas","satisfi",
        "awesome","perfect","thrill","cheer","ecstat","glad"
    },
    "trust": {
        "trust","reliab","depend","consistent","authent","honest","solid","secure","sturdy","confid",
        "assur","faith","credib","durab","backed"
    },
}

NEGATORS = {"not","n't","never","no","hardly","scarcely","barely"}

def normalize_token(token: str) -> str:
    t = re.sub(r"[^a-zA-Z]", "", token).lower()
    # crude stemming: drop common suffixes to match lexicon roots
    for suf in ("ing","ed","ly","es","s"):
        if t.endswith(suf) and len(t) > len(suf)+2:
            t = t[: -len(suf)]
            break
    return t

def emphasis_weight(token: str, exclam_count: int) -> float:
    w = 1.0
    if token.isupper() and len(token) > 1:
        w += 0.25  # ALL CAPS boost
    if exclam_count:
        w += min(0.5, 0.15 * exclam_count)  # exclamation boost
    if re.search(r"(.)\1{2,}$", token):
        w += 0.2  # loooong words
    return w

def score_text(text: str) -> dict:
    # Count exclamations to approximate emphasis for the sentence
    exclam_count = text.count("!")
    raw_tokens = re.findall(r"\b\w+\b|!+", text)
    scores = {k: 0.0 for k in LEXICON}
    negate_window = 0
    for raw in raw_tokens:
        if raw.startswith("!"):
            exclam_count += len(raw)
            continue
        tok_norm = normalize_token(raw)
        if not tok_norm:
            continue
        # manage negation scope (~3 tokens after a negator)
        if tok_norm in NEGATORS:
            negate_window = 3
            continue
        weight = emphasis_weight(raw, exclam_count)
        for emo, words in LEXICON.items():
            matched = any(tok_norm.startswith(w) for w in words)
            if not matched:
                continue
            val = 1.0 * weight
            if negate_window:
                val *= -0.7  # invert and attenuate when negated
            scores[emo] += val
        if negate_window:
            negate_window -= 1
    # small smoothing and clamp tiny noise
    for k in scores:
        if abs(scores[k]) < 0.05:
            scores[k] = 0.0
    return scores

def label_from_scores(scores: dict) -> str:
    # If all near zero, return neutral
    if all(v == 0 for v in scores.values()):
        return "neutral"
    # Choose highest signed magnitude; tie-breaker by magnitude then name
    emo = max(scores.items(), key=lambda kv: (abs(kv[1]), kv[1], kv[0]))[0]
    direction = scores[emo]
    return emo if direction > 0 else f"not_{emo}"

def main():
    ap = argparse.ArgumentParser(description="Detect anger, joy, trust in review text")
    ap.add_argument("text", nargs="?", help="review text to analyze")
    ap.add_argument("-f", "--file", help="path to a text file of reviews (one per line)")
    args = ap.parse_args()
    inputs = []
    if args.file:
        with open(args.file, "r", encoding="utf-8", errors="ignore") as fh:
            inputs.extend([line.strip() for line in fh if line.strip()])
    if args.text:
        inputs.append(args.text)
    if not inputs:
        print("Provide text or -f file.")
        return
    for line in inputs:
        sc = score_text(line)
        lab = label_from_scores(sc)
        print(f"{lab}\tanger={sc['anger']:.2f}\tjoy={sc['joy']:.2f}\ttrust={sc['trust']:.2f}\t| {line}")

if __name__ == "__main__":
    main()


