import requests

API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"

def fetch_word_data(word):
    response = requests.get(API_URL + word)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def display_word_info(word_data):
    if word_data:
        for meaning in word_data[0]['meanings']:
            print(f"Part of Speech: {meaning['partOfSpeech']}")
            for definition in meaning['definitions']:
                print(f"Definition: {definition['definition']}")
                
            if 'synonyms' in meaning:
                print(f"Synonyms: {', '.join(meaning['synonyms']) if meaning['synonyms'] else 'None'}")
                
            if 'antonyms' in meaning:
                print(f"Antonyms: {', '.join(meaning['antonyms']) if meaning['antonyms'] else 'None'}")
    else:
        print("Word not found!")

# User input
word_to_lookup = "cool"  # Example word

# Fetch and display word info
word_info = fetch_word_data(word_to_lookup)
display_word_info(word_info)
