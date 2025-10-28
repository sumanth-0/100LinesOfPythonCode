# 💱 Currency Converter (Python + ExchangeRate API)

A simple Python-based currency converter that uses the [**ExchangeRate API**](https://www.exchangerate-api.com/) to:
- Fetch live exchange rates for all currencies  
- Convert specific currency pairs (e.g., EUR → GBP)  
- Retrieve historical exchange rate data for a given date  

---

## 🚀 Setup

## Requirements
This tool uses the following libraries:-
- python-dotenv
- requests 

## Installation
### 1. Install Python from [python.org](https://www.python.org/downloads/) if you don't have it.
### 2. Install requirements via pip:
2.1 navigate to directory 
```bash
cd "#1567_CURRENCY_CONVERTER"
```
2.2 then install the requirements
```bash
pip install -r requirements.txt
 ```

## API key
create a .env file by copying .env.example and substituting your api key
```bash
cp .env.example .env
```

## Running the script
```bash
python currency_converter.py
```

## Features
1. list all live exchange rates for a currency
2. conversion between currencies using live exchange rate
3. list historical exchange rates for a currency 

