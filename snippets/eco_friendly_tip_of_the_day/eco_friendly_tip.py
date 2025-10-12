#!/usr/bin/env python3
"""
Eco-Friendly Tip of the Day
Displays random eco-friendly tips to promote environmental awareness.
"""

import random
import sys


class EcoFriendlyTips:
    """Manage and display eco-friendly tips."""
    
    def __init__(self):
        self.tips = [
            "💡 Switch to LED bulbs - they use 75% less energy than traditional bulbs!",
            "🚰 Fix leaky faucets - a drip per second wastes 3,000 gallons per year!",
            "🛍️ Bring reusable bags when shopping to reduce plastic waste.",
            "🔌 Unplug devices when not in use to save phantom energy consumption.",
            "🚲 Walk or bike for short trips instead of driving.",
            "♻️ Recycle paper, plastic, glass, and metal properly.",
            "🌡️ Lower your thermostat by 2°F in winter to save energy.",
            "💧 Take shorter showers to conserve water.",
            "🌱 Plant trees - one tree absorbs 48 lbs of CO2 per year!",
            "📦 Buy products with minimal packaging.",
            "🥗 Eat more plant-based meals to reduce your carbon footprint.",
            "🚿 Install low-flow showerheads to save water.",
            "☀️ Dry clothes on a line instead of using a dryer.",
            "🏠 Insulate your home properly to reduce heating/cooling needs.",
            "🔋 Use rechargeable batteries instead of disposable ones.",
            "🍴 Compost food scraps to reduce landfill waste.",
            "🎁 Give experiences instead of material gifts.",
            "📱 Buy refurbished electronics when possible.",
            "🧊 Keep your fridge at 37-40°F and freezer at 0-5°F for efficiency.",
            "🌊 Support ocean cleanup initiatives and reduce plastic use.",
            "🚗 Carpool or use public transportation when possible.",
            "💻 Print only when necessary and use both sides of paper.",
            "🌿 Use natural cleaning products instead of harsh chemicals.",
            "☕ Use a reusable coffee cup instead of disposable ones.",
            "🪟 Open windows for ventilation instead of AC when weather permits."
        ]
    
    def get_random_tip(self):
        """Return a random eco-friendly tip."""
        return random.choice(self.tips)
    
    def display_tip(self):
        """Display a random tip with formatting."""
        tip = self.get_random_tip()
        print("\n" + "="*60)
        print("🌍 ECO-FRIENDLY TIP OF THE DAY 🌍")
        print("="*60)
        print(f"\n{tip}\n")
        print("="*60)


def main():
    """Main function to run the eco-friendly tips program."""
    tips_manager = EcoFriendlyTips()
    
    print("\n🌿 Welcome to Eco-Friendly Tips! 🌿")
    print("Help save the planet, one tip at a time!\n")
    
    while True:
        tips_manager.display_tip()
        
        print("\nOptions:")
        print("  [N] - Show another tip")
        print("  [Q] - Quit")
        
        choice = input("\nYour choice: ").strip().upper()
        
        if choice == 'Q':
            print("\n🌍 Thank you for caring about our planet! 🌍")
            print("Remember: Small actions make a big difference!\n")
            sys.exit(0)
        elif choice == 'N':
            continue
        else:
            print("\n⚠️  Invalid choice. Please enter 'N' or 'Q'.")


if __name__ == "__main__":
    main()
