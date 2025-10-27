import re

def score_subject_line(subject):
    POWER_WORDS = {
    # Evokes urgency, fear of missing out (FOMO), and immediate action.
    "URGENCY_SCARCITY": [
        "Urgent", "Important", "Alert", "Breaking", "Now", "Today", "Limited",
        "Final", "Last chance", "Deadline", "Expires", "Hurry", "Ending soon",
        "Immediately", "Critical", "Instantly", "Few spots", "One-time", "Rush"
    ],
    
    # Piques curiosity, suggests exclusive information, and creates an information gap.
    "CURIOSITY_INTRIGUE": [
        "Secret", "Discover", "Unveiled", "Shocking", "Exposed", "Forbidden", 
        "Hack", "Hidden", "Confidential", "Bizarre", "Unusual", "Mystery", 
        "Spoiler", "Revealed", "Controversial", "Untold", "Sneak peek"
    ],
    
    # Focuses on value, money, and personal gain.
    "VALUE_GAIN": [
        "Free", "Save", "Bonus", "Gift", "Offer", "Win", "Profit", "Increase", 
        "Guaranteed", "Ultimate", "Massive", "Exclusive", "Premium", "New", 
        "Bargain", "Revenue", "Multiply", "Lifetime", "Worth"
    ],
    
    # Appeals to ease, convenience, and low effort.
    "SIMPLICITY_EASE": [
        "Easy", "Simple", "Quick", "Effortless", "Painless", "Simple-steps", 
        "Fast", "Proven", "Blueprint", "Cheat Sheet", "Template", "No-risk", 
        "Foolproof", "Simple-hack"
    ],
    
    # Strong action verbs that encourage clicking and reading.
    "ACTION_VERBS": [
        "Get", "Grab", "Stop", "Start", "Download", "Crush", "Transform", 
        "Unleash", "Dominate", "Conquer", "Fix", "Solve", "Learn", "Explore", 
        "Boost", "Accelerate", "Master", "Achieve", "Take"
    ],
    
    # Words that build trust, credibility, and authority.
    "TRUST_CREDIBILITY": [
        "Proven", "Guaranteed", "Trusted", "Certified", "Official", "Expert", 
        "Backed", "Tested", "Results", "Science", "Authentic", "Reliable",
        "Case Study", "Evidence"
    ],
    
    # Words that evoke strong positive or negative emotional responses.
    "EMOTION_QUALITY": [
        "Amazing", "Best", "Remarkable", "Fantastic", "Incredible", "Mistake", 
        "Warning", "Awe", "Exciting", "Jaw-dropping", "Inspiring", "Worse",
        "Horror", "Pain", "Vibrant", "Wonderful"
    ]
}
    
    all_power_words = set()
    for category_list in POWER_WORDS.values():
        for word in category_list:
            all_power_words.add(word.lower())
     
    subject_cleaned = re.sub(r'[^\w\s]', '', subject.lower())
    words = subject_cleaned.split()

    matches = [word for word in words if word in all_power_words]
    score = len(matches)

    total_words = len(words)
    percentage = round((score / total_words) * 100, 2) if total_words > 0 else 0

    print("\nSubject Line Analysis:")
    print(f"Subject: {subject}")
    print(f"Power Words Found: {matches}")
    print(f"Score: {score} / {total_words} words ({percentage}%)")

   
    if score == 0:
        print(" Suggestion: Try adding strong words like 'exclusive', 'free', or 'limited'.")
    elif percentage < 20:
        print(" Suggestion: Add one or two more emotional or action-oriented words.")
    else:
        print("Great job! This subject line is already engaging!")


if __name__ == "__main__":
    subject_line = input("Enter your email subject line: ")
    score_subject_line(subject_line)