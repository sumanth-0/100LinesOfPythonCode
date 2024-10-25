# Import necessary libraries
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import random
import tkinter as tk

# Download VADER lexicon
nltk.download('vader_lexicon')

# Define a function to perform sentiment analysis and suggest a random playlist
def suggest_playlist(text):
    # Initialize VADER sentiment analyzer
    sia = SentimentIntensityAnalyzer()
    
    # Get sentiment scores
    sentiment_scores = sia.polarity_scores(text)
    
    # Define large lists of songs for each mood with trending songs
    positive_songs = [
        "Flowers - Miley Cyrus", "As It Was - Harry Styles", 
        "About Damn Time - Lizzo", "Levitating - Dua Lipa", 
        "Bad Habits - Ed Sheeran", "Good 4 U - Olivia Rodrigo", 
        "Stay - The Kid LAROI & Justin Bieber", "Blinding Lights - The Weeknd", 
        "Peaches - Justin Bieber", "Heat Waves - Glass Animals"
    ]
    
    negative_songs = [
        "When the Party's Over - Billie Eilish", "Someone You Loved - Lewis Capaldi", 
        "Goodbye Yellow Brick Road - Elton John", "Back to Black - Amy Winehouse", 
        "Lose You to Love Me - Selena Gomez", "Nights - Frank Ocean", 
        "Skinny Love - Bon Iver", "Creep - Radiohead", 
        "Breathe Me - Sia", "Hurt - Nine Inch Nails"
    ]
    
    neutral_songs = [
        "Sunflower - Post Malone & Swae Lee", "Electric Feel - MGMT", 
        "Royals - Lorde", "Take Me to Church - Hozier", 
        "Riptide - Vance Joy", "Stressed Out - Twenty One Pilots", 
        "Old Town Road - Lil Nas X", "Dance Monkey - Tones and I", 
        "Young Folks - Peter Bjorn and John", "Shivers - Ed Sheeran"
    ]
    
    # Randomly choose 5 songs from the relevant list
    if sentiment_scores['compound'] >= 0.05:
        mood = 'Positive'
        playlist = random.sample(positive_songs, 5)
    elif sentiment_scores['compound'] <= -0.05:
        mood = 'Negative'
        playlist = random.sample(negative_songs, 5)
    else:
        mood = 'Neutral'
        playlist = random.sample(neutral_songs, 5)
    
    # Update the result label with mood and playlist
    result_text = f"Detected Mood: {mood}\n\nSuggested Playlist:\n" + "\n".join(f"- {song}" for song in playlist)
    result_label.config(text=result_text)

# Function to get input from the text box and perform sentiment analysis
def get_entry_and_analyze():
    diary_entry = text_box.get("1.0", tk.END).strip()  # Get the text from the text box
    suggest_playlist(diary_entry)

# Set up the GUI window
root = tk.Tk()
root.title("Sentiment-based Playlist Suggester")

# Create a label for the input box
label = tk.Label(root, text="Enter your diary entry or text below:")
label.pack(pady=10)

# Create a text box for user input
text_box = tk.Text(root, height=10, width=50)
text_box.pack(pady=10)

# Create a button to submit the text and analyze
submit_button = tk.Button(root, text="Analyze and Suggest Playlist", command=get_entry_and_analyze)
submit_button.pack(pady=10)

# Create a label to display the result below the input box
result_label = tk.Label(root, text="", justify=tk.LEFT, anchor='w')
result_label.pack(pady=10)

# Start the GUI loop
root.mainloop()
