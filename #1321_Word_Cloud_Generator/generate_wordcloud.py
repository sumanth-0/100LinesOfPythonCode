import matplotlib.pyplot as plt # For displaying the image
from wordcloud import WordCloud, STOPWORDS # For generating the word cloud
import os # For path handling if saving image

# --- Configuration ---
# Name of the output image file
OUTPUT_IMAGE_FILENAME = "wordcloud_output.png"
# Text to generate the word cloud from (you can change this or get input)
DEFAULT_TEXT = """
Word clouds are visual representations of text data. They are commonly used to 
depict keyword metadata on websites, or to visualize the free form text. 
Tags are usually single words, and the importance of each tag is shown 
with font size or color. This format is useful for quickly perceiving 
the most prominent terms and for quickly locating a term.
"""

# --- Core Word Cloud Generation Function ---

def generate_word_cloud(text_input: str, output_filename: str = OUTPUT_IMAGE_FILENAME):
    """
    Generates a word cloud image from the given text and saves it.
    
    Args:
        text_input: The string content to create the word cloud from.
        output_filename: The name of the file to save the word cloud image.
    """
    
    # Combine default stop words with any custom words you want to ignore
    # Stopwords are common words (like 'the', 'is', 'a') that don't add meaning
    custom_stopwords = set(STOPWORDS)
    custom_stopwords.update(["word", "cloud", "text", "data", "use", "using", "can"]) # Add common words from example

    print(f"Generating word cloud from input text...")
    
    # Create a WordCloud object
    wordcloud = WordCloud(
        width=800,              # Width of the generated image
        height=400,             # Height of the generated image
        background_color="white", # Background color of the image
        stopwords=custom_stopwords, # Words to ignore
        min_font_size=10,       # Minimum font size for words
        max_words=100           # Maximum number of words to display
    ).generate(text_input) # Generate the word cloud from the provided text

    # Display the generated image:
    plt.figure(figsize=(10, 5)) # Set figure size for display
    plt.imshow(wordcloud, interpolation='bilinear') # Display the word cloud
    plt.axis("off") # Remove axes for a clean image
    plt.title("Generated Word Cloud")
    plt.show() # Show the plot

    # Save the generated image to a file
    try:
        wordcloud.to_file(output_filename)
        print(f"Word cloud image saved as '{output_filename}' in the current directory.")
    except Exception as e:
        print(f"Error saving image: {e}")

# --- Execution ---

if __name__ == "__main__":
    
    print("\n--- Word Cloud Generator ---\n")
    
    # You can get input from the user, or use the default text
    user_input = input("Enter text for the word cloud (press Enter to use default text): \n")
    
    if user_input.strip(): # Check if user input is not just whitespace
        generate_word_cloud(user_input)
    else:
        generate_word_cloud(DEFAULT_TEXT)
        
    print("\n------------------------------\n")