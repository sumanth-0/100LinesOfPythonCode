
## Overview
This project implements an ASCII-based digital clock with signal analysis using the Matrix Fourier Transform (DFT). It displays the current time in a 7-segment ASCII style and performs a Fast Fourier Transform (FFT) on a tic-tac signal to analyze its frequency components.

## Project Structure
The project consists of two main files:

- **sevseg.py**: A module to display numbers in ASCII 7-segment style.
- **ledigital_clock_FFT.py**: The main script that displays the clock and calculates the FFT of a tic-tac signal.

## Files Description

### 1. sevseg.py – 7-Segment Display
**Purpose**  
This module converts digits or numbers into ASCII characters representing a classic 7-segment digital display.

**How It Works**  
- **DIGITS Dictionary**: Contains 3×3 ASCII patterns for digits 0–9.
- **Function** `getSevSegStr(number, minWidth=1)`:
  - Converts the input number into a string, adding leading zeros if necessary to meet the `minWidth` requirement.
  - Retrieves the corresponding ASCII lines for each digit from the `DIGITS` dictionary.
  - Joins the lines to create the complete 7-segment ASCII display.

**Example**  
Input: `getSevSegStr(42, 3)`  
Output:
```
 _       _ 
|_|     | |
|_|     |_| 
```

### 2. ledigital_clock_FFT.py – Main Script
**Purpose**  
This script combines the ASCII digital clock display with signal analysis by computing the FFT of a tic-tac signal.

**How It Works**  
- **Clock Display**: Uses `sevseg.py` to render the current time in ASCII 7-segment style.
- **FFT Analysis**: Generates a tic-tac signal and applies the Matrix Fourier Transform to analyze its frequency components.

## Requirements
- Python 3.x
- NumPy (for FFT calculations)
- (Optional) Additional libraries may be required for signal generation or visualization, depending on implementation.

## Installation
1. Clone or download the project repository.
2. Ensure Python 3.x is installed.
3. Install required dependencies:  
   ```bash
   pip install numpy
   ```

## Usage
1. Run the main script:  
   ```bash
   python ledigital_clock_FFT.py
   ```
2. The ASCII digital clock will display the current time, and the FFT analysis of the tic-tac signal will be computed and displayed (if configured).

## Example Output
**Current Time:**
```
 _       _       _ 
| |     | |     | |
|_|     |_|     |_| 
```
**FFT Analysis:**  
```
[Frequency components and amplitudes]
```




