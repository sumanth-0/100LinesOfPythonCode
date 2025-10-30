# 📝 Fake Product Review Generator

A fun Python script that automatically generates **random, human-like product reviews** using customizable vocabulary lists and templates.  
Perfect for testing, demos, or just having fun with procedurally generated text.

---

## 🚀 Features

- 🧠 Generates **unique, randomized product reviews**
- 🗣️ Uses varied **adjectives**, **nouns**, and **verbs** for natural phrasing
- 🧩 Employs multiple **sentence templates** for better variety
- ⚙️ Easily extendable — add your own words or templates
- 💬 Prints multiple reviews at once for bulk generation

---

## 🧠 How It Works

The script randomly selects:
- 1–2 **adjectives**
- 1–2 **nouns**
- 1 **verb**
- 1 **sentence template**

It then fills the placeholders in the chosen template to create a natural-sounding review.


---

## ⚙️ Configuration

| Variable | Default | Description |
|-----------|----------|-------------|
| `NUM_REVIEWS` | `5` | Number of reviews to generate per run |
| `ADJECTIVES`, `NOUNS`, `VERBS` | Lists of strings | Word banks used for random selection |
| `TEMPLATES` | List of sentence structures | Determines the style of generated reviews |

To modify behavior, edit these constants directly in the script.

---
