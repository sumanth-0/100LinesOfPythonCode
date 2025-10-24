import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# Load your OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_hashtags(caption, max_hashtags=10):
    """
    Generate hashtags for a given social media caption.
    
    Args:
        caption (str): The social media caption.
        max_hashtags (int): Maximum number of hashtags to generate.
    
    Returns:
        List[str]: A list of hashtags without emojis.
    """
    prompt = f"Generate {max_hashtags} relevant hashtags for the following caption. Do not include emojis:\n\n'{caption}'"

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini-2024-07-18",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that generates relevant hashtags without emojis."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,
        temperature=0.7
    )

    hashtags_text = response.choices[0].message['content']
    # Split hashtags by space or comma
    hashtags = [tag.strip() for tag in hashtags_text.replace(',', ' ').split() if tag.startswith("#")]
    
    return hashtags

if __name__ == "__main__":
    caption = input("Enter your social media caption: ")
    hashtags = generate_hashtags(caption)
    print("Generated Hashtags:", hashtags)
