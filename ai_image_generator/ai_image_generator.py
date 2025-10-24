import openai, requests, os
from io import BytesIO

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")  # or replace with "sk-XXXX"

def generate_image(prompt, size="256x256"):
    try:
        response = openai.Image.create(prompt=prompt, n=1, size=size)
        url = response['data'][0]['url']
        return url
    except Exception as e:
        print("Error:", e)
        return None

def download_image(url, filename="generated_image.png"):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(filename, "wb") as f:
                f.write(response.content)
            print(f"✅ Image saved as {filename}")
        else:
            print("Failed to download image")
    except Exception as e:
        print("Error downloading image:", e)

if __name__ == "__main__":
    print("🎨 AI Image Generator")
    prompt = input("Enter your image prompt: ")
    url = generate_image(prompt)
    if url:
        print("🖼️ Image URL:", url)
        save = input("Do you want to download it? (y/n): ").lower()
        if save=="y":
            download_image(url)
