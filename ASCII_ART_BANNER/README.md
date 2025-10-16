# ASCII Banner Generator

Generate stylish ASCII banners in your terminal using Python! This project includes both a **dependency-free version** and an **advanced version with fonts and colors**.  

---

## Features

- Display large, stylish ASCII banners for A–Z, 0–9, and spaces  
- Custom colors: red, green, yellow, blue, magenta, cyan, white  
- Interactive input: enter multiple texts continuously  
- Exception handling for invalid characters, colors, or fonts  
- Exits cleanly on `q`  
- Optional advanced version supports multiple fonts via `pyfiglet`  
- Dependency-free version uses only Python 3 standard library  

---

## How to Use
1. **Dependency-Free Version:**  
```bash
python ascii_banner.py 
```

Advanced Version (with fonts):
```bash
pip install pyfiglet
python ascii_banner_advanced.py
```
Enter your text
Choose a font (default applied if invalid)
Choose a color
Press q to quit
