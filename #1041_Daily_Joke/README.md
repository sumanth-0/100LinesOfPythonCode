# 😂 Daily Joke Fetcher

A simple Python script that fetches and displays a **new joke every day** from public APIs directly in your terminal.  
No API keys are required, and jokes are cached locally so you only get one joke per day.

---

## 🧠 Features
- Fetches jokes from **public APIs**:
  - Official Joke API
  - JokeAPI (v2)
- Caches the joke locally per day (`~/.cache/daily_joke.json`)  
- Optional **force refresh** to get a new joke anytime
- PEP 8 compliant and under 100 lines
- Works on **Windows, macOS, and Linux terminals**

---

## 🛠️ Requirements
- Python 3.6 or higher
- Internet connection (for fetching jokes)

---

## 🚀 Usage

### Run normally
```bash
python daily_joke.py
```

### Force to get new joke
```bash
python daily_joke.py --force
```