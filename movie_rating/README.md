# 🎬 Movie Ratings CLI

A simple command-line tool to fetch **IMDb ratings** and basic info for any movie using the [OMDb API](http://www.omdbapi.com/).

---

## ⚡ Features

- Fetch **IMDb rating**, year, genre, and director
- Interactive prompt or command-line argument
- Lightweight and easy to use

---

## 💻 Usage

### 1️⃣ Install dependencies
```bash
pip install requests
```
### 2️⃣ Run the CLI
Option 1: Interactive prompt
```bash
python movie.py
```
Then type the movie title when prompted:
Enter movie title: Inception

Option 2: Command-line argument
```bash
python movie.py "Inception"
```
### 3️⃣ Sample Output
Title: Inception      
Year: 2010      
IMDb Rating: 8.8/10      
Genre: Action, Adventure, Sci-Fi      
Director: Christopher Nolan      

---
## 📌 Notes
- Replace API_KEY in movie.py with your OMDb API key.

