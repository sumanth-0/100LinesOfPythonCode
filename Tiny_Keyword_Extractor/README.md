# Tiny Keyword Extractor 🔑

Extract the most important keywords from any text file based on word frequency, automatically filtering out common stopwords.

## 🎯 What This Script Does

This Python script analyzes text files and identifies the most frequently occurring meaningful words. It automatically filters out common English stopwords (like "the", "and", "is") to focus on the actual keywords that matter.

## ✨ Features

- **No External Dependencies**: Uses only Python's standard library (`re`, `collections`)
- **Smart Filtering**: Automatically removes 60+ common English stopwords
- **Flexible Output**: Extract 5, 10, or any number of top keywords
- **Clean Results**: Displays keywords with their frequency counts
- **Robust Error Handling**: Handles missing files and encoding issues gracefully
- **Two Usage Modes**: Command-line arguments or interactive input

## 🚀 Usage

### Method 1: Command Line Arguments
```bash
# Extract top 10 keywords (default)
python tiny_keyword_extractor.py document.txt

# Extract custom number of keywords
python tiny_keyword_extractor.py document.txt 5
```

### Method 2: Interactive Mode
```bash
python tiny_keyword_extractor.py
```
Then enter the file path and number of keywords when prompted.

## 💡 Examples

### Example 1: Analyze a blog post
```bash
python tiny_keyword_extractor.py blog_post.txt 10
```

### Example 2: Quick analysis
```bash
python tiny_keyword_extractor.py article.txt
```

## 📋 Sample Output

```
============================================================
Tiny Keyword Extractor
============================================================

Top 10 Keywords:
------------------------------------------------------------
 1. python               (appeared 45 times)
 2. data                 (appeared 32 times)
 3. programming          (appeared 28 times)
 4. code                 (appeared 24 times)
 5. learning             (appeared 19 times)
 6. algorithm            (appeared 15 times)
 7. function             (appeared 14 times)
 8. development          (appeared 12 times)
 9. software             (appeared 11 times)
10. computer             (appeared 10 times)
============================================================
```

## 🛠️ How It Works

1. **Read File**: Loads the text file content with UTF-8 encoding
2. **Process Text**: Converts to lowercase and extracts words (3+ letters) using regex
3. **Filter & Count**: Removes stopwords and counts word frequencies with `Counter`
4. **Display Results**: Shows top N keywords ranked by occurrence

## 📝 Stopwords Included

The script filters out 60+ common stopwords including:
- Articles: a, an, the
- Conjunctions: and, or, but
- Prepositions: in, on, at, to, from
- Pronouns: I, you, he, she, it, we, they
- Common verbs: is, are, was, were, have, has
- And many more...

## ⚙️ Customization

You can easily customize the script by:
- **Adding More Stopwords**: Edit the `STOPWORDS` set
- **Changing Minimum Word Length**: Modify the regex pattern `r'\b[a-z]{3,}\b'`
- **Supporting Other Languages**: Add language-specific stopwords
- **Case Sensitivity**: Remove the `.lower()` conversion


## ⚠️ Limitations

- Currently supports English stopwords only
- Doesn't handle multi-word phrases (bigrams/trigrams)
- No stemming or lemmatization (e.g., "running" and "run" are separate)
- Requires plain text files (doesn't parse PDFs or Word documents)

## 🎓 Learning Points

This script demonstrates:
- Regular expressions for efficient text parsing
- Using Python's `Counter` for frequency analysis
- File I/O with proper error handling
- Command-line argument processing
- Writing concise, readable code under 100 lines

## 🤝 Contributing

Issue #836 Tiny Keyword Extractor
