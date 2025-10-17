#!/usr/bin/env python3
"""
Simple CLI trivia quiz using OpenTDB (https://opentdb.com).
Keep it small, open-source friendly, and easy to extend.
"""
import argparse, json, random, sys
from html import unescape
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError

API = "https://opentdb.com/api.php"

def fetch_questions(amount=10, difficulty=None, qtype=None):
    params = f"?amount={amount}"
    if difficulty: params += f"&difficulty={difficulty}"
    if qtype: params += f"&type={qtype}"
    req = Request(API + params, headers={"User-Agent": "trivia-cli/1.0"})
    try:
        with urlopen(req, timeout=10) as r:
            data = json.load(r)
    except (URLError, HTTPError) as e:
        print("Network error:", e)
        return []
    if data.get("response_code") != 0:
        print("API returned no results (response_code {})".format(data.get("response_code")))
        return []
    return data.get("results", [])

def ask_question(q, idx, total):
    question = unescape(q["question"])
    correct = unescape(q["correct_answer"])
    wrong = [unescape(x) for x in q["incorrect_answers"]]
    choices = wrong + [correct]
    random.shuffle(choices)
    print(f"\nQuestion {idx}/{total} — ({q.get('category','')}, {q.get('difficulty','')})")
    print(question)
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    mapping = {}
    for i, choice in enumerate(choices):
        letter = letters[i]
        mapping[letter] = choice
        print(f"  {letter}. {choice}")
    # accept answer
    while True:
        ans = input("Your answer (letter): (or q to quit) ").strip().upper()
        if ans=="q":
            print("Goodbye!")
            sys.exit(0)
        if not ans:
            print("Type a letter (or Ctrl-C to quit).")
            continue
        if ans in mapping:
            picked = mapping[ans]
            is_correct = picked == correct
            if is_correct:
                print("✅ Correct!")
            else:
                print(f"❌ Wrong — correct answer: {correct}")
            return is_correct
        else:
            print("Invalid letter. Try again.")

def main():
    ap = argparse.ArgumentParser(description="Minimal trivia CLI (OpenTDB).")
    ap.add_argument("-n","--num", type=int, default=10, help="Number of questions (1-50).")
    ap.add_argument("-d","--difficulty", choices=["easy","medium","hard"], help="Difficulty.")
    ap.add_argument("-t","--type", choices=["multiple","boolean"], help="Question type.")
    args = ap.parse_args()
    num = max(1, min(50, args.num))
    print(f"Fetching {num} question(s)...")
    qs = fetch_questions(amount=num, difficulty=args.difficulty, qtype=args.type)
    if not qs:
        print("No questions available. Try different options or check your network.")
        sys.exit(1)
    score = 0
    total = len(qs)
    try:
        for i, q in enumerate(qs, start=1):
            if ask_question(q, i, total):
                score += 1
    except KeyboardInterrupt:
        print("\nInterrupted by user. Showing score so far...")
    print(f"\nFinal score: {score}/{total} ({score/total*100:.1f}%)")
    if score == total:
        print("Legendary! ❤️‍🔥 Consider adding a high-score feature to the repo.")
    elif score >= total*0.7:
        print("Nice — above average.")
    else:
        print("Tough luck. Read more trivia docs and try again.")

if __name__ == "__main__":
    main()
