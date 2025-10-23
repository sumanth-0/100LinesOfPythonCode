import requests
from PIL import Image
from io import BytesIO
import json

image_url=".mp4"

url = "https://random.dog/woof.json"
# sometimes gives an mp4 file and the api is non configurable hence manual check to avoid the issue
while(image_url.endswith('.mp4')):
    response = requests.get(url)
    data = json.loads(response.content.decode())
    image_url = data["url"]

img_response = requests.get(image_url)

img = Image.open(BytesIO(img_response.content))

img.show()
