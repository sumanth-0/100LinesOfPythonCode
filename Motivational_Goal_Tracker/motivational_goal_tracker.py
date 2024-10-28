import matplotlib.pyplot as plt

# List of motivational quotes
quotes = [
    "Keep going! You're getting closer to your goal!",
    "Every step counts, no matter how small!",
    "Believe in yourself and all that you are!",
    "Success is not final, failure is not fatal: It is the courage to continue that counts."
]

def track_goals():
    """Track and visualize user goals."""
    goals = {}
    
    while True:
        goal = input("Enter a goal (or type 'done' to finish): ")
        if goal.lower() == 'done':
            break
        progress = int(input(f"Enter your progress for '{goal}' (0-100): "))
        goals[goal] = progress
    
    return goals

def display_progress(goals):
    """Display the progress of goals in a bar chart."""
    names = list(goals.keys())
    values = list(goals.values())
    
    plt.figure(figsize=(10, 5))
    plt.bar(names, values, color='skyblue')
    plt.xlabel('Goals')
    plt.ylabel('Progress (%)')
    plt.title('Motivational Goal Tracker')
    plt.ylim(0, 100)
    plt.axhline(y=100, color='r', linestyle='--', label='Goal Completed')
    plt.legend()
    plt.show()
    
    # Provide a motivational quote based on progress
    for goal, progress in goals.items():
        if progress >= 100:
            print(f"🎉 Congratulations on completing your goal: '{goal}'!")
        else:
            print(f"{quotes[progress // 25]}")

def main():
    """Main function to run the goal tracker."""
    goals = track_goals()
    display_progress(goals)

if __name__ == "__main__":
    main()
