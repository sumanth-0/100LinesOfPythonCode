# 🧠 Word to Emoji Replacer

A simple and fun Python program that replaces common words in your text with their corresponding emojis 🎉.  
The program works in **case-insensitive** mode and supports both **example conversions** and an **interactive mode** where you can enter your own text.

---

## ✨ Features

- 🔤 Replaces common words with emojis (e.g., `love` → ❤️, `happy` → 😊)
- 🔍 Case-insensitive word matching
- 🚫 Avoids partial word matches (e.g., “lover” won’t replace “love”)
- 🧩 Includes an **interactive mode** for user input
- 💬 Easy to extend — just add new words to the emoji map!

---

## 📦 Requirements

This program only requires Python (no external libraries needed).

- **Python Version:** 3.x

---

## ⚙️ How to Run

1. **Clone or Download** this repository  
   ```bash
   git clone https://github.com/<your-username>/word-to-emoji-replacer.git
   cd word-to-emoji-replacer
   ```

2. **Run the Python Script**  
   ```bash
   python text-to-emoji-converter.py
   ```

3. You’ll see example conversions first, followed by **interactive mode**:
   ```
   === Word to Emoji Replacer ===

   Examples:
   Original:  I love pizza and coffee!
   Converted: I ❤️ 🍕 and ☕

   --- Interactive Mode ---
   Enter text to convert (or 'quit' to exit):
   > I am happy with my dog
   ✨ I am 😊 with my 🐶
   ```

---

## 🧩 Example Outputs

| Original Sentence | Converted Output |
|--------------------|------------------|
| I love pizza and coffee! | I ❤️ 🍕 and ☕ |
| Happy birthday! Here's a cake and a gift. | 😊 birthday! Here's a 🎂 and a 🎁. |
| The fire is so cool, it's lit! | The 🔥 is so 😎, it's 🔥! |
| My dog and cat make me smile with love. | My 🐶 and 🐱 make me 😃 with ❤️. |
| Let's celebrate and dance under the moon and stars! | Let's 🥳 and 💃 under the 🌙 and ⭐! |

---

## 🧱 Project Structure

```
📁 word-to-emoji-replacer
│
├── text-to-emoji-converter.py         # Main program file
├── README.md       # Project documentation
```

---

## 🧠 How It Works

- The script defines a **dictionary** (`emoji_map`) mapping common English words to their emoji equivalents.
- It uses **regular expressions (`re`)** to find and replace these words while:
  - Matching **whole words only** (`\b` word boundaries)
  - Ignoring **case differences** (`re.IGNORECASE`)
- The function `replace_words_with_emojis(text)` performs the conversion.
- The `main()` function demonstrates usage and allows user interaction.

---

## 🛠️ Customization

Want to add more emojis?  
Simply open `text-to-emoji-converter.py` and add new entries to the `emoji_map`:

```python
emoji_map = {
    'love': '❤️',
    'sun': '☀️',
    'ocean': '🌊',  # <-- add new ones like this
}
```

---

## 🙌 Example Extensions (Optional)

- Handle **plural words** (e.g., `cats` → 🐱)
- Add **phrase replacements** (e.g., “good morning” → 🌅)
- Build a **GUI or web version** using Tkinter or Flask

---

## 🧑‍💻 Author

**Your Name**  
📧 [batabyalsoumi23@gmail.com](mailto:batabyalsoumi23@gmail.com)  
🌐 [github.com/Blackspadesz05](https://github.com/Blackspadesz05)

---

> 💡 *Turn your text into emoji art effortlessly!* 🌟
