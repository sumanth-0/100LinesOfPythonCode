#!/usr/bin/env python3
"""
Random Startup Idea Generator
Generates randomized startup ideas combining problems, audiences, and solutions.
"""

import random
import sys

# Lists of startup components
PROBLEMS = [
    "People waste too much time on",
    "It's hard to find reliable",
    "Small businesses struggle with",
    "Students can't afford",
    "Remote workers need better",
    "Elderly people have difficulty accessing",
    "Parents lack tools for",
    "Freelancers spend too much time on",
    "Travelers often face issues with",
    "Fitness enthusiasts need help with",
    "Pet owners struggle to manage",
    "Content creators waste time on",
    "Developers need better tools for",
    "Teams have poor visibility into",
    "People want to reduce their spending on"
]

AUDIENCES = [
    "busy professionals",
    "college students",
    "small business owners",
    "remote teams",
    "creative freelancers",
    "health-conscious millennials",
    "eco-friendly consumers",
    "tech-savvy parents",
    "senior citizens",
    "digital nomads",
    "fitness trainers",
    "content creators",
    "software developers",
    "restaurant owners",
    "real estate agents"
]

SOLUTIONS = [
    "an AI-powered mobile app",
    "a subscription-based platform",
    "a blockchain-enabled marketplace",
    "a peer-to-peer sharing network",
    "an automated SaaS tool",
    "a community-driven website",
    "a gamified learning platform",
    "a voice-activated assistant",
    "an AR/VR experience",
    "a data analytics dashboard",
    "a smart IoT device",
    "a social networking app",
    "a collaborative workspace tool",
    "a personalized recommendation engine",
    "a no-code automation platform"
]


def generate_idea():
    """Generate a single random startup idea."""
    problem = random.choice(PROBLEMS)
    audience = random.choice(AUDIENCES)
    solution = random.choice(SOLUTIONS)
    return f"{problem} for {audience} using {solution}."


def main():
    """Main function to run the startup idea generator."""
    print("\n🚀 Random Startup Idea Generator 🚀\n")
    print("="*50)
    
    # Check for command line argument for number of ideas
    num_ideas = 1
    if len(sys.argv) > 1:
        try:
            num_ideas = int(sys.argv[1])
            if num_ideas < 1 or num_ideas > 10:
                print("Please enter a number between 1 and 10.")
                return
        except ValueError:
            print("Invalid input. Please enter a number.")
            return
    
    for i in range(num_ideas):
        print(f"\nIdea #{i+1}:")
        print(generate_idea())
    
    print("\n" + "="*50)
    print("Good luck with your startup! 💡\n")


if __name__ == "__main__":
    main()
