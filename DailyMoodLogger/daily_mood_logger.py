from textblob import TextBlob
import matplotlib.pyplot as plt
from datetime import datetime
import re

def get_sentiment(text):
    """Compute sentiment polarity (-1 negative to 1 positive)."""
    blob = TextBlob(text)
    return blob.sentiment.polarity

def parse_date(date_str):
    """Parse date string to datetime object."""
    formats = ['%Y-%m-%d', '%m/%d/%Y', '%d-%m-%Y']
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            pass
    raise ValueError("Invalid date format. Use YYYY-MM-DD, MM/DD/YYYY, or DD-MM-YYYY.")

def main():
    entries = []
    print("Journal Mood Analyzer")
    print("Enter journal entries (date: text). Type 'done' to finish.")
    
    while True:
        line = input("Entry (or 'done'): ").strip()
        if line.lower() == 'done':
            break
        try:
            # Assume format "YYYY-MM-DD: text here"
            date_str, text = line.split(':', 1)
            date = parse_date(date_str.strip())
            sentiment = get_sentiment(text.strip())
            entries.append((date, sentiment))
        except ValueError as e:
            print(f"Error: {e}. Skipping.")
    
    if not entries:
        print("No entries added.")
        return
    
    # Sort by date
    entries.sort(key=lambda x: x[0])
    
    dates = [entry[0] for entry in entries]
    moods = [entry[1] for entry in entries]
    
    # Plot
    plt.figure(figsize=(10, 5))
    plt.plot(dates, moods, marker='o', linestyle='-', color='b')
    plt.title('Mood Trends Over Time')
    plt.xlabel('Date')
    plt.ylabel('Sentiment Score (-1 to 1)')
    plt.ylim(-1, 1)
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    # Print summary
    print("\nSummary:")
    for date, mood in entries:
        print(f"{date.strftime('%Y-%m-%d')}: {mood:.2f}")

if __name__ == "__main__":
    main()
