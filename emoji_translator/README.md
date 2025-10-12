# 🎉 Emoji Translator

A fun Python CLI tool that converts text to emojis and vice versa! Perfect for adding some emoji magic to your messages.

## ✨ Features

- 🔄 **Bidirectional Translation**: Convert text to emojis and emojis back to text
- 💬 **Multi-word Support**: Handles phrases and multiple words intelligently
- 🎮 **Interactive Mode**: Real-time translation with easy-to-use interface
- 💻 **CLI Mode**: Quick translations from the command line
- 🎨 **60+ Emoji Mappings**: Comprehensive dictionary covering emotions, food, nature, animals, activities, objects, people, and symbols

## 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/sumanth-0/100LinesOfPythonCode.git
cd 100LinesOfPythonCode/emoji_translator

# Make the script executable (optional)
chmod +x emoji_translator.py
```

## 📚 Usage

### Interactive Mode

```bash
python emoji_translator.py
```

Then follow the prompts:
- Type text to convert to emojis
- Type `reverse` to switch to emoji-to-text mode
- Type `help` for assistance
- Type `quit` to exit

### Command-Line Mode

```bash
python emoji_translator.py I love pizza and coffee
# Output: I ❤️ 🍕 and ☕

python emoji_translator.py Happy birthday! Let's celebrate with cake
# Output: 😊 birthday! Let's 🎊 with 🎂
```

## 🎯 Examples

```python
# Text to Emoji
"I love pizza" → "I ❤️ 🍕"
"Happy cat playing music" → "😊 🐱 playing 🎵"
"Sun and moon in the sky" → "☀️ and 🌙 in the sky"

# Emoji to Text
"🍕 ❤️ 🍔" → "[pizza] [love] [burger]"
"😊 🐱 🐶" → "[happy] [cat] [dog]"
```

## 📝 Supported Words

- **Emotions**: love, happy, sad, angry, laugh, smile, cry, cool, excited, etc.
- **Food**: pizza, burger, coffee, tea, cake, sushi, taco, ramen, etc.
- **Nature**: sun, moon, star, cloud, rain, snow, fire, water, tree, flower, etc.
- **Animals**: cat, dog, bird, fish, monkey, lion, tiger, bear, panda, etc.
- **Activities**: party, music, dance, football, basketball, game, movie, etc.
- **Objects**: phone, computer, car, plane, rocket, home, money, crown, etc.
- **People**: king, queen, baby, family, hand, etc.
- **Symbols**: check, cross, warning, question, exclamation, etc.

## 🔧 Requirements

- Python 3.6+
- No external dependencies required!

## 💯 Code Quality

- **90 lines of code** (under the 100-line requirement)
- Clean, well-documented code
- Type hints and docstrings included
- Follows Python best practices

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Add more emoji mappings
- Improve the translation algorithm
- Add new features
- Fix bugs

## 📜 License

This project is part of the 100LinesOfPythonCode collection.

## 👤 Author

Created for issue [#647](https://github.com/sumanth-0/100LinesOfPythonCode/issues/647)

---

Made with ❤️ and Python 🐍
