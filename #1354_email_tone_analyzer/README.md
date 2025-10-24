# 📧 Email Tone Analyzer

A simple Python program that analyzes if an email sounds **Friendly**, **Rude**, or **Formal** using rule-based text analysis — no machine learning required!  
It uses keyword detection, punctuation patterns, and tone indicators to estimate the overall sentiment of an email.

---

## 🧠 Description

This program analyzes a given email message by scanning for:
- **Friendly** words like “thanks”, “hello”, “cheers”
- **Rude** expressions such as “stupid”, “nonsense”, or “useless”
- **Formal** phrases like “dear”, “sincerely”, and “please find attached”

It then assigns a score for each tone category and reports which one dominates.  
If two or more tones have similar scores, it classifies the email as **Mixed**.

---

## ✨ Features

✅ Detects three tones: **Friendly**, **Rude**, **Formal**  
✅ Simple and rule-based — works offline  
✅ Under 100 lines of clean Python code  
✅ Handles punctuation and common polite/rude phrases  
✅ Provides a score breakdown and a clear result  

---

## 🚀 How to Run

### 1️⃣ Clone or Download
Download the script or clone the repository:
```bash
git clone https://github.com/yourusername/email-tone-analyzer.git
cd email-tone-analyzer
### to run the code 
python3 email_tone_analyzer.py
