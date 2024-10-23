# BMI and Caloric Needs Calculator

This Python program calculates a user's Body Mass Index (BMI) and daily caloric needs based on their weight, height, age, gender, and activity level. It provides a simple and interactive way to help users understand their weight status and caloric requirements.

## Features

- Calculates BMI using weight and height.
- Determines weight category based on BMI value.
- Estimates daily caloric needs using the Mifflin-St Jeor equation.
- Accounts for different activity levels to provide personalized caloric needs.

## How It Works

### Components

1. **BMI Calculation**:
   - The program uses the formula:
     ```
     BMI = weight / (height^2)
     ```
   - It categorizes the BMI result into:
     - Underweight: BMI < 18.5
     - Normal weight: 18.5 ≤ BMI < 24.9
     - Overweight: 25 ≤ BMI < 29.9
     - Obesity: BMI ≥ 30

2. **Caloric Needs Calculation**:
   - The program calculates the Basal Metabolic Rate (BMR) using the Mifflin-St Jeor equation:
     - For males:
       ```
       BMR = (10 × weight (kg)) + (6.25 × height (cm)) - (5 × age (years)) + 5
       ```
     - For females:
       ```
       BMR = (10 × weight (kg)) + (6.25 × height (cm)) - (5 × age (years)) - 161
       ```
   - BMR is then multiplied by an activity multiplier based on the user’s activity level:
     - Sedentary: BMR × 1.2
     - Lightly active: BMR × 1.375
     - Moderately active: BMR × 1.55
     - Very active: BMR × 1.725
     - Super active: BMR × 1.9

### User Input

The program prompts the user for:
- Weight (in kg or lb)
- Height (in meters or inches)
- Age (in years)
- Gender (male/female)
- Activity level (from a predefined list)

### Example Output

After entering the required information, the program provides:
- The calculated BMI and its category.
- The estimated daily caloric needs to maintain current weight.

## Getting Started

### Requirements

- Python 3.x

### How to Run

1. In a command line:
   ```bash
   python bmi_caloric_needs.py