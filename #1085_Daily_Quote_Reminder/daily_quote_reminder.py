#!/usr/bin/env python3
"""
Daily Quote Reminder - A CLI tool to display motivational quotes at scheduled times
Issue #1085
"""

import random
import time
from datetime import datetime, timedelta
import argparse
import sys

QUOTES = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "It does not matter how slowly you go as long as you do not stop. - Confucius",
    "Everything you've ever wanted is on the other side of fear. - George Addair",
    "Believe in yourself. You are braver than you think. - Roy T. Bennett",
    "Success is not how high you have climbed, but how you make a positive difference. - Roy T. Bennett",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
    "The only impossible journey is the one you never begin. - Tony Robbins",
    "Start where you are. Use what you have. Do what you can. - Arthur Ashe",
    "Act as if what you do makes a difference. It does. - William James",
    "Success usually comes to those who are too busy to be looking for it. - Henry David Thoreau",
    "The way to get started is to quit talking and begin doing. - Walt Disney",
    "Don't be afraid to give up the good to go for the great. - John D. Rockefeller",
    "I find that the harder I work, the more luck I seem to have. - Thomas Jefferson",
    "If you are not willing to risk the usual, you will have to settle for the ordinary. - Jim Rohn",
    "Success is walking from failure to failure with no loss of enthusiasm. - Winston Churchill",
    "What lies behind us and what lies before us are tiny matters compared to what lies within us. - Ralph Waldo Emerson",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt"
]

def display_quote():
    """Display a random motivational quote"""
    quote = random.choice(QUOTES)
    print("\n" + "="*80)
    print("DAILY MOTIVATIONAL QUOTE")
    print("="*80)
    print(f"\n{quote}\n")
    print("="*80)
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*80 + "\n")

def schedule_reminder(interval_hours=24):
    """Schedule quote reminders at specified intervals"""
    print(f"\nDaily Quote Reminder started!")
    print(f"You'll receive a quote every {interval_hours} hour(s).")
    print(f"Press Ctrl+C to stop.\n")
    
    try:
        while True:
            display_quote()
            time.sleep(interval_hours * 3600)
    except KeyboardInterrupt:
        print("\n\nDaily Quote Reminder stopped. Have a great day!\n")
        sys.exit(0)

def schedule_at_time(target_time):
    """Schedule quote at a specific time daily"""
    print(f"\nDaily Quote Reminder set for {target_time} every day.")
    print(f"Press Ctrl+C to stop.\n")
    
    try:
        while True:
            now = datetime.now()
            target_hour, target_minute = map(int, target_time.split(':'))
            target_datetime = now.replace(hour=target_hour, minute=target_minute, second=0, microsecond=0)
            
            if target_datetime <= now:
                target_datetime += timedelta(days=1)
            
            wait_seconds = (target_datetime - now).total_seconds()
            print(f"Next quote at {target_datetime.strftime('%Y-%m-%d %H:%M:%S')}")
            time.sleep(wait_seconds)
            display_quote()
    except KeyboardInterrupt:
        print("\n\nDaily Quote Reminder stopped. Have a great day!\n")
        sys.exit(0)

def main():
    parser = argparse.ArgumentParser(description="Daily Quote Reminder - Get motivated!")
    parser.add_argument('--now', action='store_true', help='Display a quote immediately')
    parser.add_argument('--interval', type=float, default=24, help='Interval in hours between quotes (default: 24)')
    parser.add_argument('--time', type=str, help='Specific time to show quote daily (format: HH:MM, e.g., 09:00)')
    
    args = parser.parse_args()
    
    if args.now:
        display_quote()
    elif args.time:
        try:
            schedule_at_time(args.time)
        except ValueError:
            print("Error: Invalid time format. Use HH:MM (e.g., 09:00)")
            sys.exit(1)
    else:
        schedule_reminder(args.interval)

if __name__ == "__main__":
    main()
