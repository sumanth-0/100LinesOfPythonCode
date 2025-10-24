#!/usr/bin/env python3

"""
journal_prompt.py

Displays a random journaling question for self-reflection.
Part of the 100LinesOfPythonCode project.
"""

import random
import textwrap

# A list of self-reflection questions
JOURNAL_PROMPTS = [
    "What was the best part of your day today, and why?",
    "What is one thing you're grateful for right now?",
    "Describe a challenge you faced today and how you handled it.",
    "What is a skill you'd like to learn or improve, and why?",
    "If you could give one piece of advice to your younger self, what would it be?",
    "What are three things that made you smile today?",
    "Describe a place where you feel completely at peace.",
    "What is one thing you can do tomorrow to make it a great day?",
    "Write about a recent accomplishment you're proud of.",
    "What does 'success' mean to you, and how do you measure it?",
    "What is a fear you'd like to overcome?",
    "Who is someone who inspires you, and what qualities do you admire in them?",
    "What new thing did you learn today?",
    "Describe a simple pleasure you enjoyed recently.",
    "What is one of your core values, and how did you live by it today?"
]


def get_random_prompt(prompts: list) -> str:
    """Selects a single random prompt from the provided list."""
    return random.choice(prompts)


def display_prompt(prompt: str):
    """
    Prints the prompt to the console with formatted wrapping
    for readability.
    """
    print("\n" + "=" * 50)
    print("  Your Daily Journaling Prompt")
    print("=" * 50 + "\n")
    
    # Wrap text for readability in the terminal
    wrapper = textwrap.TextWrapper(
        width=70, 
        initial_indent="  ", 
        subsequent_indent="  "
    )
    print(wrapper.fill(prompt))
    
    print("\n" + "=" * 50 + "\n")


def main():
    """Main function to get and display the prompt."""
    prompt = get_random_prompt(JOURNAL_PROMPTS)
    display_prompt(prompt)


if __name__ == "__main__":
    main()