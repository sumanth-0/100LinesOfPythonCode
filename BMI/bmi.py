import csv
import datetime
import os

file_name = 'bmi_log.csv'
headers = ['date', 'height_m', 'weight_kg', 'bmi']

file_exists = os.path.exists(file_name)

try:
    height = float(input("Enter your height in meters (e.g., 1.75): "))
    weight = float(input("Enter your weight in kg (e.g., 70): "))

    if height <= 0 or weight <= 0:
        print("Error: Height and weight must be positive numbers.")
    else:
        bmi = weight / (height ** 2)
        today = datetime.date.today()
        data_row = [today, height, weight, round(bmi, 2)]

        with open(file_name, 'a', newline='') as f:
            writer = csv.writer(f)
            
            if not file_exists:
                writer.writerow(file_name)
            
            writer.writerow(data_row)

        print(f"Your BMI is: {bmi:.2f}")
        print(f"Your entry has been saved to {file_name}")

except ValueError:
    print("\nError: Invalid input. Please enter numbers only.")
