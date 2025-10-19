#!/usr/bin/env python3
"""
Reminder CLI - A command-line reminder application
Features:
- Schedule reminders with date and time
- List all scheduled reminders
- Delete reminders
- Persistent storage using JSON
- Clean terminal-based interface
"""

import json
import os
import sys
from datetime import datetime, timedelta
import argparse
from pathlib import Path

# Configuration
REMINDERS_FILE = Path.home() / '.reminders.json'


class ReminderManager:
    """Manages reminder operations including add, list, delete, and storage."""
    
    def __init__(self, storage_file=REMINDERS_FILE):
        """Initialize the reminder manager with a storage file."""
        self.storage_file = storage_file
        self.reminders = self.load_reminders()
    
    def load_reminders(self):
        """Load reminders from JSON file."""
        if not self.storage_file.exists():
            return []
        
        try:
            with open(self.storage_file, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            print(f"Warning: Could not load reminders from {self.storage_file}")
            return []
    
    def save_reminders(self):
        """Save reminders to JSON file."""
        try:
            with open(self.storage_file, 'w') as f:
                json.dump(self.reminders, f, indent=2)
        except IOError as e:
            print(f"Error saving reminders: {e}")
            sys.exit(1)
    
    def add_reminder(self, message, date_str, time_str):
        """Add a new reminder with validation."""
        try:
            # Parse date and time
            reminder_datetime = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
            
            # Check if the reminder is in the future
            if reminder_datetime <= datetime.now():
                print("Error: Reminder time must be in the future.")
                return False
            
            # Create reminder object
            reminder = {
                'id': len(self.reminders) + 1,
                'message': message,
                'datetime': reminder_datetime.isoformat(),
                'created_at': datetime.now().isoformat()
            }
            
            self.reminders.append(reminder)
            self.save_reminders()
            print(f"✓ Reminder added: '{message}' on {reminder_datetime.strftime('%Y-%m-%d at %H:%M')}")
            return True
            
        except ValueError as e:
            print(f"Error parsing date/time: {e}")
            print("Expected format: YYYY-MM-DD HH:MM")
            return False
    
    def list_reminders(self, show_all=False):
        """List all reminders or only upcoming ones."""
        if not self.reminders:
            print("No reminders found.")
            return
        
        now = datetime.now()
        active_reminders = []
        
        for reminder in self.reminders:
            reminder_dt = datetime.fromisoformat(reminder['datetime'])
            if show_all or reminder_dt > now:
                active_reminders.append(reminder)
        
        if not active_reminders:
            print("No active reminders.")
            return
        
        # Sort by datetime
        active_reminders.sort(key=lambda x: x['datetime'])
        
        print("\n" + "="*60)
        print(f"{'ID':<5} {'Date':<12} {'Time':<8} {'Message':<30}")
        print("="*60)
        
        for reminder in active_reminders:
            reminder_dt = datetime.fromisoformat(reminder['datetime'])
            date_str = reminder_dt.strftime('%Y-%m-%d')
            time_str = reminder_dt.strftime('%H:%M')
            message = reminder['message'][:27] + '...' if len(reminder['message']) > 30 else reminder['message']
            print(f"{reminder['id']:<5} {date_str:<12} {time_str:<8} {message:<30}")
        
        print("="*60 + "\n")
    
    def delete_reminder(self, reminder_id):
        """Delete a reminder by ID."""
        for i, reminder in enumerate(self.reminders):
            if reminder['id'] == reminder_id:
                deleted = self.reminders.pop(i)
                self.save_reminders()
                print(f"✓ Deleted reminder: '{deleted['message']}'")
                return True
        
        print(f"Error: Reminder with ID {reminder_id} not found.")
        return False
    
    def check_due_reminders(self):
        """Check and display due reminders."""
        now = datetime.now()
        due_reminders = []
        
        for reminder in self.reminders:
            reminder_dt = datetime.fromisoformat(reminder['datetime'])
            # Check if reminder is due (within the last 5 minutes)
            if now >= reminder_dt and (now - reminder_dt).total_seconds() <= 300:
                due_reminders.append(reminder)
        
        if due_reminders:
            print("\n" + "!"*60)
            print("REMINDERS DUE!")
            print("!"*60)
            for reminder in due_reminders:
                print(f"• {reminder['message']}")
            print("!"*60 + "\n")


def main():
    """Main function to handle CLI arguments and execute commands."""
    parser = argparse.ArgumentParser(
        description='Reminder CLI - Schedule and manage reminders in your terminal',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  reminder_cli.py add "Team meeting" 2025-10-20 14:30
  reminder_cli.py list
  reminder_cli.py delete 1
  reminder_cli.py check
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Add command
    add_parser = subparsers.add_parser('add', help='Add a new reminder')
    add_parser.add_argument('message', help='Reminder message')
    add_parser.add_argument('date', help='Date (YYYY-MM-DD)')
    add_parser.add_argument('time', help='Time (HH:MM)')
    
    # List command
    list_parser = subparsers.add_parser('list', help='List all reminders')
    list_parser.add_argument('--all', action='store_true', help='Show all reminders including past ones')
    
    # Delete command
    delete_parser = subparsers.add_parser('delete', help='Delete a reminder')
    delete_parser.add_argument('id', type=int, help='Reminder ID to delete')
    
    # Check command
    check_parser = subparsers.add_parser('check', help='Check for due reminders')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    manager = ReminderManager()
    
    # Execute command
    if args.command == 'add':
        manager.add_reminder(args.message, args.date, args.time)
    elif args.command == 'list':
        manager.list_reminders(show_all=args.all)
    elif args.command == 'delete':
        manager.delete_reminder(args.id)
    elif args.command == 'check':
        manager.check_due_reminders()


if __name__ == '__main__':
    main()
