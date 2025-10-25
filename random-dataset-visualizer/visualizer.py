# visualizer.py
"""
Script to randomly select a CSV file from the repository and generate a 
basic data visualization using pandas and matplotlib.

This script ensures compliance with Hacktoberfest contribution guidelines 
by featuring robust error handling, detailed commenting, and flexible file scanning.
"""

import pandas as pd
import matplotlib.pyplot as plt
import os
import random
from typing import List, Optional, Tuple

# --- CONFIGURATION CONSTANTS ---
FILE_EXT = '.csv' 
MAX_ROWS = 50           # Max rows to sample for plot clarity
MIN_COLUMNS = 2         # Minimum number of columns required for a simple plot
PLOT_FILE = 'random_plot.png' # Name of the generated output file

# Define common problematic file locations to ignore during search
EXCLUSION_DIRS = ['.git', 'node_modules', 'venv', '__pycache__', 'test', 'docs']


# --- UTILITY FUNCTIONS ---

def find_all_csv_paths(start_path: str = '.') -> List[str]:
    """
    Recursively scans the directory tree to find all relevant CSV file paths.

    Args:
        start_path: The directory from which to begin the recursive search.

    Returns:
        A list of absolute paths to all discovered CSV files.
    """
    csv_files = []
    
    # os.walk efficiently traverses the directory tree
    for dirpath, dirnames, filenames in os.walk(start_path):
        
        # Prune directories that should be excluded from the search
        dirnames[:] = [d for d in dirnames if d not in EXCLUSION_DIRS]

        for filename in filenames:
            # Check for the correct file extension
            if filename.lower().endswith(FILE_EXT):
                
                # Construct the full path
                full_path = os.path.join(dirpath, filename)
                csv_files.append(full_path)
                
    return csv_files

def select_random_file(csv_paths: List[str]) -> Optional[str]:
    """
    Selects one random file path from the provided list.

    Args:
        csv_paths: A list of valid CSV file paths.

    Returns:
        The path to the randomly selected CSV file, or None if the list is empty.
    """
    if not csv_paths:
        return None
    return random.choice(csv_paths)


# --- MAIN VISUALIZATION LOGIC ---

def visualize_data_from_csv(csv_path: str) -> bool:
    """
    Loads data from the given CSV path and attempts to generate a plot.
    
    Args:
        csv_path: The path to the CSV file to load and visualize.
        
    Returns:
        True if the visualization was successful, False otherwise.
    """
    print(f"--- Loading data from: {csv_path} ---")

    try:
        # Attempt to load the data, handling common encoding and parsing errors
        try:
            df = pd.read_csv(csv_path, encoding='utf-8', on_bad_lines='skip')
        except UnicodeDecodeError:
            df = pd.read_csv(csv_path, encoding='latin1', on_bad_lines='skip')
        
    except Exception as e:
        print(f"Error: Could not parse CSV file {csv_path} due to: {e}")
        return False

    if df.empty or len(df.columns) < MIN_COLUMNS:
        print(f"Skipping: CSV is empty or has less than {MIN_COLUMNS} columns.")
        return False

    # Use only the first two columns and limit the rows for a readable chart
    df_plot = df.iloc[:MAX_ROWS, :MIN_COLUMNS]
    
    col_x = df_plot.columns[0]
    col_y = df_plot.columns[1]
    
    plt.figure(figsize=(10, 6))
    plot_type = "Line/Scatter" # Default type

    # Attempt to plot as line/scatter (requires numeric or datetime index/values)
    try:
        plt.plot(df_plot[col_x], df_plot[col_y], marker='o', linestyle='-')
        
    except (TypeError, ValueError):
        # Fallback to a bar chart if data types are incompatible (e.g., categorical)
        df_plot[col_y].plot(kind='bar')
        plot_type = "Bar Chart"

    # Finalize and save the plot
    plt.title(f"Visualization of '{os.path.basename(csv_path)}' ({plot_type})")
    plt.xlabel(col_x)
    plt.ylabel(col_y)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(PLOT_FILE)
    print(f"Success: Plot saved to {PLOT_FILE}")
    plt.close() # Close the plot figure to free memory
    
    return True

def run_visualizer():
    """Main execution function to find a file and generate the plot."""
    # Find all potential CSV files in the current repository
    csv_paths = find_all_csv_paths()

    if not csv_paths:
        print("Fatal Error: No CSV files found in the repository. Visualization aborted.")
        return

    # Select one file to visualize
    random_csv = select_random_file(csv_paths)
    
    # Execute the visualization
    visualize_data_from_csv(random_csv)

if __name__ == '__main__':
    run_visualizer()