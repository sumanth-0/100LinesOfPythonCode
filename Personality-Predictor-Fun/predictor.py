"""
Personality Predictor (for Fun) – MBTI-like 4-letter type from short answers.

Usage:
  Interactive: python predictor.py
  Non-interactive: python predictor.py -a A,B,A,B,A,B,A,B

Notes:
- For entertainment only; not a psychological assessment.
- Under 100 lines, dependency-free, with simple scoring and confidence.
"""

import argparse

QUESTIONS = [
    ("At a party, do you: A) Mingle with many, B) Talk to a few?", "EI", {"A": "E", "B": "I"}),
    ("When learning, you prefer: A) Facts, B) Big ideas?", "SN", {"A": "S", "B": "N"}),
    ("Decisions lean: A) Logic, B) Values?", "TF", {"A": "T", "B": "F"}),
    ("Your schedule is: A) Planned, B) Flexible?", "JP", {"A": "J", "B": "P"}),
    ("On weekends you: A) Go out, B) Recharge alone?", "EI", {"A": "E", "B": "I"}),
    ("You notice: A) Details, B) Patterns?", "SN", {"A": "S", "B": "N"}),
    ("Feedback style: A) Candid, B) Gentle?", "TF", {"A": "T", "B": "F"}),
    ("Trip planning: A) Itinerary, B) See what happens?", "JP", {"A": "J", "B": "P"}),
]

DIM_PAIRS = {"EI": ("E", "I"), "SN": ("S", "N"), "TF": ("T", "F"), "JP": ("J", "P")}

def ask_interactive() -> list[str]:
    answers = []
    for i, (q, _dim, _map) in enumerate(QUESTIONS, 1):
        while True:
            user = input(f"Q{i}. {q} ").strip().upper()
            if user in ("A", "B"):
                answers.append(user)
                break
            print("Please answer A or B.")
    return answers

def score(answers: list[str]) -> tuple[str, dict]:
    # Tally counts per side (e.g., E vs I)
    counts = {c: 0 for c in "EISNTFJP"}
    for ans, (_q, dim, mapping) in zip(answers, QUESTIONS):
        choice = mapping.get(ans)
        if choice:
            counts[choice] += 1
    # Build four-letter type and compute confidence per dimension
    letters, info = [], {}
    for dim, (a, b) in DIM_PAIRS.items():
        ca, cb = counts[a], counts[b]
        chosen = a if ca >= cb else b
        margin = abs(ca - cb)
        confidence = ["low", "med", "high"][min(2, margin)]
        info[dim] = {"chosen": chosen, "counts": {a: ca, b: cb}, "confidence": confidence}
        letters.append(chosen)
    return "".join(letters), info

def emoji_for(type4: str) -> str:
    return {
        "INTJ": "🧠", "INTP": "🔬", "ENTJ": "📈", "ENTP": "💡",
        "INFJ": "🧭", "INFP": "🎨", "ENFJ": "🤝", "ENFP": "✨",
        "ISTJ": "📘", "ISFJ": "🛡️", "ESTJ": "🧱", "ESFJ": "🌷",
        "ISTP": "🛠️", "ISFP": "🌿", "ESTP": "⚡", "ESFP": "🎉",
    }.get(type4, "🌟")

def explain(info: dict) -> str:
    parts = []
    names = {"EI": ("Extraversion", "Introversion"), "SN": ("Sensing", "Intuition"),
             "TF": ("Thinking", "Feeling"), "JP": ("Judging", "Perceiving")}
    for dim, data in info.items():
        a, b = DIM_PAIRS[dim]
        (an, bn) = names[dim]
        ca, cb = data["counts"][a], data["counts"][b]
        parts.append(f"{a}/{b} ({an}/{bn}): {ca}-{cb} conf={data['confidence']}")
    return "; ".join(parts)

def parse_args():
    ap = argparse.ArgumentParser(description="Personality Predictor (for Fun)")
    ap.add_argument("-a", "--answers", help="comma list of A/B (len=8)")
    return ap.parse_args()

def main():
    args = parse_args()
    if args.answers:
        answers = [x.strip().upper() for x in args.answers.split(",") if x.strip()]
        if len(answers) != len(QUESTIONS) or any(a not in ("A","B") for a in answers):
            print("Provide 8 answers as A/B, e.g., -a A,B,A,B,A,B,A,B")
            return
    else:
        print("Answer A/B. Be spontaneous; it's just for fun!\n")
        answers = ask_interactive()
    t4, info = score(answers)
    print(f"Type: {t4} {emoji_for(t4)}")
    print(explain(info))
    print("Disclaimer: This is playful and not a clinical assessment.")

if __name__ == "__main__":
    main()


