# pip install instabot
import time
from instabot import Bot
from datetime import datetime, timedelta

def schedule_post(image_path, caption, post_time):
    while datetime.now() < post_time:
        time.sleep(10)  # Check every 10 seconds
    bot = Bot()
    bot.login(username='YOUR_USERNAME', password='YOUR_PASSWORD')
    bot.upload_photo(image_path, caption=caption)
    print(f"Posted: {image_path} with caption: '{caption}'")

if __name__ == "__main__":
    image_path = "path/to/your/image.jpg"
    caption = "Your caption here!"
    post_time = datetime.now() + timedelta(minutes=1)
    print(f"Scheduling post for {post_time}")
    schedule_post(image_path, caption, post_time)
