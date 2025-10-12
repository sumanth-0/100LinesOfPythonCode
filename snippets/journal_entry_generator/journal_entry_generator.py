#!/usr/bin/env python3
"""
Personal Journal Entry Generator
Generates daily writing prompts to help users reflect on their day.

Author: Contributing to 100LinesOfPythonCode
Issue: #768
"""

import random
from datetime import datetime
import json
import os

# Collection of thoughtful journal prompts organized by category
PROMPTS = {
    "gratitude": [
        "What are three things you're grateful for today?",
        "Who made a positive impact on your day and why?",
        "What simple pleasure brought you joy today?",
    ],
    "reflection": [
        "What was the most challenging moment today and how did you handle it?",
        "What did you learn about yourself today?",
        "How did you grow or improve today?",
    ],
    "goals": [
        "What progress did you make toward your goals today?",
        "What's one thing you want to accomplish tomorrow?",
        "What obstacle can you plan to overcome this week?",
    ],
    "creativity": [
        "If today were a movie, what would be its title and genre?",
        "Describe your day using only metaphors.",
        "What would your future self thank you for doing today?",
    ],
    "mindfulness": [
        "What emotions did you experience most strongly today?",
        "What moment today deserves to be remembered?",
        "How did you take care of yourself today?",
    ]
}

def get_daily_prompt(category=None):
    """Generate a random prompt, optionally from a specific category."""
    if category and category in PROMPTS:
        return random.choice(PROMPTS[category])
    # If no category specified, choose from all prompts
    all_prompts = [prompt for prompts in PROMPTS.values() for prompt in prompts]
    return random.choice(all_prompts)

def display_prompt_with_timestamp():
    """Display a prompt with the current date and time."""
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%I:%M %p")
    
    print(f"\n{'='*60}")
    print(f"Journal Entry - {date_str} at {time_str}")
    print(f"{'='*60}\n")
    
    # Select a random category and prompt
    category = random.choice(list(PROMPTS.keys()))
    prompt = get_daily_prompt(category)
    
    print(f"Category: {category.title()}")
    print(f"\nToday's Prompt:\n{prompt}\n")
    print(f"{'='*60}\n")

def save_entry(prompt, entry_text, filename="journal_entries.json"):
    """Save journal entry to a JSON file."""
    entry = {
        "timestamp": datetime.now().isoformat(),
        "prompt": prompt,
        "entry": entry_text
    }
    
    # Load existing entries if file exists
    entries = []
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            entries = json.load(f)
    
    entries.append(entry)
    
    with open(filename, 'w') as f:
        json.dump(entries, f, indent=2)
    
    print(f"Entry saved to {filename}")

if __name__ == "__main__":
    display_prompt_with_timestamp()
