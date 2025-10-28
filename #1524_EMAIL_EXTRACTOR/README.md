# Email Extractor Script

## Overview
This Python script extracts **valid email addresses** from any text or HTML file.  
It handles encoded characters like `&#64;` (`@`) and ignores invalid email-like patterns.

---

## Files Included
| File Name | Description |
|------------|-------------|
| `extract_emails.py` | Main Python script for extracting emails |
| `index.html` | Sample HTML file for testing |
| `sample.txt` | Sample text file for testing |

---

##  Requirements
- Python 3.7 or higher  
- Works on Windows, macOS, and Linux  
- No external libraries required

---

##  Usage

```bash
python extract_emails.py <filename>
```

### Example 1: Extract from HTML
```bash
python extract_emails.py index.html
```

### Example 2: Extract from Text
```bash
python extract_emails.py sample.txt
```

---

## 🧪 Sample Output

For the provided `index.html`, output will be similar to:

```
Found 4 email address(es):

abcdef123g@gmail.com
hr.department@company.org
james.dean@example.com
marketing@brand.co.uk
support@webmail.com
```

---

