import random
import json
import os
from datetime import datetime
from pathlib import Path

# File to store reflection history
HISTORY_FILE = "reflection_history.json"

# Comprehensive list of reflection prompts
REFLECTION_PROMPTS = [
    "What are three things you're grateful for today?",
    "What was the most challenging moment today, and how did you handle it?",
    "What did you learn about yourself today?",
    "How did you show kindness to yourself or others today?",
    "What could you have done differently today?",
    "What made you smile or laugh today?",
    "What are you looking forward to tomorrow?",
    "How did you step out of your comfort zone today?",
    "What accomplishment, big or small, are you proud of today?",
    "What emotion did you feel most strongly today, and why?",
    "How did you take care of your physical health today?",
    "What relationship in your life needs more attention?",
    "What fear did you face today, or what fear are you avoiding?",
    "How aligned were your actions today with your core values?",
    "What would you like to let go of from today?",
    "What energized you today?",
    "What drained your energy today?",
    "How did you practice self-compassion today?",
    "What conversation had the most impact on you today?",
    "What decision did you make today that you feel good about?",
    "How did you contribute to someone else's happiness today?",
    "What pattern or habit did you notice in yourself today?",
    "What would your future self thank you for doing today?",
    "How did you express your creativity today?",
    "What boundary did you set or need to set today?",
    "What are you avoiding thinking about right now?",
    "How did you show up authentically today?",
    "What aspect of your life needs more balance?",
    "What small victory should you celebrate today?",
    "How did you handle stress or pressure today?",
    "What would make tomorrow better than today?",
    "What limiting belief held you back today?",
    "How did you practice mindfulness or presence today?",
    "What are you curious about right now?",
    "How did you honor your needs today?",
    "What brought you peace today?",
    "What inner critic voice was loudest today?",
    "How did you practice gratitude beyond just thinking it?",
    "What risk did you take today, or wish you had taken?",
    "How did you invest in your personal growth today?"
]

def load_history():
    """Load reflection history from JSON file."""
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            return {}
    return {}

def save_history(history):
    """Save reflection history to JSON file."""
    with open(HISTORY_FILE, 'w') as file:
        json.dump(history, file, indent=4)

def get_daily_prompt():
    """Get today's reflection prompt."""
    history = load_history()
    today = datetime.now().strftime("%Y-%m-%d")
    
    # Check if we already have a prompt for today
    if today in history:
        return history[today]["prompt"], False
    
    # Get a new random prompt
    prompt = random.choice(REFLECTION_PROMPTS)
    return prompt, True

def save_reflection(prompt, reflection):
    """Save today's reflection."""
    history = load_history()
    today = datetime.now().strftime("%Y-%m-%d")
    
    history[today] = {
        "prompt": prompt,
        "reflection": reflection,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    save_history(history)

def display_past_reflections():
    """Display past reflections."""
    history = load_history()
    
    if not history:
        print("\nNo past reflections found.")
        return
    
    print("\n=== Past Reflections ===")
    for date in sorted(history.keys(), reverse=True)[:7]:  # Show last 7 days
        entry = history[date]
        print(f"\nDate: {date}")
        print(f"Prompt: {entry['prompt']}")
        print(f"Reflection: {entry['reflection']}")
        print("-" * 60)

def main():
    print("\n" + "=" * 60)
    print("   Daily Reflection Prompts")
    print("=" * 60)
    
    prompt, is_new = get_daily_prompt()
    
    if not is_new:
        print("\nYou've already received today's prompt!")
        print(f"\nToday's Prompt: {prompt}\n")
        
        choice = input("Would you like to view past reflections? (y/n): ").strip().lower()
        if choice == 'y':
            display_past_reflections()
    else:
        print(f"\nToday's Reflection Prompt:\n{prompt}\n")
        
        reflection = input("Your reflection (press Enter to skip): ").strip()
        
        if reflection:
            save_reflection(prompt, reflection)
            print("\nThank you for reflecting! Your thoughts have been saved.")
        else:
            save_reflection(prompt, "")
            print("\nPrompt saved. You can reflect on it anytime!")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
