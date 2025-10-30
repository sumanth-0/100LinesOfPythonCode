import matplotlib.pyplot as plt
import numpy as np

def visualize_sleep_data():
    """
    Creates and saves a bar chart of daily sleep durations
    with the weekly average.
    """
    
    # --- 1. Sample Data ---
    # You can change this data to your own!
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    # Sleep durations in hours
    hours = [7.5, 6.0, 8.0, 6.5, 7.0, 9.0, 8.5]
    
    # --- 2. Calculate the Average ---
    average_sleep = np.mean(hours)
    
    # --- 3. Create the Visualization ---
    plt.figure(figsize=(10, 6))

    # Create the bar chart
    plt.bar(days, hours, color='skyblue', label='Daily Sleep (hrs)')

    # Add the average line
    plt.axhline(
        average_sleep, 
        color='red', 
        linestyle='--', 
        linewidth=2, 
        label=f'Weekly Avg: {average_sleep:.2f} hrs'
    )

    # Add text labels on top of each bar
    for i, hour in enumerate(hours):
        plt.text(i, hour + 0.1, f'{hour:.1f}', ha='center', fontweight='bold')

    # --- 4. Customize the Plot ---
    plt.title('Weekly Sleep Duration', fontsize=16)
    plt.xlabel('Day of the Week', fontsize=12)
    plt.ylabel('Hours Slept', fontsize=12)
    
    # Set Y-axis limits to give some space
    plt.ylim(0, max(hours) + 2) 
    
    plt.legend(fontsize=12)
    plt.grid(axis='y', linestyle=':', alpha=0.7)
    
    # Ensure layout is clean
    plt.tight_layout()

    # --- 5. Display the File (Instead of Saving) ---
    # plot_filename = "sleep_duration_chart.png"
    # plt.savefig(plot_filename)
    # print(f"Chart saved as {plot_filename}")
    
    print(f"Weekly average sleep: {average_sleep:.2f} hours")

    # Add this line to show the plot:
    plt.show()

if __name__ == "__main__":
    visualize_sleep_data()