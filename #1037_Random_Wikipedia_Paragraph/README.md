# 📖 Random Wikipedia Paragraph Fetcher

A simple Python program that fetches and displays the first paragraph of a random Wikipedia article using the Wikipedia API.

## 🌟 Features

- Fetches random Wikipedia articles
- Displays the article title and first paragraph
- Provides a link to read the full article
- Interactive mode - fetch multiple articles in one session
- Clean, formatted output
- Error handling for network issues

## 📋 Requirements

- Python 3.6+
- `requests` library

## 🚀 Installation

1. Install the required package:
```bash
pip install requests
```

## 💻 Usage

Run the program:
```bash
python main.py
```

The program will:
1. Fetch a random Wikipedia article
2. Display the title and first paragraph
3. Show a link to the full article
4. Ask if you want to fetch another random article

## 📝 Example Output

```
🌐 Fetching a random Wikipedia article...

======================================================================
📖 RANDOM WIKIPEDIA ARTICLE
======================================================================

🔖 Title: Python (programming language)

📝 First Paragraph:
Python is a high-level, interpreted, general-purpose programming language...

🔗 Read more: https://en.wikipedia.org/wiki/Python_(programming_language)
======================================================================

Would you like another random article? (y/n):
```

## 🔧 How It Works

The program uses the Wikipedia REST API endpoint:
- `https://en.wikipedia.org/api/rest_v1/page/random/summary`

This endpoint returns a random article summary, which includes:
- Article title
- First paragraph (extract)
- URL to the full article
- Other metadata

## 📚 API Documentation

Wikipedia API Documentation: https://en.wikipedia.org/api/rest_v1/

## 🤝 Contributing

Feel free to fork this project and submit pull requests with improvements!

## 📄 License

This project is open source and available for educational purposes.
