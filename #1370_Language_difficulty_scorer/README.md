# 🧠 Text Complexity Estimator

## 📖 Description
The **Text Complexity Estimator** is a simple command-line Python tool that analyzes how complex a piece of text is based on **sentence length** and **vocabulary diversity**.  
It provides a **complexity score** and categorizes the text as **Simple**, **Moderate**, or **Complex**, helping writers, students, and developers quickly gauge readability.

---

## 🌟 Features

- ✏️ **Automatic Sentence Splitting** — Detects sentences using punctuation marks.  
- 🧩 **Word Tokenization** — Identifies and counts all valid words.  
- 📊 **Average Sentence Length** — Measures how long your sentences are on average.  
- 🔠 **Vocabulary Richness** — Calculates the ratio of unique words to total words.  
- 🎯 **Complexity Scoring System** — Generates a readability score (0–10).  
- 🟢 **Clear Difficulty Rating** — Classifies text as *Simple*, *Moderate*, or *Complex*.  
- 💻 **No Dependencies** — Uses only Python’s built-in libraries.  

---

## 🧮 How It Works

1. **Input any text** into the program.  
2. The tool analyzes:
   - **Average Sentence Length** → longer sentences = higher complexity.  
   - **Vocabulary Richness** → more unique words = lower complexity.  
3. Combines these factors into a **Complexity Score** (0–10).  
4. Displays a **readable summary** of your text’s structure and difficulty.

---

## 🧰 Requirements
- **Python 3.x**  
- No external libraries required  

---

## 🚀 How to Run

```bash
# Clone the repository
git clone <repository-url>
cd text_complexity_estimator

# Run the program
python text_complexity_estimator.py
