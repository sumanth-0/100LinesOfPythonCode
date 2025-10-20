# Typing Speed Racer

A simple Python-based typing speed and accuracy test that fetches random sentences directly from **Wikipedia** using their public API. The player types the displayed sentence as quickly and accurately as possible, and the program calculates their **Words Per Minute (WPM)** and **accuracy**.

---

## Features

- Fetches a **random sentence** from Wikipedia via the API.  
- Measures **typing speed** (WPM) based on elapsed time.  
- Evaluates **accuracy** by comparing typed words to the original sentence.  
- Allows the user to **play multiple rounds** in one session.  
- Lightweight and runs entirely in the terminal.

---

## How It Works

1. A random Wikipedia article is fetched.  
2. The first sentence of the article is displayed.  
3. The user presses `Enter` to start, types the sentence, and presses `Enter` again when done.  
4. The program calculates:
   - **Words Per Minute (WPM)** = number of words typed ÷ time taken × 60  
   - **Accuracy (%)** = number of correctly typed words ÷ total words × 100  
5. The results are printed to the console.  
6. The user can press `n` to fetch a new sentence or any other key to quit.

---

## Requirements

- Python 3.7 or higher  
- `requests` library  

Install dependencies with:
```bash
pip install requests
```

---

## Usage

1. Clone or download this repository.  
2. Open a terminal in the project directory.  
3. Run the program:
   ```bash
   python main.py
   ```
4. Follow the on-screen instructions.

---

## Example Output

```
Press Enter when you're ready to type the sentence:
Python is a widely used high-level programming language.
Python is a widely used high-level programming language.
Results:
Words Per Minute (WPM): 42.31
Accuracy (% of words typed correctly): 100.00%
Type 'n' for a new sentence or any other key to exit: 
```

---

## File Overview

| File | Description |
|------|--------------|
| `main.py` | Main program containing all logic (fetching, timing, and results) |
| `README.md` | Project documentation |

---

## Next Steps / Ideas

- Add difficulty levels (short vs. long sentences).  
- Include punctuation accuracy checking.  
- Display leaderboard for multiple players.  
- Create a GUI version with Tkinter or Streamlit.  