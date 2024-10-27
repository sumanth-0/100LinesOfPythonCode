import random

class HoroscopeGenerator:
    def __init__(self):
        self.horoscopes = {
            "Aries": "Today is a day of new beginnings. Take the leap!",
            "Taurus": "Patience is a virtue. Good things come to those who wait.",
            "Gemini": "Communication is key today. Reach out to someone you haven't talked to in a while.",
            "Cancer": "Focus on your home and family. They need your attention.",
            "Leo": "Your charisma will shine bright today. Embrace it!",
            "Virgo": "Organize your thoughts. Clarity will come from a clear mind.",
            "Libra": "Balance is essential. Find harmony in your relationships.",
            "Scorpio": "Trust your instincts. They will guide you well today.",
            "Sagittarius": "Adventure awaits you. Be open to new experiences.",
            "Capricorn": "Hard work will pay off. Stay focused on your goals.",
            "Aquarius": "Innovative ideas will come to you. Embrace your creativity.",
            "Pisces": "Emotional connections are strong today. Nurture them."
        }

    def get_daily_horoscope(self, sign):
        return self.horoscopes.get(sign, "Unknown sign. Please enter a valid zodiac sign.")

def main():
    zodiac_sign = input("Enter your zodiac sign: ").strip().capitalize()
    horoscope_generator = HoroscopeGenerator()
    horoscope = horoscope_generator.get_daily_horoscope(zodiac_sign)
    print(f"Today's Horoscope for {zodiac_sign}: {horoscope}")

if __name__ == "__main__":
    main()
