import sys  # Add this if you're using exit()

measurement_type = input("Input your measurement type (Imperial / Metric) >> ")

try:
    if measurement_type == "Metric":
        weight = float(input("Input your weight (In Kilogram) >> "))
        height = float(input("Input your height (in Meter) >> "))
    
    elif measurement_type == "Imperial":
        weight = float(input("Input your weight (In Pounds) >> "))
        height = float(input("Input your height (in Inches) >> "))
        
        weight = weight * 0.453592  # Convert pounds to kilograms
        height = height * 0.0254    # Convert inches to meters
    
    else:
        print("Invalid measurement type!")
        sys.exit()  # Use sys.exit() to exit the program

    bmi = weight / (height ** 2)  # Calculate BMI
    
    # Determine BMI category
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    # Output BMI and category
    print(f"Your BMI is {bmi:.2f}")
    print(f"You are classified as: {category}")

except ValueError:
    print("Invalid input! Please enter numeric values for weight and height.")
