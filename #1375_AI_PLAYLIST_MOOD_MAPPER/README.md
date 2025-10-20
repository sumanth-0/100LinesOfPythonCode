# 🎧 AI Playlist Mood Mapper

### 🧠 Detect a song’s mood — happy, sad, or chill — using NLP and AI

This lightweight Python tool analyzes a song title and predicts its mood using a combination of:
- **Keyword analysis**
- **Sentiment polarity (TextBlob)**
- **Semantic similarity (SentenceTransformer, optional)**

It’s perfect for playlist organization, music analysis projects, or just experimenting with simple NLP!

---

## 🚀 Features

✅ Detects moods (`happy`, `sad`, `chill`, or `unknown`)  
✅ Uses three scoring systems — **keywords**, **sentiment**, and **semantic similarity**  
✅ Works offline (semantic mode optional)  
✅ Easy to extend with new moods or keywords  
✅ Under **100 lines** of clean, well-commented code  

---

## 🧩 Example Output

```bash
🎧 AI Playlist Mood Mapper Results
----------------------------------------
Tears in Heaven           → SAD (78%)
Good Vibes Only           → HAPPY (91%)
Lost at Midnight          → SAD (65%)
Dancing in the Sun        → HAPPY (88%)
Ocean Breeze              → CHILL (84%)



1️⃣ Clone the Repository
git clone https://github.com/yourusername/AI-Playlist-Mood-Mapper.git
cd AI-Playlist-Mood-Mapper

2️⃣ Create a Virtual Environment (optional)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

3️⃣ Install Dependencies
pip install textblob


💡 Optional (for deeper analysis):

To enable semantic mood detection, also install:
pip install sentence-transformers


🧪 Usage

Run the script directly:
python ai_playlist_mood.py



Or analyze any custom title from your terminal:
python ai_playlist_mood.py "Dancing Alone in the Dark"