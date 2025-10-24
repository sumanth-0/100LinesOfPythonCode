💬 Positive vs Negative Sentiment Visualizer
🧠 Overview
This Python script analyzes and visualizes positive vs negative sentiment across multiple paragraphs entered by the user.
It uses NLTK’s VADER sentiment analyzer and Matplotlib to produce a diverging bar chart that shows how emotionally positive or negative each paragraph is.

⚙️ Features
✅ Takes multiple paragraph inputs directly from the user
✅ Computes sentiment scores (pos, neg, neu, compound)
✅ Displays a clean diverging horizontal bar chart
✅ Works entirely offline after first lexicon download
✅ Auto-repairs missing NLTK data (optional code block below)

🧩 Requirements
Make sure you have Python 3.9+ (works with 3.13 too) and install dependencies:

pip install nltk matplotlib

If NLTK fails to download data due to SSL issues (macOS users), fix it via:

/Applications/Python\ 3.13/Install\ Certificates.command

Then:
python3 -m nltk.downloader vader_lexicon

🚀 Usage
Run the script:
python3 pos_neg_sentiment.py


Enter paragraphs one by one, for example:

I love the design and color of this product!
It was okay, not the best but not terrible either.
I'm really disappointed, it broke after one use.


Press Enter twice to finish.
A sentiment visualization window will appear 🎨

📊 Visualization
Green bars → Positive sentiment
Red bars → Negative sentiment
Labels like compound = 0.85 summarize overall emotion strength

🧠 Example Output
Paragraph	Positive	Negative	Compound
P1	        0.78	        0.05	        0.85
P2		0.32		0.25		0.10
P3		0.04		0.65		-0.70

And a visual chart like:

← Negative              Positive →
|███████████▌         ████████████|

