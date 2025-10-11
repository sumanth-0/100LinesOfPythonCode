#!/usr/bin/env python3
"""
Eco-Friendly Tip of the Day
Displays random eco-friendly tips to help users make environmentally conscious choices.
"""

import random
import sys

# List of eco-friendly tips
ECO_TIPS = [
    "🌱 Use reusable shopping bags instead of plastic bags.",
    "💡 Switch to LED bulbs - they use 75% less energy than incandescent bulbs.",
    "🚰 Turn off the tap while brushing your teeth to save up to 8 gallons of water per day.",
    "🚴 Bike or walk for short trips instead of driving.",
    "♻️ Recycle paper, plastic, glass, and metal products.",
    "🌳 Plant a tree - it absorbs CO2 and provides oxygen.",
    "🥤 Use a reusable water bottle instead of buying bottled water.",
    "🔌 Unplug electronics when not in use to prevent phantom energy drain.",
    "🚿 Take shorter showers to conserve water.",
    "🍃 Compost food scraps to reduce waste and create nutrient-rich soil.",
    "📱 Buy refurbished or second-hand electronics instead of new ones.",
    "👕 Donate or repurpose old clothes instead of throwing them away.",
    "🌡️ Lower your thermostat by 2 degrees in winter to save energy.",
    "🛒 Buy local and seasonal produce to reduce transportation emissions.",
    "📄 Go paperless - opt for digital bills and statements.",
    "🍽️ Reduce food waste by planning meals and storing food properly.",
    "🧴 Choose products with minimal or recyclable packaging.",
    "🌊 Use eco-friendly cleaning products to protect water systems.",
    "☀️ Hang clothes to dry instead of using a dryer when possible.",
    "🚗 Carpool with coworkers or friends to reduce emissions.",
    "🏡 Insulate your home to reduce heating and cooling costs.",
    "🌿 Start a small herb or vegetable garden.",
    "💻 Enable power-saving mode on your devices.",
    "🎁 Use reusable gift wrap or fabric bags for presents.",
    "🔋 Use rechargeable batteries instead of disposable ones."
]

def display_tip():
    """Display a random eco-friendly tip."""
    tip = random.choice(ECO_TIPS)
    print("\n" + "="*60)
    print("🌍 ECO-FRIENDLY TIP OF THE DAY 🌍")
    print("="*60)
    print(f"\n{tip}\n")
    print("="*60 + "\n")

def main():
    """Main function to run the Eco-Friendly Tip CLI."""
    print("\nWelcome to Eco-Friendly Tip of the Day!")
    print("Help the planet one tip at a time! 🌎\n")
    
    while True:
        display_tip()
        
        print("Options:")
        print("  [1] Show another tip")
        print("  [2] Exit")
        
        choice = input("\nEnter your choice (1 or 2): ").strip()
        
        if choice == '1':
            continue
        elif choice == '2':
            print("\n🌿 Thank you for caring about our planet! Goodbye! 🌿\n")
            sys.exit(0)
        else:
            print("\n⚠️  Invalid choice. Please enter 1 or 2.\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n🌿 Thank you for caring about our planet! Goodbye! 🌿\n")
        sys.exit(0)
