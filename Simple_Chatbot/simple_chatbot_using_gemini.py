import streamlit as st
import google.generativeai as genai
from PIL import Image
import io

# Configure Google API key
genai.configure(api_key='AIzaSyByfPNLCfyz8g_KWU2_vrrLV32oFUFFT2A')

# Initialize Gemini model
model = genai.GenerativeModel('gemini-1.5-flash')

# Function to get response from Gemini model
def get_gemini_response(conversation_history, images):
    return model.generate_content(conversation_history + images).text

# Function to convert uploaded files to PIL Images
def convert_to_pil_images(uploaded_files):
    return [Image.open(io.BytesIO(file.getvalue())) for file in uploaded_files]

# Streamlit app
st.title("Multi-Image Context-Aware Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
if "images" not in st.session_state:
    st.session_state.images = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# File uploader for multiple images
uploaded_files = st.file_uploader("Choose images...", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

if uploaded_files:
    new_images = convert_to_pil_images(uploaded_files)
    st.session_state.images.extend(new_images)
    
    # Display newly uploaded images
    st.image(new_images, caption=[f"Image {i+1}" for i in range(len(new_images))])

# Chat input
if prompt := st.chat_input("You:"):
    st.chat_message("user").markdown(prompt)
    
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    conversation_history = [
        f"{msg['role']}: {msg['content']}" for msg in st.session_state.messages
    ]
    
    response = get_gemini_response(conversation_history, st.session_state.images)
    
    with st.chat_message("assistant"):
        st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})

# Clear images button
if st.button("Clear Images"):
    st.session_state.images = []
    st.success("All images have been cleared.")
