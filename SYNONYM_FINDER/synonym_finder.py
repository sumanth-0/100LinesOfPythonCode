"""
synonym_finder.py
Get synonyms for a word using Free Dictionary API.
Usage:
    python synonym_finder.py
Enter words interactively, get up to 3 synonyms each. Type 'exit' to quit.
"""

import sys
import requests

DICT_URL = "https://api.dictionaryapi.dev/api/v2/entries/en"

def get_synonyms(word: str, max_results: int = 3) -> list[str]:
    """Return a list of synonyms for `word` using Free Dictionary API."""
    try:
        resp = requests.get(f"{DICT_URL}/{word}", timeout=5)
        if resp.status_code == 404:
            return []  # Word not found
        resp.raise_for_status()
    except requests.RequestException as e:
        raise RuntimeError(f"Network/API error: {e}") from e

    try:
        data = resp.json()
    except ValueError:
        raise RuntimeError("Failed to parse JSON response from API")

    synonyms = set()
    for entry in data:
        for meaning in entry.get("meanings", []):
            for definition in meaning.get("definitions", []):
                for syn in definition.get("synonyms", []):
                    synonyms.add(syn)
            for syn in meaning.get("synonyms", []):
                synonyms.add(syn)
    return list(synonyms)[:max_results]

def main():
    while True:
        try:
            word = input("Enter a word (or 'exit' to quit): ").strip()
        except EOFError:
            break
        if word.lower() == 'exit' or not word:
            break
        try:
            synonyms = get_synonyms(word)
        except RuntimeError as e:
            print(f"Error: {e}", file=sys.stderr)
            continue
        if not synonyms:
            print(f"No synonyms found for '{word}'.")
            continue
        print(f"Synonyms for '{word}':")
        for i, s in enumerate(synonyms, start=1):
            print(f"{i}. {s}")

if __name__ == "__main__":
    main()
