import random

# Funny comment templates with placeholders for topic
templates = [
    "This is why {topic} should be illegal. Too much {topic} leads to bad decisions... like watching this again.",
    "If {topic} was a superpower, I'd be unstoppable. But alas, I'm just here for the {topic} vibes.",
    "Plot twist: the real {topic} was the friends we made along the way. Nah, it's just this video.",
    "Me: 'I'll just watch this once.' Also me: rewatching for the 47th time. {topic} has me hooked.",
    "{topic}? More like {topic_upper} of the century! (Sorry, had to.)",
    "This {topic} energy is what I need to get through Monday. Or any day, really.",
    "Who hurt you to make this {topic} masterpiece? Asking for a friend who needs therapy.",
    "10/10 would recommend. Now excuse me while I practice my {topic} moves in the mirror.",
    "If I had a dollar for every time this {topic} made me laugh, I'd buy more {topic}.",
    "This is peak {topic}. Humanity peaked here. We're all downhill from now.",
    "Pro tip: Pair this with {topic} snacks for maximum chaos. You're welcome.",
    "I came for the {topic}, stayed for the existential crisis. 5 stars.",
    "{topic} just solved world hunger... by making me too busy laughing to eat.",
    "Bold of you to assume I won't share this with my mom. {topic} family bonding incoming.",
    "This {topic} hits different after 2am. Or 2pm. Or whenever."
]

def generate_comments(topic, num_comments=5):
    """Generate fake funny comments based on a topic."""
    comments = []
    for _ in range(num_comments):
        template = random.choice(templates)
        comment = template.format(topic=topic.lower(), topic_upper=topic.upper())
        comments.append(comment)
    return comments

def main():
    print("Fake Funny Comments Generator")
    topic = input("Enter video/post topic (e.g., 'cat dancing'): ").strip()
    if not topic:
        topic = "random stuff"
    
    try:
        num = int(input("Number of comments (default 5): ").strip() or "5")
    except ValueError:
        num = 5
    
    comments = generate_comments(topic, num)
    print(f"\nGenerated comments for '{topic}':\n")
    for i, comment in enumerate(comments, 1):
        print(f"{i}. {comment}")
        print()

if __name__ == "__main__":
    main()
