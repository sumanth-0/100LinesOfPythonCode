# --------------------------------------------
# LLM Joke Classifier: pun / dark / dad joke
# --------------------------------------------
# Uses OpenAI's GPT model to classify jokes
# into three categories.
# --------------------------------------------

from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(api_key="YOUR_API_KEY_HERE")

def classify_joke_llm(joke: str) -> str:
    """
    Classify a joke as 'pun', 'dark', or 'dad joke'
    using a large language model (LLM).

    Args:
        joke (str): The joke text.

    Returns:
        str: One of 'pun', 'dark', or 'dad joke'.
    """

    prompt = f"""
    Classify the following joke as one of: "pun", "dark", or "dad joke".
    Return only the category name.

    Joke: "{joke}"
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",  # lightweight, fast model
        messages=[{"role": "user", "content": prompt}],
        temperature=0  # deterministic output
    )

    # Extract the model’s text output and clean it
    category = response.choices[0].message.content.strip().lower()

    return category


# --- Example Usage ---
if __name__ == "__main__":
    jokes = [
        "I used to be a banker but I lost interest.",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "I told my friend I saw a man drowning, and he said 'oh no, did you film it?'",
        "I made a pun about the wind but it blows."
    ]

    for joke in jokes:
        category = classify_joke_llm(joke)
        print(f"Joke: {joke}\n→ Category: {category}\n")
