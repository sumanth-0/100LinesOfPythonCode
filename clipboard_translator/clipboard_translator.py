import pyperclip
import requests

def translate_text(text, target_lang='hi'):
    url = "https://translate.googleapis.com/translate_a/single"
    params = {
        "client": "gtx",
        "sl": "en",        # source language: English
        "tl": target_lang, # target language: Hindi ('hi')
        "dt": "t",
        "q": text
    }
    resp = requests.get(url, params=params)
    if resp.status_code != 200:
        print("Translation failed")
        return text
    try:
        translation = resp.json()[0][0][0]
        return translation
    except Exception:
        print("Could not parse translation response")
        return text

def main():
    print("Clipboard Translator: EN → HI")
    input("Copy any English text, then press Enter...")
    text = pyperclip.paste().strip()
    if not text:
        print("Clipboard is empty!")
        return
    print("Original:", text)
    translated = translate_text(text, 'hi')
    if translated:
        pyperclip.copy(translated)
        print("Translated (HI):", translated)
        print("Translation copied to clipboard.")

if __name__ == "__main__":
    main()
