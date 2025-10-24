# 📰 News Headlines Sentiment Analyzer

A simple Python script that fetches the latest U.S. news headlines and performs a quick sentiment check using lists of positive and negative words. Perfect for a lightweight peek into how “positive” or “negative” today’s headlines sound!

### ✨ **Features**

- **Live Headlines:** Fetches current top headlines from [News API](https://newsapi.org/)
- **Word-Based Sentiment:** Counts how many positive and negative words appear in each headline
- **Readable Output:** Prints each headline with its sentiment word counts
- **Lightweight:** Uses only Python’s standard libraries + `requests`

### ⚙️ **Setup**

1. Make sure you have **Python 3.x** installed.
2. Install the required dependency:
    
    ```bash
    pip install requests
    ```
    
3. Get your free API key from [newsapi.org](http://newsapi.org/)
4. Set the API key as an environment variable:

**macOS / Linux:**

```bash
export NEWS_API_KEY="your_api_key_here”
```

*(to make it permanent, add this line to your `~/.bashrc` or `~/.zshrc`)*

**Windows (PowerShell):**

```powershell
setx NEWS_API_KEY "your_api_key_here"
```

### 📂 **File Structure**

```
├── #1024_mini_news_headline_analyzer.py
├── positive-words.txt
└── negative-words.txt
```

### 🚀 **Usage**

Run the script:

```bash
python #1024_mini_news_headline_analyzer.py
```

Example Output:

```rust
'Markets surge as tech stocks rebound' → {'num_pos_words': 2, 'num_neg_words': 0}
'Wildfires cause major damage across the west' → {'num_pos_words': 0, 'num_neg_words': 1}
```

### 🧠 **How It Works**

- Fetches top U.S. headlines from the News API
- Loads positive and negative words from the text files
- Counts how many occur in each headline
- Prints a quick sentiment summary for each one

### 🪪 **License**

MIT License — free to use, modify, and share.