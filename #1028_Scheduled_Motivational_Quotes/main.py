"""
Scheduled Motivational Quote Printer
Displays a random motivational quote at scheduled times throughout the day.
"""

import random
import time
from datetime import datetime, timedelta
import schedule


# Collection of motivational quotes
MOTIVATIONAL_QUOTES = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "It does not matter how slowly you go as long as you do not stop. - Confucius",
    "Everything you've ever wanted is on the other side of fear. - George Addair",
    "Success is not how high you have climbed, but how you make a positive difference to the world. - Roy T. Bennett",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
    "The only impossible journey is the one you never begin. - Tony Robbins",
    "In the middle of difficulty lies opportunity. - Albert Einstein",
    "What lies behind us and what lies before us are tiny matters compared to what lies within us. - Ralph Waldo Emerson",
    "The way to get started is to quit talking and begin doing. - Walt Disney",
    "Don't be afraid to give up the good to go for the great. - John D. Rockefeller",
    "I find that the harder I work, the more luck I seem to have. - Thomas Jefferson",
    "Success usually comes to those who are too busy to be looking for it. - Henry David Thoreau",
    "The road to success and the road to failure are almost exactly the same. - Colin R. Davis",
    "Don't let yesterday take up too much of today. - Will Rogers",
    "You learn more from failure than from success. Don't let it stop you. - Unknown",
    "It's not whether you get knocked down, it's whether you get up. - Vince Lombardi",
    "If you are working on something that you really care about, you don't have to be pushed. - Steve Jobs",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
    "The secret of success is to do the common thing uncommonly well. - John D. Rockefeller Jr.",
    "I never dreamed about success, I worked for it. - Estee Lauder",
    "Success seems to be connected with action. Successful people keep moving. - Conrad Hilton",
    "Don't be distracted by criticism. Remember--the only taste of success some people get is to take a bite out of you. - Zig Ziglar"
]


def display_quote():
    """
    Select and display a random motivational quote with formatting.
    """
    quote = random.choice(MOTIVATIONAL_QUOTES)
    current_time = datetime.now().strftime("%H:%M:%S")
    
    print("\n" + "=" * 80)
    print(f"⏰ TIME: {current_time}")
    print("=" * 80)
    print(f"\n💡 {quote}\n")
    print("=" * 80 + "\n")


def schedule_quotes(times_list):
    """
    Schedule quotes to be displayed at specific times.
    
    Args:
        times_list: List of time strings in HH:MM format (24-hour)
    """
    for time_str in times_list:
        schedule.every().day.at(time_str).do(display_quote)
        print(f"✅ Quote scheduled for {time_str}")


def run_scheduler():
    """
    Run the scheduler continuously and check for pending jobs.
    """
    print("\n🚀 Motivational Quote Scheduler is running...")
    print("Press Ctrl+C to stop\n")
    
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\n👋 Scheduler stopped. Have a great day!")


def main():
    """
    Main function to set up and run the scheduled motivational quote system.
    """
    print("\n" + "=" * 80)
    print("💪 SCHEDULED MOTIVATIONAL QUOTE PRINTER")
    print("=" * 80 + "\n")
    
    # Option to choose mode
    print("Choose your mode:")
    print("1. Use default schedule (9:00 AM, 12:00 PM, 3:00 PM, 6:00 PM)")
    print("2. Set custom times")
    print("3. Show quote now and exit")
    print("4. Continuous mode (quote every X minutes)")
    
    choice = input("\nEnter your choice (1-4): ").strip()
    
    if choice == "1":
        # Default schedule
        default_times = ["09:00", "12:00", "15:00", "18:00"]
        print("\n📅 Using default schedule:")
        schedule_quotes(default_times)
        run_scheduler()
        
    elif choice == "2":
        # Custom schedule
        print("\nEnter times in HH:MM format (24-hour). Type 'done' when finished.")
        custom_times = []
        while True:
            time_input = input("Enter time (or 'done'): ").strip()
            if time_input.lower() == 'done':
                break
            try:
                # Validate time format
                datetime.strptime(time_input, "%H:%M")
                custom_times.append(time_input)
            except ValueError:
                print("Invalid time format. Please use HH:MM (e.g., 09:30)")
        
        if custom_times:
            print("\n📅 Custom schedule:")
            schedule_quotes(custom_times)
            run_scheduler()
        else:
            print("No times scheduled. Exiting...")
            
    elif choice == "3":
        # Show quote immediately
        display_quote()
        
    elif choice == "4":
        # Continuous mode
        try:
            interval = int(input("\nEnter interval in minutes: ").strip())
            if interval > 0:
                print(f"\n🔄 Quote will be displayed every {interval} minute(s)")
                schedule.every(interval).minutes.do(display_quote)
                display_quote()  # Show one immediately
                run_scheduler()
            else:
                print("Invalid interval. Must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("Invalid choice. Exiting...")


if __name__ == "__main__":
    main()
