import streamlit as st
from transformers import pipeline
import random

# Initialize the text generation model
# Using distilgpt2 for a balance between performance and quality
comment_gen = pipeline("text-generation", model="distilgpt2")

# --- UI Setup ---
st.set_page_config(layout="wide")
st.title("😂 Fake Funny Comment Generator 😂")
st.markdown("Describe the post, image, or video content, and the AI will try to generate a funny comment!")

# --- Input Area ---
content_description = st.text_area(
    "Describe the content here (e.g., 'A cat trying to fit into a tiny box', 'Someone slipping on a banana peel', 'My terrible attempt at cooking'):",
    height=100
)

# --- Generation Controls ---
col1, col2 = st.columns([1, 3])
with col1:
    num_comments = st.slider("Number of comments to generate:", 1, 5, 1)
    max_length = st.slider("Max comment length (words):", 10, 50, 25)

# --- Comment Generation ---
if st.button("Generate Funny Comments!"):
    if content_description:
        st.subheader("Generated Comments:")
        
        # Craft a prompt that encourages humor and relevance
        base_prompt = f"Here's a funny comment about \"{content_description}\":"

        # Generate comments
        with st.spinner("Thinking of something funny... 🤔"):
            try:
                # Generate multiple sequences based on the prompt
                generated_outputs = comment_gen(
                    base_prompt,
                    max_length=max_length + len(base_prompt.split()), # Adjust max_length based on prompt
                    num_return_sequences=num_comments,
                    temperature=0.85, # Increase temperature slightly for more creativity/randomness
                    do_sample=True,  # Ensure sampling is enabled for temperature to work
                    pad_token_id=comment_gen.model.config.eos_token_id # Suppress padding warning
                )
                
                # Process and display generated comments
                for i, output in enumerate(generated_outputs):
                    # Extract only the generated part after the prompt
                    comment_text = output['generated_text'].replace(base_prompt, "").strip()
                    
                    # Basic filtering for empty or too short comments
                    if len(comment_text.split()) > 2:
                        st.markdown(f"**Comment {i+1}:** {comment_text}")
                    else:
                         st.warning(f"Comment {i+1} was too short or empty, try generating again.")

            except Exception as e:
                st.error(f"An error occurred during generation: {e}")
                st.info("Maybe try a slightly different description or adjust the length?")

    else:
        st.warning("Please describe the content first!")

# --- Add some humor ---
st.sidebar.markdown("---")
st.sidebar.header("Why did the AI cross the road?")
st.sidebar.markdown("To optimize its pathfinding algorithm!")
st.sidebar.markdown("---")