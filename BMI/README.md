# 🧮 BMI Logger
A simple Python program to calculate and log your Body Mass Index (BMI) along with the date, height, and weight into a CSV file.

## 📋 Features
- Prompts user for height (in meters) and weight (in kilograms)
- Calculates BMI using the standard formula
- Automatically saves the data (date, height, weight, BMI) into bmi_log.csv
- Creates the CSV file with headers if it doesn’t exist
- Handles invalid or non-numeric input gracefully

## 🚀 How to Run
- Open a terminal in the `BMI` directory and run:
> python bmi_logger.py
- Enter your height and weight when prompted.

## 📂 Output
A file named bmi_log.csv will be created (if not already present) with entries like:
| date       | height_m | weight_kg | bmi   |
| ---------- | -------- | --------- | ----- |
| 2025-10-25 | 1.75     | 70.0      | 22.86 |

Additionaly BMI will be displayed on the terminal each time user will make a entry.
## ⚠️ Notes
- Ensure height and weight are positive numbers.
- If you enter invalid data (e.g., text instead of numbers), the program will show an error message.
