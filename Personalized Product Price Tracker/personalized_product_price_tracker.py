import requests
from bs4 import BeautifulSoup
import time

def check_price(url, target_price):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36"
    }

    print("Fetching the product page...")
    response = requests.get(url, headers=headers)
    print("Response received.")

    if response.status_code != 200:
        print(f"Error fetching page: {response.status_code}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')

    # Adjust this selector based on the actual price element
    price_element = soup.select_one('.a-price .a-offscreen')  # Example selector
    if price_element:
        current_price = float(price_element.get_text(strip=True).replace('₹', '').replace(',', ''))
        print(f"Current price: ₹{current_price}")

        if current_price <= target_price:
            print(f"Price alert! The price has dropped to ₹{current_price}!")
    else:
        print("Price element not found. Check the selector.")

if __name__ == "__main__":
    url = input("Enter the product URL: ")
    target_price = float(input("Enter your target price: "))

    while True:
        check_price(url, target_price)
        time.sleep(3600)  # Check every hour
