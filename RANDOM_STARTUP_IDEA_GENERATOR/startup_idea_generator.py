"""Random Startup Idea Generator - Combines tech buzzwords with industries"""
import random
import sys

TECH_BUZZWORDS = [
    "AI-powered", "Blockchain-based", "IoT-enabled", "Cloud-native",
    "Machine Learning", "AR/VR", "Quantum-ready", "5G-optimized",
    "Decentralized", "Smart", "Automated", "Predictive",
    "Neural network", "Edge computing", "Serverless", "Voice-activated",
    "Biometric", "Cryptocurrency", "NFT-based", "Metaverse",
    "Data-driven", "Algorithm-optimized", "Deep learning", "Robotic"
]

ACTIONS = [
    "platform", "assistant", "marketplace", "analyzer", "optimizer",
    "scheduler", "tracker", "planner", "finder", "manager",
    "advisor", "coach", "consultant", "curator", "aggregator",
    "predictor", "monitor", "detector", "recommender", "companion"
]

INDUSTRIES = [
    "construction", "fitness", "education", "healthcare", "finance",
    "real estate", "food delivery", "pet care", "fashion", "travel",
    "music", "art", "sports", "cooking", "banking",
    "productivity", "dating", "gaming", "sustainability", "agriculture",
    "interior design", "mental health", "childcare", "eldercare", "beauty"
]

TARGET_MARKETS = [
    "for urban homes", "for small businesses", "for freelancers",
    "for remote workers", "for students", "for seniors",
    "for millennials", "for parents", "for professionals",
    "for startups", "for enterprises", "for developers",
    "for creators", "for influencers", "for travelers",
    "for subscription-based models", "for Gen Z", "for busy professionals",
    "for sustainable living", "for minimalists", "for digital nomads"
]

def generate_idea(include_target=True):
    """Generate a random startup idea"""
    tech = random.choice(TECH_BUZZWORDS)
    industry = random.choice(INDUSTRIES)
    action = random.choice(ACTIONS)
    if include_target:
        target = random.choice(TARGET_MARKETS)
        return f"{tech} {industry} {action} {target}"
    return f"{tech} {industry} {action}"

def display_menu():
    """Display the main menu"""
    print("\n" + "="*60)
    print("🚀 RANDOM STARTUP IDEA GENERATOR 🚀".center(60))
    print("="*60)
    print("\n1. Generate a single startup idea")
    print("2. Generate a list of 10 ideas")
    print("3. Generate multiple ideas (up to 25)")
    print("4. Generate short-form ideas (without target market)")
    print("5. Exit")
    print("\n" + "-"*60)

def main():
    """Main program loop"""
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == "1":
            print("\n💡 Your Startup Idea:")
            print(f"   → {generate_idea()}")
        elif choice == "2":
            print("\n💡 Here are 10 startup ideas:\n")
            for i in range(10):
                print(f"{i+1:2d}. {generate_idea()}")
        elif choice == "3":
            try:
                num = int(input("\nHow many ideas? (1-25): ").strip())
                if 1 <= num <= 25:
                    print(f"\n💡 Here are {num} startup ideas:\n")
                    for i in range(num):
                        print(f"{i+1:2d}. {generate_idea()}")
                else:
                    print("❌ Please enter a number between 1 and 25.")
            except ValueError:
                print("❌ Invalid input. Please enter a number.")
        elif choice == "4":
            print("\n💡 Here are 5 short-form startup ideas:\n")
            for i in range(5):
                print(f"{i+1}. {generate_idea(include_target=False)}")
        elif choice == "5":
            print("\n✨ Thanks for using the Startup Idea Generator!")
            print("   Good luck with your next unicorn! 🦄\n")
            sys.exit(0)
        else:
            print("❌ Invalid choice. Please select 1-5.")

if __name__ == "__main__":
    main()
