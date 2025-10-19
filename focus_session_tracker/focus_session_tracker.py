#!/usr/bin/env python3
"""
Focus Session Tracker
A comprehensive tool to track focus/work sessions with timer, logging, and statistics.

Features:
- Session timer with countdown
- Session logging to file
- Statistics tracking (total time, average session, etc.)
- Break reminders
- Session history review
"""

import time
import json
import os
from datetime import datetime, timedelta
from pathlib import Path


class FocusSessionTracker:
    """Main class for tracking focus sessions"""
    
    def __init__(self, data_file='focus_sessions.json'):
        self.data_file = data_file
        self.sessions = self.load_sessions()
        self.current_session = None
        
    def load_sessions(self):
        """Load session history from JSON file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return []
        return []
    
    def save_sessions(self):
        """Save session history to JSON file"""
        with open(self.data_file, 'w') as f:
            json.dump(self.sessions, f, indent=2)
    
    def start_session(self, duration_minutes, task_name=''):
        """Start a new focus session"""
        self.current_session = {
            'task': task_name,
            'start_time': datetime.now().isoformat(),
            'planned_duration': duration_minutes,
            'actual_duration': 0,
            'completed': False
        }
        
        print(f"\n🎯 Starting focus session: {task_name}")
        print(f"⏱️  Duration: {duration_minutes} minutes\n")
        
        start_time = time.time()
        duration_seconds = duration_minutes * 60
        
        try:
            while True:
                elapsed = time.time() - start_time
                remaining = duration_seconds - elapsed
                
                if remaining <= 0:
                    print("\n✅ Session completed! Great work!\n")
                    self.current_session['completed'] = True
                    self.current_session['actual_duration'] = duration_minutes
                    break
                
                mins, secs = divmod(int(remaining), 60)
                hours, mins = divmod(mins, 60)
                
                print(f"\r⏰ Time remaining: {hours:02d}:{mins:02d}:{secs:02d}", end='', flush=True)
                time.sleep(1)
                
        except KeyboardInterrupt:
            elapsed_minutes = (time.time() - start_time) / 60
            self.current_session['actual_duration'] = round(elapsed_minutes, 2)
            print(f"\n\n⏸️  Session interrupted after {elapsed_minutes:.1f} minutes\n")
        
        self.current_session['end_time'] = datetime.now().isoformat()
        self.sessions.append(self.current_session)
        self.save_sessions()
        
    def view_statistics(self):
        """Display session statistics"""
        if not self.sessions:
            print("\n📊 No sessions recorded yet.\n")
            return
        
        total_sessions = len(self.sessions)
        completed_sessions = sum(1 for s in self.sessions if s.get('completed', False))
        total_time = sum(s.get('actual_duration', 0) for s in self.sessions)
        avg_time = total_time / total_sessions if total_sessions > 0 else 0
        
        print("\n" + "="*50)
        print("📊 FOCUS SESSION STATISTICS")
        print("="*50)
        print(f"Total Sessions: {total_sessions}")
        print(f"Completed Sessions: {completed_sessions}")
        print(f"Completion Rate: {(completed_sessions/total_sessions*100):.1f}%")
        print(f"Total Focus Time: {total_time:.1f} minutes ({total_time/60:.1f} hours)")
        print(f"Average Session: {avg_time:.1f} minutes")
        print("="*50 + "\n")
        
    def view_history(self, limit=10):
        """Display recent session history"""
        if not self.sessions:
            print("\n📜 No session history available.\n")
            return
        
        print("\n" + "="*50)
        print("📜 SESSION HISTORY (Most Recent)")
        print("="*50)
        
        recent_sessions = self.sessions[-limit:]
        recent_sessions.reverse()
        
        for i, session in enumerate(recent_sessions, 1):
            status = "✅" if session.get('completed', False) else "⏸️"
            task = session.get('task', 'Unnamed task')
            duration = session.get('actual_duration', 0)
            start = session.get('start_time', '')
            
            try:
                start_dt = datetime.fromisoformat(start)
                date_str = start_dt.strftime('%Y-%m-%d %H:%M')
            except:
                date_str = start
            
            print(f"\n{i}. {status} {task}")
            print(f"   Started: {date_str}")
            print(f"   Duration: {duration:.1f} minutes")
        
        print("\n" + "="*50 + "\n")
        
    def clear_history(self):
        """Clear all session history"""
        confirm = input("⚠️  Are you sure you want to clear all history? (yes/no): ")
        if confirm.lower() == 'yes':
            self.sessions = []
            self.save_sessions()
            print("\n✅ History cleared.\n")
        else:
            print("\n❌ Cancelled.\n")


def display_menu():
    """Display the main menu"""
    print("\n" + "="*50)
    print("🎯 FOCUS SESSION TRACKER")
    print("="*50)
    print("1. Start a focus session")
    print("2. View statistics")
    print("3. View session history")
    print("4. Clear history")
    print("5. Exit")
    print("="*50)


def main():
    """Main program loop"""
    tracker = FocusSessionTracker()
    
    print("\n🚀 Welcome to Focus Session Tracker!")
    print("Track your focus sessions and boost productivity.\n")
    
    while True:
        display_menu()
        choice = input("\nSelect an option (1-5): ").strip()
        
        if choice == '1':
            task_name = input("\nEnter task name: ").strip()
            try:
                duration = int(input("Enter session duration (minutes): ").strip())
                if duration <= 0:
                    print("\n❌ Duration must be positive!\n")
                    continue
                tracker.start_session(duration, task_name)
            except ValueError:
                print("\n❌ Invalid duration! Please enter a number.\n")
        
        elif choice == '2':
            tracker.view_statistics()
        
        elif choice == '3':
            tracker.view_history()
        
        elif choice == '4':
            tracker.clear_history()
        
        elif choice == '5':
            print("\n👋 Thank you for using Focus Session Tracker!")
            print("Keep up the great work!\n")
            break
        
        else:
            print("\n❌ Invalid option! Please select 1-5.\n")


if __name__ == '__main__':
    main()
