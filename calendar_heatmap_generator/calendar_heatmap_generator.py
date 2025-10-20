#!/usr/bin/env python3
"""
Calendar Heatmap Generator
Generates a GitHub-style activity calendar heatmap visualization using ASCII or matplotlib.
"""

import random
import datetime
from collections import defaultdict

def generate_random_activity(days=365):
    """Generate random activity data for the specified number of days."""
    activity = defaultdict(int)
    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=days-1)
    
    current_date = start_date
    while current_date <= end_date:
        # Random activity level (0-10)
        activity[current_date] = random.randint(0, 10)
        current_date += datetime.timedelta(days=1)
    
    return activity

def print_ascii_heatmap(activity):
    """Print ASCII calendar heatmap."""
    dates = sorted(activity.keys())
    if not dates:
        return
    
    # Define intensity levels
    levels = [' ', '░', '▒', '▓', '█']
    
    # Group by weeks
    weeks = defaultdict(list)
    for date in dates:
        week_num = date.isocalendar()[1]
        weeks[week_num].append(date)
    
    print("\nCalendar Heatmap (Last 365 days)")
    print("=" * 50)
    print("Mon Tue Wed Thu Fri Sat Sun")
    
    # Print heatmap
    for week in sorted(weeks.keys()):
        week_data = weeks[week]
        row = []
        
        # Align to start on Monday
        if week_data:
            start_weekday = week_data[0].weekday()
            row.extend([' . '] * start_weekday)
        
        for date in week_data:
            count = activity[date]
            level_idx = min(count // 3, len(levels) - 1)
            row.append(f' {levels[level_idx]} ')
        
        if len(row) > 0 and len(row) <= 7:
            print(''.join(row))
    
    print("\nLegend: Less " + ' '.join(levels) + " More")

def plot_matplotlib_heatmap(activity):
    """Plot calendar heatmap using matplotlib."""
    try:
        import matplotlib.pyplot as plt
        import numpy as np
        
        dates = sorted(activity.keys())
        if not dates:
            return
        
        # Create matrix for heatmap (weeks x 7 days)
        weeks = defaultdict(lambda: [0] * 7)
        
        for date in dates:
            week_num = date.isocalendar()[1]
            weekday = date.weekday()
            weeks[week_num][weekday] = activity[date]
        
        # Convert to numpy array
        matrix = np.array([weeks[w] for w in sorted(weeks.keys())])
        
        # Create plot
        fig, ax = plt.subplots(figsize=(12, 8))
        im = ax.imshow(matrix.T, cmap='Greens', aspect='auto')
        
        # Labels
        ax.set_yticks(range(7))
        ax.set_yticklabels(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
        ax.set_xlabel('Week')
        ax.set_title('Activity Calendar Heatmap')
        
        # Colorbar
        plt.colorbar(im, ax=ax, label='Activity Level')
        plt.tight_layout()
        plt.savefig('calendar_heatmap.png', dpi=150, bbox_inches='tight')
        print("\nHeatmap saved as 'calendar_heatmap.png'")
        
    except ImportError:
        print("Matplotlib not installed. Showing ASCII version only.")

if __name__ == "__main__":
    print("Calendar Heatmap Generator")
    print("=" * 50)
    
    # Generate random activity data
    activity_data = generate_random_activity(365)
    
    # Print ASCII heatmap
    print_ascii_heatmap(activity_data)
    
    # Try to plot with matplotlib
    plot_matplotlib_heatmap(activity_data)
