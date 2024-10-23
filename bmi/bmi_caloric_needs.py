def calculate_bmi(weight, height):
    return weight / (height ** 2)

def get_weight():
    unit = input("Choose weight unit (kg/lb): ").strip().lower()
    if unit == "kg":
        weight = float(input("Enter your weight in kg: "))
    elif unit == "lb":
        weight = float(input("Enter your weight in lb: "))
        weight = weight / 2.205#Convert to kg
    else:
        print("Invalid unit. Please restart.")
        exit()
    return weight

def get_height():
    unit = input("Choose height unit (m/in): ").strip().lower()
    if unit == "m":
        height = float(input("Enter your height in meters: "))
    elif unit == "in":
        height = float(input("Enter your height in inches: "))
        height = height * 0.0254#Convert to meters
    else:
        print("Invalid unit. Please restart.")
        exit()
    return height

def get_activity_level():
    print("\nChoose your activity level:\n")
    print("\t1: Sedentary (little or no exercise)")
    print("\t2: Lightly active (light exercise/sports 1-3 days a week)")
    print("\t3: Moderately active (moderate exercise/sports 3-5 days a week)")
    print("\t4: Very active (hard exercise/sports 6-7 days a week)")
    print("\t5: Super active (very hard exercise, physical job or training twice a day)")
    level = int(input("\nEnter the number corresponding to your activity level: "))
    return level

#Calculating daily calorie needs with basal metabolic rate equation, based on age and gender
def calculate_caloric_needs(weight, height, age, gender, activity_level):
    if gender == "male":
        bmr = 10 * weight + 6.25 * height * 100 - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height * 100 - 5 * age - 161
    activity_multipliers = [1.2, 1.375, 1.55, 1.725, 1.9]
    return bmr * activity_multipliers[activity_level - 1]

weight = get_weight()
height = get_height()
age = int(input("Enter your age in years: "))
gender = input("Enter your gender (male/female): ").strip().lower()
activity_level = get_activity_level()
bmi = calculate_bmi(weight, height)

if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 24.9:
    category = "Normal weight"
elif 25 <= bmi < 29.9:
    category = "Overweight"
else:
    category = "Obesity"

caloric_needs = calculate_caloric_needs(weight, height, age, gender, activity_level)

print(f"\nYour BMI is {bmi:.2f}. Category: {category}")
print(f"Your daily caloric needs to maintain your weight: {caloric_needs:.2f} calories.")
