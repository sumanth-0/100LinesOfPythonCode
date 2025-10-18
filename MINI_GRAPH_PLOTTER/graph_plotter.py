import pandas as pd
import matplotlib.pyplot as plt
import os

# --- Configuration ---
# Define the directory and filename relative to the script's location
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_FOLDER = "MINI_GRAPH_PLOTTER"
CSV_FILE = "data.csv"
OUTPUT_FILE = "sales_plot.png"

# Define the full path to the folder and files
FOLDER_PATH = os.path.join(SCRIPT_DIR, PROJECT_FOLDER)
CSV_PATH = os.path.join(FOLDER_PATH, CSV_FILE)
PLOT_PATH = os.path.join(FOLDER_PATH, OUTPUT_FILE)


def create_sample_csv():
    """Creates the necessary folder and sample CSV file with data."""
    
    # 1. Create directory if it doesn't exist
    if not os.path.exists(FOLDER_PATH):
        os.makedirs(FOLDER_PATH)
    
    # 2. Write the sample data to the file path
    print(f"Creating sample data at: {CSV_PATH}")
    with open(CSV_PATH, 'w') as f:
        # NOTE: Using \n for newlines is crucial for proper file structure
        f.write("Month,Sales\n")
        f.write("Jan,100\n")
        f.write("Feb,120\n")
        f.write("Mar,90\n")
        f.write("Apr,150\n")
        f.write("May,130\n")


def plot_sales_data(csv_path):
    """Reads data from the full CSV path and plots it."""
    
    # 1. Read data from the CSV file using pandas
    try:
        # Pandas reads the data using the guaranteed absolute path
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        print(f"Fatal Error: CSV file not found at {csv_path}")
        return
    
    # 2. Plotting logic
    x_data = df['Month']
    y_data = df['Sales']
    
    plt.figure(figsize=(8, 5))
    plt.plot(x_data, y_data, marker='o', linestyle='-', color='blue')
    
    plt.title('Monthly Sales Report')
    plt.xlabel('Month')
    plt.ylabel('Sales Volume')
    plt.grid(True)
    
    # 3. Save the figure to the defined PLOT_PATH
    plt.savefig(PLOT_PATH)
    print(f"Graph successfully saved as '{PLOT_PATH}'")


if __name__ == "__main__":
    
    # 1. ALWAYS ensure the data file is created/overwritten before plotting
    create_sample_csv()
    
    # 2. Pass the absolute path to the plotting function
    plot_sales_data(CSV_PATH)
