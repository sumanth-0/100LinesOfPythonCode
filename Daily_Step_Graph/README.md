# Step Counter Bar Chart Plotter

A simple Python script to visualize your daily step count data as a bar chart.

## Installation

1. Clone or download this repository
2. Install required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

```bash
python plot_steps.py
```

This will look for `steps_data.csv` in the current directory. If not found, it will create sample data.

### Custom CSV File

```bash
python plot_steps.py your_data.csv
```

## CSV Format

Your CSV file should have at least two columns:

- **date**: Date in format YYYY-MM-DD (or any readable date format)
- **steps**: Number of steps walked (integer)

### Example CSV:

```csv
date,steps
2025-10-18,8500
2025-10-19,12300
2025-10-20,9800
2025-10-21,15200
2025-10-22,7600
```

## Output

The script generates:
- **steps_chart.png**: A high-resolution bar chart (300 DPI)
- **Console statistics**: Total days, average, max, and min steps
