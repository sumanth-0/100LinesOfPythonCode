# 🎯 Flask Number Guessing Game

A fun web-based number guessing game built using **Flask**, **HTML**, **CSS**, and **JavaScript**.  
The server randomly selects a number between **1** and **100**, and the player tries to guess it.  
Feedback ("Too Low", "Too High", or "Correct") is displayed instantly.

## 🚀 How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
2. Start the Flask server:
    python app.py
3. Open your browser and visit:
    http://127.0.0.1:5001

**🎮 How It Works**

1. Submit Guess: Sends your number to the backend (/api/guess) and gets feedback.

2. Your Last Guess: Fetches your previous guess using the /api/status endpoint.

3. When you guess correctly, a new random number is generated automatically.