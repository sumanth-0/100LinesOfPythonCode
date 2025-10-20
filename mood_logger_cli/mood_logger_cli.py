#!/usr/bin/env python3
"""
Mood Logger CLI - A command-line tool for logging and tracking your daily moods
Author: Contributors to 100LinesOfPythonCode
Issue: #1031
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path
import argparse
from collections import Counter

# Configuration
DATA_FILE = os.path.expanduser('~/.mood_logger_data.json')

# Available mood options
MOOD_OPTIONS = [
    'happy', 'sad', 'anxious', 'excited', 'calm', 
    'stressed', 'grateful', 'angry', 'peaceful', 'energetic',
    'tired', 'motivated', 'frustrated', 'content', 'overwhelmed'
]

# Mood emojis for better visualization
MOOD_EMOJIS = {
    'happy': '😊', 'sad': '😢', 'anxious': '😰', 'excited': '🤩',
    'calm': '😌', 'stressed': '😫', 'grateful': '🙏', 'angry': '😠',
    'peaceful': '☮️', 'energetic': '⚡', 'tired': '😴', 'motivated': '💪',
    'frustrated': '😤', 'content': '😊', 'overwhelmed': '😵'
}


def load_data():
    """Load mood data from JSON file"""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {'entries': []}
    return {'entries': []}


def save_data(data):
    """Save mood data to JSON file"""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)


def log_mood(mood, note=''):
    """Log a new mood entry"""
    if mood.lower() not in MOOD_OPTIONS:
        print(f"\n❌ Invalid mood. Please choose from: {', '.join(MOOD_OPTIONS)}")
        return False
    
    data = load_data()
    entry = {
        'mood': mood.lower(),
        'note': note,
        'timestamp': datetime.now().isoformat()
    }
    data['entries'].append(entry)
    save_data(data)
    
    emoji = MOOD_EMOJIS.get(mood.lower(), '🌟')
    print(f"\n{emoji} Mood logged successfully!")
    print(f"Mood: {mood.capitalize()}")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    if note:
        print(f"Note: {note}")
    return True


def view_moods(limit=10, filter_mood=None):
    """View recent mood entries"""
    data = load_data()
    entries = data.get('entries', [])
    
    if not entries:
        print("\n📝 No mood entries found. Start logging your moods!")
        return
    
    # Filter by mood if specified
    if filter_mood:
        entries = [e for e in entries if e['mood'] == filter_mood.lower()]
        if not entries:
            print(f"\n🔍 No entries found for mood: {filter_mood}")
            return
    
    # Get recent entries
    recent_entries = entries[-limit:] if limit else entries
    recent_entries.reverse()
    
    print("\n" + "="*60)
    print(f"{'MOOD LOG ENTRIES':<60}")
    print("="*60)
    
    for i, entry in enumerate(recent_entries, 1):
        mood = entry['mood']
        emoji = MOOD_EMOJIS.get(mood, '🌟')
        timestamp = datetime.fromisoformat(entry['timestamp'])
        formatted_time = timestamp.strftime('%Y-%m-%d %H:%M:%S')
        
        print(f"\n{i}. {emoji} {mood.upper()}")
        print(f"   Time: {formatted_time}")
        if entry.get('note'):
            print(f"   Note: {entry['note']}")
    
    print("\n" + "="*60)


def show_stats():
    """Display mood statistics"""
    data = load_data()
    entries = data.get('entries', [])
    
    if not entries:
        print("\n📊 No mood data available for statistics.")
        return
    
    moods = [e['mood'] for e in entries]
    mood_counts = Counter(moods)
    total_entries = len(entries)
    
    print("\n" + "="*60)
    print(f"{'MOOD STATISTICS':<60}")
    print("="*60)
    print(f"\nTotal entries: {total_entries}")
    print(f"\nMood breakdown:")
    
    for mood, count in mood_counts.most_common():
        emoji = MOOD_EMOJIS.get(mood, '🌟')
        percentage = (count / total_entries) * 100
        bar_length = int(percentage / 2)
        bar = '█' * bar_length
        print(f"  {emoji} {mood.capitalize():<15} {bar} {count} ({percentage:.1f}%)")
    
    # Most common mood
    most_common = mood_counts.most_common(1)[0]
    emoji = MOOD_EMOJIS.get(most_common[0], '🌟')
    print(f"\n🏆 Most common mood: {emoji} {most_common[0].capitalize()} ({most_common[1]} times)")
    
    # Recent mood trend (last 5 entries)
    if len(entries) >= 5:
        recent_moods = [e['mood'] for e in entries[-5:]]
        print(f"\n📈 Recent trend (last 5): {' → '.join([MOOD_EMOJIS.get(m, '🌟') + m.capitalize() for m in recent_moods])}")
    
    print("\n" + "="*60)


def delete_entry(index):
    """Delete a mood entry by index"""
    data = load_data()
    entries = data.get('entries', [])
    
    if not entries:
        print("\n❌ No entries to delete.")
        return
    
    if 0 < index <= len(entries):
        deleted = entries.pop(-index)
        save_data(data)
        print(f"\n🗑️ Deleted entry: {deleted['mood'].capitalize()} from {deleted['timestamp']}")
    else:
        print(f"\n❌ Invalid index. Please choose between 1 and {len(entries)}")


def clear_all_data():
    """Clear all mood data"""
    confirm = input("\n⚠️  Are you sure you want to delete all mood entries? (yes/no): ")
    if confirm.lower() == 'yes':
        save_data({'entries': []})
        print("\n✅ All mood data cleared.")
    else:
        print("\n❌ Operation cancelled.")


def list_moods():
    """List all available mood options"""
    print("\n" + "="*60)
    print(f"{'AVAILABLE MOODS':<60}")
    print("="*60)
    for i in range(0, len(MOOD_OPTIONS), 3):
        row = MOOD_OPTIONS[i:i+3]
        mood_str = '  '.join([f"{MOOD_EMOJIS.get(m, '🌟')} {m.capitalize():<12}" for m in row])
        print(f"  {mood_str}")
    print("\n" + "="*60)


def main():
    """Main function to handle CLI arguments"""
    parser = argparse.ArgumentParser(
        description='Mood Logger CLI - Track your daily moods with timestamps',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='Examples:\n'
               '  mood_logger_cli.py log happy "Had a great day!"\n'
               '  mood_logger_cli.py view\n'
               '  mood_logger_cli.py stats\n'
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Log command
    log_parser = subparsers.add_parser('log', help='Log a new mood')
    log_parser.add_argument('mood', help='Your current mood')
    log_parser.add_argument('note', nargs='?', default='', help='Optional note about your mood')
    
    # View command
    view_parser = subparsers.add_parser('view', help='View recent mood entries')
    view_parser.add_argument('-l', '--limit', type=int, default=10, help='Number of entries to show')
    view_parser.add_argument('-f', '--filter', help='Filter by specific mood')
    
    # Stats command
    subparsers.add_parser('stats', help='Display mood statistics')
    
    # Delete command
    delete_parser = subparsers.add_parser('delete', help='Delete a mood entry')
    delete_parser.add_argument('index', type=int, help='Index of entry to delete (from recent view)')
    
    # Clear command
    subparsers.add_parser('clear', help='Clear all mood data')
    
    # List command
    subparsers.add_parser('list', help='List all available moods')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    # Execute commands
    if args.command == 'log':
        log_mood(args.mood, args.note)
    elif args.command == 'view':
        view_moods(args.limit, args.filter)
    elif args.command == 'stats':
        show_stats()
    elif args.command == 'delete':
        delete_entry(args.index)
    elif args.command == 'clear':
        clear_all_data()
    elif args.command == 'list':
        list_moods()


if __name__ == '__main__':
    main()
