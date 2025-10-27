import requests
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
import sys

API_KEY = "DEMO_KEY" 
APOD_URL = "https://api.nasa.gov/planetary/apod"


def display_apod_image(date=None):
    
    print(f"Fetching APOD data for date: {'Today' if date is None else date}...")

    params = {
        'api_key': API_KEY,
        'hd': 'True'
    }

    if date:
        params['date'] = date

    try:
      
        response = requests.get(APOD_URL, params=params)
        response.raise_for_status() 
        apod_data = response.json()

        if apod_data.get('media_type') != 'image':
            print("-" * 50)
            print(f"Note: The content for {apod_data.get('date')} is a video/other media, not an image.")
            print(f"Link: {apod_data.get('url')}")
            return
            
        image_url = apod_data.get('hdurl') or apod_data.get('url')
        if not image_url:
            print("Error: Could not find an image URL in the APOD response.")
            return
        print(f"Downloading image from: {image_url}")
        image_response = requests.get(image_url, stream=True)
        image_response.raise_for_status()
        image_data = Image.open(BytesIO(image_response.content))

        plt.figure(figsize=(10, 8)) 
  
        plot_title = f"NASA APOD: {apod_data.get('date')}"
        plt.title(plot_title, fontsize=14, fontweight='bold')
        
      
        plt.imshow(image_data)
        
        plt.axis('off') 
        
        print("-" * 50)
        print("Displaying image...")
        plt.show() 

    except requests.exceptions.RequestException as e:
        print(f"\nA request error occurred: {e}", file=sys.stderr)
        if '404' in str(e):
            print("Hint: A 404 error might mean no APOD exists for the specified date.")
        elif '403' in str(e):
            print("Hint: A 403 error often means your API key is invalid or your rate limit is exceeded.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    
    display_apod_image()
