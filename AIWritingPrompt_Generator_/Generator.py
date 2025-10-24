import random
import streamlit as st
from transformers import pipeline
from faker import Faker

# --- Initialize AI model and Faker ---
story_gen = pipeline("text-generation", model="distilgpt2")
fake = Faker()

# --- Story Element Sources ---

# Source 1: Curated Lists (Original)
def get_curated_elements():
    return {
        "characters": [
            "a grizzled star-captain with a robotic arm",
            "a young sorceress who talks to ghosts",
            "a cyborg detective haunted by his last case",
            "a dimension-hopping librarian on the run",
            "a rogue android fighting for equal rights",
            "a time-traveling historian trying to fix the past",
            "a chef who can cook emotions into her food",
            "a dream-weaver who sells memories",
        ],
        "settings": [
            "in a city powered by captured lightning",
            "on a colony ship lost in deep space",
            "in a magical library with books that read you back",
            "during a masquerade ball on a floating island",
            "in a virtual reality where the code is sentient",
            "on a desert planet with two suns",
            "in a steampunk city run by clockwork automatons",
            "in an underwater kingdom on the brink of war",
        ],
        "conflicts": [
            "must deliver a forbidden message",
            "is hunted by a relentless temporal paradox",
            "must win a high-stakes cosmic race",
            "is possessed by a mischievous ancient spirit",
            "has to reverse a magical curse before it's too late",
            "must expose a conspiracy that goes to the top",
            "is tasked with protecting the last of a species",
            "must find a legendary artifact to save their world",
        ]
    }

# Source 2: Simulated Database
def get_database_elements():
    """
    In a real application, this function would connect to your database
    (e.g., PostgreSQL, MongoDB) and fetch the elements.
    For this example, we'll just return a different set of lists.
    """
    return {
        "characters": [
            "a genetically-engineered musician",
            "a retired god of mischief",
            "an art thief who steals memories",
            "a lighthouse keeper on a forgotten world",
        ],
        "settings": [
            "in a city built on the back of a giant creature",
            "on a space station orbiting a black hole",
            "in a world where everyone's dreams are connected",
            "during a solar flare that grants temporary superpowers",
        ],
        "conflicts": [
            "must find a cure for a magical plague",
            "is framed for a crime they didn't commit",
            "must outsmart a sentient computer virus",
            "has to unite warring factions before an alien invasion",
        ]
    }

# Source 3: Randomly Generated with Faker
def get_random_elements():
    """
    Uses the Faker library to generate completely random story elements.
    """
    return {
        "characters": [
            f"a {fake.job()} who secretly {fake.bs()}",
            f"a {fake.color_name()} {fake.word()} with a hidden past",
            f"an android who believes they are {fake.name()}",
            f"a talking {fake.animal()} on a quest for {fake.word()}",
        ],
        "settings": [
            f"in a futuristic {fake.city()}",
            f"on a planet made of {fake.word()}",
            f"inside a massive, abandoned {fake.company()} building",
            f"during a festival celebrating the {fake.word()} of {fake.color_name()}",
        ],
        "conflicts": [
            f"must find the lost {fake.word()} of {fake.name()}",
            f"has to escape from a {fake.catch_phrase()}",
            f"needs to prevent a {fake.word()} from destroying the world",
            f"must solve the mystery of the disappearing {fake.color_name()} {fake.word()}",
        ]
    }

# --- Helper Functions ---

def generate_prompt(elements):
    """Generates a random story prompt from the given elements."""
    char = random.choice(elements["characters"])
    set_ = random.choice(elements["settings"])
    conflict = random.choice(elements["conflicts"])
    return f"Tell a story about {char} {set_} who {conflict}."

# (The rest of the helper functions remain the same as the previous version)
def generate_story_start(prompt):
    """Generates the beginning of the story."""
    return story_gen(prompt, max_length=150, num_return_sequences=1)[0]['generated_text']

def generate_choices(story_text):
    """Generates three choices for story continuation."""
    prompts = [
        f"{story_text} What happens next is that",
        f"{story_text} Suddenly, everything changed when",
        f"{story_text} The next thing they knew,"
    ]
    choices = story_gen(prompts, max_length=len(story_text.split()) + 50, num_return_sequences=1)
    return [choice[0]['generated_text'].replace(story_text, "").strip() for choice in choices]

def continue_story(story_text, user_input):
    """Continues the story with user's choice or input."""
    continuation_prompt = f"{story_text} {user_input}"
    return story_gen(continuation_prompt, max_length=len(continuation_prompt.split()) + 200, num_return_sequences=1)[0]['generated_text']


# --- UI ---

st.set_page_config(layout="wide")
st.title("Next-Level AI Story Generator")

# Initialize session state
if 'story' not in st.session_state:
    st.session_state.story = ""
if 'prompt' not in st.session_state:
    st.session_state.prompt = ""
if 'choices' not in st.session_state:
    st.session_state.choices = []

# --- Sidebar Controls ---

with st.sidebar:
    st.header("Story Controls")
    user_name = st.text_input("Enter your name:", "Author")

    source_option = st.selectbox(
        "Choose story element source:",
        ("Curated Lists", "Database", "Randomly Generated")
    )

    if st.button("Start New Story"):
        if source_option == "Curated Lists":
            elements = get_curated_elements()
        elif source_option == "Database":
            elements = get_database_elements()
        else:
            elements = get_random_elements()

        st.session_state.prompt = generate_prompt(elements)
        st.session_state.story = generate_story_start(st.session_state.prompt)
        st.session_state.choices = generate_choices(st.session_state.story)

    if st.session_state.story:
        if st.button("Restart Story"):
            st.session_state.story = ""
            st.session_state.prompt = ""
            st.session_state.choices = []
            st.experimental_rerun()

# --- Main Story Area ---

if not st.session_state.story:
    st.info("Click 'Start New Story' in the sidebar to begin.")
else:
    st.write(f"**Initial Idea by {user_name}:** {st.session_state.prompt}")
    st.markdown("---")
    st.write(st.session_state.story)

    st.markdown("---")
    st.subheader("What Happens Next?")

    # Display choices
    for i, choice in enumerate(st.session_state.choices):
        if st.button(choice, key=f"choice_{i}"):
            st.session_state.story = continue_story(st.session_state.story, choice)
            st.session_state.choices = generate_choices(st.session_state.story)
            st.experimental_rerun()

    with st.expander("Write your own continuation"):
        user_twist = st.text_area("Add your twist or next scene direction:", key="user_twist")
        if st.button("Continue with my twist"):
            st.session_state.story = continue_story(st.session_state.story, user_twist)
            st.session_state.choices = generate_choices(st.session_state.story)
            st.experimental_rerun()