import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()


api_key = os.getenv("open_router_api_key")

def get_history():
    with open("memory.txt", "r") as file:
        memory_content = file.read()
    return memory_content

def chatbot_response(query,history):
    response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
        "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
    },
    data=json.dumps({
        "model": "mistralai/mistral-small-3.2-24b-instruct:free",
        "messages": [
        {
            "role": "user",
            "content": [
            {
                "type": "text",
                "text": f"{history}+{user_input}"
            },
            
            ]
        }
        ],
        
    })
    )
    result = response.json()

    return result['choices'][0]['message']['content']
def clean_memory():
    with open("memory.txt", "w") as file:
        file.write("")
if __name__ == "__main__":
    try:
        while True:
            print(" Enter Query : ")
            user_input = input()
            if user_input=="exit":
                clean_memory()
            history = get_history()
            response = chatbot_response(user_input,history)
            print("AI: ", response)
            history += f"\nUser: {user_input}\nAI:{response}"
            clean_memory()
            with open("memory.txt", "a") as file:
                file.write(history)
    except KeyboardInterrupt:
        clean_memory()
        print("\nExiting... Memory cleared.")