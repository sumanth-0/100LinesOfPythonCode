# Text Emoji Replacer 😊

Replace keywords in text with emojis (e.g., "happy" → 😊) using a built-in emoji dictionary!

## 🎯 What This Script Does

This Python script automatically replaces text keywords with their corresponding emojis. It includes a dictionary of 65+ common words mapped to popular emojis, making your text more expressive and fun!

## ✨ Features

- **No External Dependencies**: Uses only Python's standard library (`re`, `sys`)
- **65+ Emoji Mappings**: Pre-configured dictionary with common words
- **Multi-word Support**: Handles phrases like "thumbs up" → 👍
- **Case-Insensitive**: Matches "Happy", "HAPPY", or "happy"
- **Two Processing Modes**: File conversion or direct text input
- **Optional File Output**: Save results or print to console
- **Smart Matching**: Uses word boundaries to avoid partial matches

## 🚀 Usage

### Method 1: Command Line (File Processing)
```bash
# Convert file and print to console
python text_emoji_replacer.py input.txt

# Convert and save to output file
python text_emoji_replacer.py input.txt output.txt
```

### Method 2: Interactive Mode
```bash
python text_emoji_replacer.py
```
Then choose between file conversion or direct text input.

## 💡 Examples

### Example 1: Simple Text Conversion
```bash
python text_emoji_replacer.py
# Choose option 2 (Convert text input)
# Input: "I'm so happy! Love this party!"
# Output: "I'm so 😊! ❤️ this 🎉!"
```

### Example 2: File Conversion
Create a file `message.txt`:
```
Good morning! The sun is shining today.
I love coffee and pizza.
Don't forget to give a thumbs up!
```

Run:
```bash
python text_emoji_replacer.py message.txt
```

Output:
```
Good morning! The ☀️ is shining today.
I ❤️ ☕ and 🍕.
Don't forget to give a 👍!
```

## 📋 Emoji Dictionary (65+ Mappings)

### Emotions & Expressions
- happy, smile → 😊
- laugh → 😂
- sad → 😢
- cry → 😭
- angry → 😠
- cool → 😎
- think → 🤔
- wow → 😮
- sleep → 😴
- sick → 🤢
- scared → 😱

### Nature & Weather
- sun → ☀️
- moon → 🌙
- cloud → ☁️
- rain → 🌧️
- snow → ❄️
- flower → 🌸
- tree → 🌳

### Animals
- cat → 🐱
- dog → 🐶
- bird → 🐦
- fish → 🐟

### Food & Drinks
- pizza → 🍕
- burger → 🍔
- coffee → ☕
- beer → 🍺
- wine → 🍷
- cake → 🎂
- apple → 🍎
- banana → 🍌
- grapes → 🍇

### Transportation
- car → 🚗
- plane → ✈️
- rocket → 🚀
- bike → 🚲
- train → 🚂

### Buildings & Places
- house → 🏠
- building → 🏢
- school → 🏫
- hospital → 🏥
- church → ⛪

### Objects & Technology
- phone → 📱
- computer → 💻
- camera → 📷
- book → 📚
- pen → ✒️

### Symbols & Actions
- love, heart → ❤️
- fire → 🔥
- star → ⭐
- party → 🎉
- gift → 🎁
- music → 🎵
- money → 💰
- trophy → 🏆
- check → ✅
- cross → ❌
- warning → ⚠️
- question → ❓
- idea → 💡
- thumbs up → 👍
- thumbs down → 👎
- clap → 👏
- wave → 👋
- punch → 👊

## 🛠️ How It Works

1. **Sort & Process**: Handles longest phrases first (e.g., "thumbs up" before "up")
2. **Pattern Match**: Uses regex with word boundaries for accurate matching
3. **Replace & Output**: Substitutes keywords with emojis, then displays or saves

## ⚙️ Customization

### Add Your Own Emojis
Edit the `EMOJI_DICT` in the script:
```python
EMOJI_DICT = {
    'happy': '😊',
    'your_word': '🎯',  # Add your custom mapping
}
```


## ⚠️ Important Notes

- **Word Boundaries**: Only complete words are replaced (e.g., "unhappy" won't match "happy")
- **Case Insensitive**: By default, matches any case variation
- **Multi-word Phrases**: Supports phrases like "thumbs up" and "thumbs down"
- **Emoji Support**: Requires UTF-8 encoding and emoji-compatible display


## 🤝 Contributing

Issue #835 Text Emoji Replacer
