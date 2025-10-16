# CSV Column Summarizer
Reads a CSV file and calculates sums, averages, and counts for numeric columns.

## How to Run
```bash
python csv_column_summarizer.py
```
Example Input:
data.csv:
```bash
Name,Math,Science,English
Divya,90,85,92
Sumanth,80,78,88
Aarav,75,,91
```
Example Output:
```bash
Column               Count          Sum      Average
--------------------------------------------------
Math                     3        245.00        81.67
Science                  2        163.00        81.50
English                  3        271.00        90.33
```