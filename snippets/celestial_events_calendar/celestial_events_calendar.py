#!/usr/bin/env python3
"""
Celestial Events Calendar
Displays upcoming celestial events from a static dataset
Created for issue #618
"""

from datetime import datetime, timedelta

def get_celestial_events():
    """Returns a list of celestial events with dates and details"""
    events = [
        {"date": "2025-10-25", "type": "Eclipse", "name": "Partial Solar Eclipse", 
         "description": "Visible in North America", "visibility": "Regional"},
        {"date": "2025-11-17", "type": "Meteor Shower", "name": "Leonids Meteor Shower", 
         "description": "Peak viewing after midnight", "visibility": "Global"},
        {"date": "2025-12-15", "type": "Meteor Shower", "name": "Geminids Meteor Shower", 
         "description": "Best meteor shower of the year", "visibility": "Global"},
        {"date": "2026-01-04", "type": "Meteor Shower", "name": "Quadrantids Meteor Shower", 
         "description": "Active from late December to mid-January", "visibility": "Northern Hemisphere"},
        {"date": "2026-02-17", "type": "Eclipse", "name": "Total Lunar Eclipse", 
         "description": "Visible from Americas, Europe, and Africa", "visibility": "Multi-continental"},
        {"date": "2026-03-20", "type": "Alignment", "name": "Spring Equinox", 
         "description": "Equal day and night", "visibility": "Global"},
        {"date": "2026-04-22", "type": "Meteor Shower", "name": "Lyrids Meteor Shower", 
         "description": "One of the oldest known meteor showers", "visibility": "Global"},
        {"date": "2026-05-06", "type": "Meteor Shower", "name": "Eta Aquarids Meteor Shower", 
         "description": "Debris from Halley's Comet", "visibility": "Southern Hemisphere"},
        {"date": "2026-06-21", "type": "Alignment", "name": "Summer Solstice", 
         "description": "Longest day of the year in Northern Hemisphere", "visibility": "Global"},
        {"date": "2026-08-12", "type": "Eclipse", "name": "Total Solar Eclipse", 
         "description": "Path of totality crosses Greenland, Iceland, and Spain", "visibility": "Regional"},
        {"date": "2026-08-13", "type": "Meteor Shower", "name": "Perseids Meteor Shower", 
         "description": "Most popular meteor shower of the year", "visibility": "Global"},
        {"date": "2026-09-22", "type": "Alignment", "name": "Autumn Equinox", 
         "description": "Equal day and night", "visibility": "Global"},
    ]
    return events

def filter_events_by_type(events, event_type=None):
    """Filter events by type"""
    if event_type:
        return [e for e in events if e["type"].lower() == event_type.lower()]
    return events

def filter_events_by_date_range(events, start_date=None, end_date=None):
    """Filter events within a date range"""
    filtered = []
    for event in events:
        event_date = datetime.strptime(event["date"], "%Y-%m-%d")
        if start_date and event_date < start_date:
            continue
        if end_date and event_date > end_date:
            continue
        filtered.append(event)
    return filtered

def display_events(events):
    """Display celestial events in a formatted manner"""
    if not events:
        print("No events found matching your criteria.")
        return
    
    print("\n" + "="*60)
    print("UPCOMING CELESTIAL EVENTS".center(60))
    print("="*60 + "\n")
    
    for event in events:
        print(f"Date: {event['date']}")
        print(f"Type: {event['type']}")
        print(f"Event: {event['name']}")
        print(f"Details: {event['description']}")
        print(f"Visibility: {event['visibility']}")
        print("-" * 60)

def main():
    """Main function to run the celestial events calendar"""
    events = get_celestial_events()
    
    # Filter for upcoming events (from today onwards)
    today = datetime.now()
    upcoming_events = filter_events_by_date_range(events, start_date=today)
    
    print("\nWelcome to the Celestial Events Calendar!")
    print(f"Current Date: {today.strftime('%Y-%m-%d')}\n")
    
    # Display all upcoming events
    display_events(upcoming_events)
    
    # Example: Display only meteor showers
    print("\n\nUPCOMING METEOR SHOWERS:")
    meteor_showers = filter_events_by_type(upcoming_events, "Meteor Shower")
    display_events(meteor_showers)

if __name__ == "__main__":
    main()
