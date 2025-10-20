import re
import requests
import time

def fetch_sentence_from_wikipedia():
    URL = "https://en.wikipedia.org/w/api.php"
    PARAMS = {
        "action": "query",
        "format": "json",
        "generator": "random",
        "grnnamespace": 0,
        "prop": "extracts",
        "exintro": True,
        "explaintext": True
    }
    HEADERS = {"User-Agent": "TypingGame/1.0 (https://github.com/alexdimmock95)"}

    try:
        response = requests.get(URL, params=PARAMS, headers=HEADERS)
        data = response.json()
        page = next(iter(data["query"]["pages"].values()))
        text = page["extract"]

        # Split text into sentences (simple regex)
        sentences = re.split(r'(?<=[.!?]) +', text)
        if sentences:
            return sentences[0]
        else:
            return "Wikipedia returned an empty page."
    except Exception as e:
        return f"Error fetching Wikipedia sentence: {e}"

def wpm_accuracy(user_input, original_sentence, time_taken):
    words_typed = user_input.split()
    original_words = original_sentence.split()
    correct_words = sum(1 for u, o in zip(words_typed, original_words) if u == o)
    total_words = len(original_words)
    wpm = (len(words_typed) / time_taken) * 60
    accuracy = (correct_words / total_words) * 100
    return wpm, accuracy

def game():
    while True:
        sentence = fetch_sentence_from_wikipedia()
        input(f"Press Enter when you're ready to type the sentence:\n{sentence}")
        start_time = time.perf_counter()
        user_input = input("")
        end_time = time.perf_counter()
        time_taken = end_time - start_time
        wpm, accuracy = wpm_accuracy(user_input, sentence, time_taken)
        print(f"Results:\nWords Per Minute (WPM): {wpm:.2f}\nAccuracy (% of words typed correctly): {accuracy:.2f}%")
        again = input("Type 'n' for a new sentence or any other key to exit: ").lower()
        if again !='n':
            print("Thank you for playing!")

if __name__ == "__main__":
    game()