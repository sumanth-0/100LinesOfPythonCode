
import json
from datetime import datetime

def generate_year_in_review(data):
    year_summary = {}
    total_events = 0
    
    for event in data:
        year = datetime.strptime(event['date'], '%Y-%m-%d').year
        if year not in year_summary:
            year_summary[year] = []
        year_summary[year].append(event)
        total_events += 1
    
    return year_summary, total_events

def display_summary(year_summary, total_events):
    for year, events in year_summary.items():
        print(f"\nYear: {year} - Total Events: {len(events)}")
        for event in events:
            print(f"  - {event['title']}: {event['description']}")

if __name__ == "__main__":
    input_file = input("Enter the path to your events JSON file: ")
    
    with open(input_file, 'r') as f:
        events_data = json.load(f)
    
    summary, total = generate_year_in_review(events_data)
    display_summary(summary, total)
