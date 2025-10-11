import time
import json
import os
from datetime import datetime

class PomodoroTimer:
    def __init__(self, work_time=25, short_break=5, long_break=15):
        self.work_time = work_time * 60  # Convert to seconds
        self.short_break = short_break * 60
        self.long_break = long_break * 60
        self.analytics_file = 'pomodoro_analytics.json'
        self.analytics = self.load_analytics()
    
    def load_analytics(self):
        """Load analytics data from JSON file"""
        if os.path.exists(self.analytics_file):
            with open(self.analytics_file, 'r') as f:
                return json.load(f)
        return {'total_sessions': 0, 'completed_sessions': 0, 'interrupted_sessions': 0, 
                'total_focus_time': 0, 'sessions_history': []}
    
    def save_analytics(self):
        """Save analytics data to JSON file"""
        with open(self.analytics_file, 'w') as f:
            json.dump(self.analytics, f, indent=4)
    
    def countdown(self, duration, session_type):
        """Run countdown timer with real-time display"""
        start_time = time.time()
        try:
            while duration > 0:
                mins, secs = divmod(duration, 60)
                timer = f'{mins:02d}:{secs:02d}'
                print(f'\r{session_type}: {timer}', end='', flush=True)
                time.sleep(1)
                duration -= 1
            print(f'\n{session_type} completed! 🎉')
            return True
        except KeyboardInterrupt:
            elapsed = int(time.time() - start_time)
            print(f'\n\nSession interrupted after {elapsed // 60} minutes')
            return False
    
    def run_session(self, session_num):
        """Run a single Pomodoro session with break"""
        print(f'\n🍅 Pomodoro Session #{session_num} starting...')
        self.analytics['total_sessions'] += 1
        
        # Work session
        completed = self.countdown(self.work_time, 'Work Time')
        
        if completed:
            self.analytics['completed_sessions'] += 1
            self.analytics['total_focus_time'] += self.work_time // 60
            
            # Determine break type (long break after every 4th session)
            if session_num % 4 == 0:
                break_time = self.long_break
                break_type = 'Long Break'
            else:
                break_time = self.short_break
                break_type = 'Short Break'
            
            print(f'\nStarting {break_type}...')
            self.countdown(break_time, break_type)
        else:
            self.analytics['interrupted_sessions'] += 1
        
        # Record session in history
        self.analytics['sessions_history'].append({
            'session': session_num,
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'completed': completed
        })
        self.save_analytics()
    
    def show_analytics(self):
        """Display focus analytics and productivity stats"""
        print('\n📊 Focus Analytics Dashboard')
        print('=' * 50)
        print(f'Total Sessions Started: {self.analytics["total_sessions"]}')
        print(f'Completed Sessions: {self.analytics["completed_sessions"]}')
        print(f'Interrupted Sessions: {self.analytics["interrupted_sessions"]}')
        print(f'Total Focus Time: {self.analytics["total_focus_time"]} minutes')
        
        if self.analytics['total_sessions'] > 0:
            completion_rate = (self.analytics['completed_sessions'] / 
                             self.analytics['total_sessions']) * 100
            print(f'Completion Rate: {completion_rate:.1f}%')
        
        print('\nRecent Sessions:')
        for session in self.analytics['sessions_history'][-5:]:
            status = '✓ Completed' if session['completed'] else '✗ Interrupted'
            print(f"  Session #{session['session']}: {status} ({session['date']})")
        print('=' * 50)

if __name__ == '__main__':
    timer = PomodoroTimer()
    timer.show_analytics()
    
    session_count = 1
    while True:
        timer.run_session(session_count)
        session_count += 1
        cont = input('\nContinue to next session? (y/n): ').lower()
        if cont != 'y':
            timer.show_analytics()
            break
