import openai
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()
# GET API key
openai.api_key = os.getenv("API_KEY")
if not openai.api_key:
    print("API Key is not set up correctly.")


# Initialize GPT model
def get_gpt4_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=prompt
    )
    return response['choices'][0]['message']['content']


st.title("Travel Guide Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Ask me about your travel destination...")

# Append user message to chat history
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    current_prompt = [{"role": "user", "content": user_input}]
    response = get_gpt4_response(current_prompt)
    st.session_state.messages.append(
        {"role": "assistant", "content": response})

# Show chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.write(f"**You:** {msg['content']}")
    else:
        st.write(f"**Travel Guide Bot:** {msg['content']}")
