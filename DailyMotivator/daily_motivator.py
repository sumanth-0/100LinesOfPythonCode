import schedule
import time
import requests

def send_motivation():
    response = requests.get("https://api.quotable.io/random")
    quote = response.json()["content"]
    print(quote)  # Replace with your preferred notification method

schedule.every().day.at("09:00").do(send_motivation)  # Adjust time as needed

while True:
    schedule.run_pending()
    time.sleep(1)
