# Calendar Heatmap Generator

## Description
A GitHub-style activity calendar heatmap generator that visualizes data over a year. This tool can display the heatmap using ASCII characters for terminal output or create a high-quality visualization using matplotlib.

## Features
- Generate random activity data for testing (365 days)
- ASCII-based calendar heatmap for terminal viewing
- Matplotlib-based visualization with color intensity mapping
- GitHub-style weekly calendar layout (Monday to Sunday)
- Customizable intensity levels
- Save as PNG image

## Requirements
- Python 3.x
- matplotlib (optional, for graphical output)
- numpy (optional, for graphical output)

## Installation
```bash
# For ASCII output only (no dependencies needed)
python3 calendar_heatmap_generator.py

# For graphical output, install dependencies:
pip install matplotlib numpy
```

## Usage
Run the script directly:
```bash
python3 calendar_heatmap_generator.py
```

The script will:
1. Generate random activity data for the past 365 days
2. Display an ASCII heatmap in the terminal
3. Attempt to create a matplotlib visualization (if dependencies are installed)
4. Save the graphical heatmap as 'calendar_heatmap.png'

## Example Output

### ASCII Heatmap
```
Calendar Heatmap (Last 365 days)
==================================================
Mon Tue Wed Thu Fri Sat Sun
 ░   ▒   ▓   █   ░   ▒   ▓
 █   ░   ▒   ▓   █   ░   ▒
...

Legend: Less     ░ ▒ ▓ █ More
```

### Matplotlib Output
A colorful heatmap image saved as `calendar_heatmap.png` with:
- Green color intensity representing activity levels
- Week numbers on the x-axis
- Days of the week on the y-axis
- Color bar showing the activity level scale

## Customization
You can modify the script to:
- Use your own activity data instead of random values
- Change the color scheme
- Adjust the time range (default: 365 days)
- Customize intensity levels and symbols

## Contributing
Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## Related Issue
This implementation addresses issue #678 in the 100LinesOfPythonCode repository.

## License
This project is part of the 100LinesOfPythonCode repository.
