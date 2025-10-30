# 📝 Extractive Text Summarizer (Python)

A **Python-based extractive text summarization tool** that condenses long paragraphs into a shorter summary by selecting the most important sentences.  
This project uses **NLTK (Natural Language Toolkit)** for text processing and a simple **frequency-based scoring** approach.

---

## 📋 Overview

Extractive summarization works by **identifying key sentences** in a text that best represent its content. Unlike abstractive summarization, which generates new sentences, extractive methods **select sentences directly from the source**.  

This script:
- Tokenizes the text into **words and sentences**
- Removes **stopwords** and punctuation
- Computes **word frequencies**
- Scores each sentence based on the frequency of words it contains
- Selects the top N sentences as the summary

It is a **lightweight, interpretable, and easy-to-use summarizer** ideal for small to medium-length text data.

---

## ⚙️ Features

- 📄 Extracts the most important sentences from a paragraph  
- 🧠 Uses NLTK for natural language processing  
- 🗑 Removes common stopwords for accurate sentence scoring  
- ⚡ Rule-based, frequency-driven summarization  
- 🔧 Customizable summary length (`SUMMARY_SIZE`)  

---