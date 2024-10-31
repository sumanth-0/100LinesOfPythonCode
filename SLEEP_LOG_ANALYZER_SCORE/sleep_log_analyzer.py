
# Sleep Log Analyzer

import pandas as pd
import matplotlib.pyplot as plt

def analyze_sleep_data(file_path):
    # Load sleep data from a CSV file
    sleep_data = pd.read_csv(file_path)
    
    # Calculate average sleep duration
    avg_duration = sleep_data['Duration'].mean()
    ideal_hours = 8
    consistency = sleep_data['Duration'].std()

    # Provide feedback
    print(f"Average Sleep Duration: {avg_duration:.2f} hours")
    print(f"Sleep Consistency (Std. Dev.): {consistency:.2f} hours")
    
    if avg_duration < ideal_hours:
        print("You are getting less sleep than the ideal duration.")
    else:
        print("You are meeting or exceeding the ideal sleep duration.")

    return sleep_data

def plot_sleep_data(sleep_data):
    plt.figure(figsize=(10, 5))
    plt.plot(sleep_data['Date'], sleep_data['Duration'], marker='o')
    plt.title("Sleep Duration Over Time")
    plt.xlabel("Date")
    plt.ylabel("Duration (hours)")
    plt.xticks(rotation=45)
    plt.grid()
    plt.tight_layout()
    plt.show()

def main():
    # Example CSV file path for sleep data
    file_path = input("Enter the path to your sleep log CSV file: ")

    sleep_data = analyze_sleep_data(file_path)
    plot_sleep_data(sleep_data)

if __name__ == "__main__":
    main()
