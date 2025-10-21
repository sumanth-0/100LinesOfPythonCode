import numpy as np

langs = { 0: "English",  1: "French",  2: "German",  3: "Spanish",  4: "Italian",  5: "Portuguese",  6: "Dutch", 7: "Swedish",  8: "Turkish",  9: "Polish" }

LETTER_FREQUENCIES = {
    "English": { 'a': 8.2, 'b': 1.5, 'c': 2.8, 'd': 4.3, 'e': 13.0, 'f': 2.2, 'g': 2.0, 'h': 6.1,
                 'i': 7.0, 'j': 0.15, 'k': 0.8, 'l': 4.0, 'm': 2.4, 'n': 6.7, 'o': 7.5, 'p': 1.9,
                 'q': 0.1, 'r': 6.0, 's': 6.3, 't': 9.1, 'u': 2.8, 'v': 1.0, 'w': 2.4, 'x': 0.15,
                 'y': 2.0, 'z': 0.07 },

    "French": { 'a': 7.6, 'b': 0.9, 'c': 3.3, 'd': 3.7, 'e': 15.0, 'f': 1.1, 'g': 1.0, 'h': 0.7,
                'i': 7.5, 'j': 0.6, 'k': 0.0, 'l': 5.4, 'm': 2.7, 'n': 7.1, 'o': 5.8, 'p': 3.0,
                'q': 0.9, 'r': 6.5, 's': 7.9, 't': 7.2, 'u': 6.4, 'v': 1.8, 'w': 0.0, 'x': 0.4,
                'y': 0.3, 'z': 0.1 },

    "German": { 'a': 6.5, 'b': 1.9, 'c': 3.1, 'd': 5.1, 'e': 17.4, 'f': 1.7, 'g': 3.0, 'h': 4.6,
                'i': 7.6, 'j': 0.3, 'k': 1.3, 'l': 3.4, 'm': 2.5, 'n': 9.8, 'o': 2.5, 'p': 0.7,
                'q': 0.02, 'r': 7.0, 's': 7.3, 't': 6.2, 'u': 4.2, 'v': 0.8, 'w': 1.9, 'x': 0.03,
                'y': 0.04, 'z': 1.1 },

    "Spanish": { 'a': 11.5, 'b': 2.2, 'c': 4.0, 'd': 5.0, 'e': 13.7, 'f': 0.9, 'g': 1.0, 'h': 0.7,
                 'i': 6.2, 'j': 0.5, 'k': 0.0, 'l': 5.0, 'm': 3.2, 'n': 6.7, 'o': 8.7, 'p': 2.5,
                 'q': 1.0, 'r': 6.9, 's': 7.9, 't': 4.6, 'u': 4.6, 'v': 1.0, 'w': 0.0, 'x': 0.2,
                 'y': 1.0, 'z': 0.5 },

    "Italian": { 'a': 11.7, 'b': 0.9, 'c': 4.5, 'd': 3.7, 'e': 11.8, 'f': 1.1, 'g': 1.6, 'h': 0.6,
                 'i': 10.8, 'j': 0.0, 'k': 0.0, 'l': 6.5, 'm': 2.5, 'n': 6.8, 'o': 9.8, 'p': 3.0,
                 'q': 0.5,  'r': 6.4, 's': 4.9, 't': 5.6, 'u': 3.0, 'v': 2.1, 'w': 0.0, 'x': 0.0, 
                 'y': 0.0, 'z': 1.0},

    "Portuguese": {'a': 14.6, 'b': 1.0, 'c': 3.9, 'd': 4.9, 'e': 12.6, 'f': 1.0, 'g': 1.3, 'h': 1.2,
                    'i': 6.2, 'j': 0.4, 'k': 0.0, 'l': 2.8, 'm': 4.7, 'n': 5.0, 'o': 10.7, 'p': 2.5,
                    'q': 1.2, 'r': 6.7, 's': 6.1, 't': 4.3, 'u': 3.6, 'v': 1.8, 'w': 0.0, 'x': 0.2,
                    'y': 0.0, 'z': 0.4},
    
    "Dutch": {'a': 7.5, 'b': 1.6, 'c': 1.2, 'd': 6.2, 'e': 18.9, 'f': 0.8, 'g': 3.4, 'h': 2.4,
              'i': 6.5, 'j': 1.5, 'k': 2.3, 'l': 3.6, 'm': 2.2, 'n': 10.0, 'o': 6.1, 'p': 1.6,
              'q': 0.01, 'r': 6.4, 's': 3.7, 't': 6.8, 'u': 1.9, 'v': 2.5, 'w': 1.5, 'x': 0.04,
              'y': 0.04, 'z': 1.4},

    "Swedish": {'a': 9.38, 'b': 1.53, 'c': 1.45, 'd': 4.70, 'e': 10.15, 'f': 2.03, 'g': 2.86, 'h': 2.09,
                'i': 5.82, 'j': 0.61, 'k': 3.14, 'l': 5.28, 'm': 3.47, 'n': 8.54, 'o': 4.48, 'p': 1.84,
                'q': 0.02, 'r': 8.43, 's': 6.59, 't': 7.69, 'u': 1.92, 'v': 2.41, 'w': 0.02, 'x': 0.14,
                'y': 0.14, 'z': 0.00},

    "Turkish": {'a': 11.92, 'b': 2.84, 'c': 0.98, 'd': 5.16, 'e': 8.91, 'f': 0.46, 'g': 1.25, 'h': 1.22,
                'i': 9.60, 'j': 0.03, 'k': 4.68, 'l': 5.92, 'm': 3.75, 'n': 7.49, 'o': 2.45, 'p': 0.98,
                'q': 0.00, 'r': 6.72, 's': 3.01, 't': 3.31, 'u': 3.14, 'v': 0.96, 'w': 0.00, 'x': 0.00,
                'y': 3.21, 'z': 1.50},

    "Polish": { 'a': 10.5, 'b': 1.5, 'c': 3.9, 'd': 3.9, 'e': 8.0, 'f': 0.3, 'g': 1.3, 'h': 1.0,
                'i': 8.2, 'j': 2.3, 'k': 3.5, 'l': 3.9, 'm': 2.8, 'n': 5.5, 'o': 7.3, 'p': 3.1,
                'q': 0.0, 'r': 4.7, 's': 4.5, 't': 3.9, 'u': 2.5, 'v': 0.0, 'w': 4.5, 'x': 0.0,
                'y': 4.0, 'z': 5.6 }

}

chars = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

counts = {}

percentage = {
    'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0,
    'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0
}

predict = {}

text = input("Enter your text: ")
text = text.lower()
text = text.replace('!', '').replace(',', '').replace('?', '').replace(' ', '').replace('/', '').replace('.', '').replace('\'', '').replace('\"', "")
for digit in '0123456789':
    text = text.replace(digit, '')
# print(text)

for char in chars:
    counts[char] = text.count(char)

length = len(text)
if length == 0:
    print("No letters detected. Please enter valid text.")
    exit()
if length < 30:
    print("Warning: Input is very short, prediction accuracy may be low.")

for char in chars:
    percentage[char] = counts[char] * 100 / length

distances = []

for lang in langs.values():
    total_diff = 0
    for char in chars:
        expected = LETTER_FREQUENCIES[lang][char]
        actual = percentage[char]
        total_diff += abs(expected - actual)
    distances.append(total_diff)

pred_lang_index = np.argmin(distances)
print("Your language is likely:", langs[pred_lang_index])

