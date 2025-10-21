# 😂 Daily Random Joke Fetcher

Fetches a random joke daily from various joke APIs and displays it with smart caching to ensure you get one joke per day!

## 🌟 Features

- **Multiple Joke APIs** - Fetches from 3 different joke sources:
  - JokeAPI (v2.jokeapi.dev)
  - Official Joke API
  - icanhazdadjoke
- **Smart Caching** - One joke per day (cached locally)
- **Joke History** - View jokes from previous days
- **Force New Joke** - Get a new random joke anytime
- **Beautiful Formatting** - Clean, readable output with emojis
- **Automatic API Rotation** - Tries different APIs for variety
- **Error Handling** - Graceful fallback if APIs are unavailable

## 📋 Requirements

- Python 3.6+
- `requests` library

## 🚀 Installation

1. Install the required package:
```bash
pip install requests
```

2. Run the program:
```bash
python main.py
```

## 💻 Usage

The program offers 4 options:

### 1. Get Today's Joke
Shows the cached joke for today. If no joke exists for today, fetches a new one.

### 2. Get a New Random Joke
Forces fetching a new joke from the API, ignoring the cache.

### 3. View Joke History
Displays jokes from the last 7 days.

### 4. Exit
Exits the program.

## 📝 Example Output

```
======================================================================
😂 DAILY JOKE OF THE DAY 😂
======================================================================
📅 Date: October 21, 2025
⏰ Time: 02:30 PM
🔗 Source: JokeAPI
======================================================================

Why don't scientists trust atoms?

Because they make up everything!

======================================================================
```

## 🔧 How It Works

1. **Caching System**: 
   - Stores one joke per day in `daily_joke_cache.json`
   - Prevents redundant API calls
   - Maintains joke history

2. **API Rotation**:
   - Automatically rotates between different joke APIs
   - Provides variety in joke styles
   - Ensures reliability if one API is down

3. **Smart Fetching**:
   - Checks cache first for today's date
   - Only fetches from API if needed
   - Tries multiple APIs if one fails

## 🎯 Joke APIs Used

### 1. JokeAPI
- URL: `https://v2.jokeapi.dev/joke/Any?safe-mode`
- Supports both single and two-part jokes
- Safe mode enabled (no offensive content)

### 2. Official Joke API
- URL: `https://official-joke-api.appspot.com/random_joke`
- Clean programming and general jokes
- Two-part format (setup + punchline)

### 3. icanhazdadjoke
- URL: `https://icanhazdadjoke.com/`
- Dad jokes collection
- Single-line format

## 📂 Files Created

- `main.py` - Main program
- `daily_joke_cache.json` - Auto-generated cache file (stores jokes)

## 🎨 Features Breakdown

### Caching System
- Saves jokes with date, source, and timestamp
- Automatically creates cache file on first run
- Prevents fetching the same joke multiple times

### Error Handling
- Gracefully handles API failures
- Tries alternative APIs
- Shows friendly error messages

### User Interface
- Clean menu system
- Colored emojis for visual appeal
- Formatted joke display with metadata

## 🔄 Daily Usage

Run the program daily to get a fresh joke! The program ensures:
- Only one joke is fetched per day (saves API calls)
- Cached joke is shown if you run multiple times per day
- History keeps track of previous jokes

## 🚀 Automation Ideas

### Windows Task Scheduler
Schedule to run at 9 AM daily:
```bash
python "path\to\main.py"
```

### Linux/Mac Cron
Add to crontab:
```bash
0 9 * * * python3 /path/to/main.py
```

### Auto-Display
Modify the script to automatically display and exit:
```python
if __name__ == "__main__":
    fetcher = DailyJokeFetcher()
    joke, source, is_cached = fetcher.get_daily_joke()
    fetcher.display_joke(joke, source, is_cached)
```

## 🤝 Contributing

Feel free to:
- Add more joke APIs
- Improve joke formatting
- Add joke categories/filters
- Implement joke rating system

## 📄 License

This project is open source and available for educational purposes.

---

**Start your day with a laugh! 😂**
