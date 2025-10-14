
# 🌍 Text Translation Tool
**A powerful Python-based translation tool using Google Translate API through the googletrans library. Perfect for Hacktoberfest contributions!**

## 📦 Installation
 **Prerequisites**
- Python 3.6+
- pip package manager

## Install Dependencies
```bash
pip install -r requirements.txt
The requirements.txt contains:
```


## 🚀 Quick Start
**Basic Translation bash**
### Translate simple text
python translator.py --text "Hello World" --dest spanish

### Output:
**==================================================**
#### 📝 TRANSLATION RESULT
==================================================
Original (en): Hello World

Translated (es): Hola Mundo
**==================================================**
### Interactive Mode
```bash
python translator.py --interactive
```
This launches an interactive session where you can continuously translate text.

## 📋 Usage Examples
Command Line Options
1. Single Text Translation
bash
### Using language code
```bash
python translator.py --text "Good morning" --dest fr
```
### Using language name 
```bash 
python translator.py --text "Thank you" --dest japanese
```
### Specify source language
```bash
python translator.py --text "Bonjour" --src fr --dest en
```
### **2. File Translation bash**
### Translate content from a file
```bash
python translator.py --file input.txt --dest german
```
### **3. Batch Translation bash**
# Translate multiple texts at once
```bash
python translator.py --batch "Hello" "Goodbye" "Thank you" --dest zh-cn
```
### **4. Language Detection bash**
### Detect language of text
```bash
python translator.py --detect "Hola cómo estás"
```
### Output:
#### Detected language: Spanish (es)
#### Confidence: 99.50%
### **5. Language Support bash**
### List all supported languages
python translator.py --list-langs

### Search for specific languages
python translator.py --search-langs "chinese"
### **6. Save Results bash**
### Save translation to JSON file
python translator.py --text "Hello World" --dest fr --output result.json

## 🌐 Supported Languages
The tool supports 100+ languages including:

Code	Language	Code	Language
en	English	es	Spanish
fr	French	de	German
zh-cn	Chinese	ja	Japanese
ko	Korean	ru	Russian
ar	Arabic	hi	Hindi
View all languages with:

```bash
python translator.py --list-langs
```
### 🔧 Features
- ✅ 100+ Languages - Comprehensive language support
- ✅ Auto-Detection - Automatic source language detection

- ✅ Batch Processing - Translate multiple texts efficiently

- ✅ File Support - Translate content from files

- ✅ Pronunciation - Get pronunciation guides

- ✅ Interactive Mode - User-friendly continuous translation

- ✅ JSON Export - Save results in structured format

- ✅ Language Search - Find languages by name

- ✅ Error Handling - Robust error management


## 🆘 Help

 Display all available options
```bash
python translator.py --help
```
For issues and feature requests, please open an issue on GitHub.

