import requests

def get_meaning(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()[0]
        meaning = data['meanings'][0]
        part_of_speech = meaning['partOfSpeech']
        definition = meaning['definitions'][0]['definition']
        example = meaning['definitions'][0].get('example', 'No example available.')
        
        print(f"\nWord: {word}")
        print(f"Part of Speech: {part_of_speech}")
        print(f"Meaning: {definition}")
        print(f"Example: {example}")
    else:
        print("Word not found!")

word = input("Enter a word: ").strip()
get_meaning(word)
