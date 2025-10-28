import pandas as pd
import matplotlib.pyplot as plt
import sys
from pathlib import Path

def load_steps_data(csv_file):
    """
    Load steps data from CSV file.

    Args:
        csv_file (str): Path to CSV file

    Returns:
        pandas.DataFrame: DataFrame with date and steps columns
    """
    try:
        df = pd.read_csv(csv_file)
        # Convert date column to datetime
        df['date'] = pd.to_datetime(df['date'])
        return df
    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error loading CSV: {e}")
        sys.exit(1)

def plot_steps_bar_chart(df, output_file='steps_chart.png'):
    """
    Create and save a bar chart of daily steps.

    Args:
        df (pandas.DataFrame): DataFrame with date and steps columns
        output_file (str): Output filename for the chart
    """
    plt.figure(figsize=(12, 6))

    # Create bar chart
    plt.bar(df['date'].dt.strftime('%Y-%m-%d'), df['steps'], 
            color='#4CAF50', edgecolor='black', linewidth=0.5)

    # Customize chart
    plt.xlabel('Date', fontsize=12, fontweight='bold')
    plt.ylabel('Steps', fontsize=12, fontweight='bold')
    plt.title('Daily Steps Walked', fontsize=14, fontweight='bold')
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', alpha=0.3, linestyle='--')

    # Add value labels on bars
    for i, (date, steps) in enumerate(zip(df['date'], df['steps'])):
        plt.text(i, steps + max(df['steps']) * 0.01, str(steps), 
                ha='center', va='bottom', fontsize=9)

    plt.tight_layout()
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"Chart saved as '{output_file}'")
    plt.show()

def main():
    """Main function to execute the script."""
    # Default CSV file
    csv_file = 'steps_data.csv'

    # Check if custom file provided
    if len(sys.argv) > 1:
        csv_file = sys.argv[1]

    # Check if file exists
    if not Path(csv_file).exists():
        print(f"CSV file '{csv_file}' not found. Creating sample data...")
        create_sample_data(csv_file)

    # Load and plot data
    df = load_steps_data(csv_file)
    plot_steps_bar_chart(df)

    # Display statistics
    print(f"\nStatistics:")
    print(f"Total days: {len(df)}")
    print(f"Average steps: {df['steps'].mean():.0f}")
    print(f"Maximum steps: {df['steps'].max()} on {df.loc[df['steps'].idxmax(), 'date'].strftime('%Y-%m-%d')}")
    print(f"Minimum steps: {df['steps'].min()} on {df.loc[df['steps'].idxmin(), 'date'].strftime('%Y-%m-%d')}")

def create_sample_data(filename='steps_data.csv'):
    """Create sample CSV data for demonstration."""
    sample_data = """date,steps
2025-10-18,8500
2025-10-19,12300
2025-10-20,9800
2025-10-21,15200
2025-10-22,7600
2025-10-23,11400
2025-10-24,13800"""

    with open(filename, 'w') as f:
        f.write(sample_data)
    print(f"Sample data created in '{filename}'")

if __name__ == "__main__":
    main()