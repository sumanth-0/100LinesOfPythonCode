# Random Quote Generator

A clean, professional CLI tool to fetch, display, save, and view inspirational quotes using the [Quotable API](https://github.com/lukePeavey/quotable). Built with **Python** and **Rich** for beautiful terminal output.

---

## Features

* Fetch random quotes from the Quotable API
* Save favorite quotes locally
* View saved quotes
* Clean, professional terminal interface with panels and custom font headings
* Cross-platform compatible (Windows, macOS, Linux)

---

## Requirements

* Python 3.8+
* Packages:

  * `requests`
  * `rich`
  * `pyfiglet`

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/random-quote-generator.git
cd random-quote-generator
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

> Or install manually:

```bash
pip install requests rich pyfiglet
```

---

## Usage

Run the script:

```bash
python runner.py
```

* You will see a heading and a random quote displayed in a styled panel.
* Options after each quote:

  * `save` – Save the current quote locally
  * `next` – Fetch another random quote
  * `view` – View all saved quotes
  * `exit` – Exit the program

Saved quotes are stored in `saved_quotes.json` in the project directory.

---

## Screenshots

*(Add terminal screenshots here showing quote display and saved quotes view)*

---

## Notes

* The script disables SSL verification to avoid certificate errors with the API. It is safe for local CLI use.
* Compatible with Windows, macOS, and Linux terminals.
* Designed for simplicity, professional appearance, and usability.

---


