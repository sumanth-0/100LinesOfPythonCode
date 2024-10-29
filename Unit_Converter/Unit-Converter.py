def convert_temperature(temp, to_unit):
    if to_unit == 'F':
        return (temp * 9/5) + 32  # Celsius to Fahrenheit
    else:
        return (temp - 32) * 5/9  # Fahrenheit to Celsius

def convert_length(value, to_unit):
    if to_unit == 'ft':
        return value * 3.28084  # Meters to Feet
    else:
        return value / 3.28084  # Feet to Meters

def convert_distance(value, to_unit):
    if to_unit == 'mi':
        return value * 0.621371  # Kilometers to Miles
    else:
        return value / 0.621371  # Miles to Kilometers

def convert_weight(value, to_unit):
    if to_unit == 'lb':
        return value * 2.20462  # Kilograms to Pounds
    else:
        return value / 2.20462  # Pounds to Kilograms

def main():
    conversions = {
        '1': ('Celsius to Fahrenheit', '°C', '°F', 'temp', 'F'),
        '2': ('Fahrenheit to Celsius', '°F', '°C', 'temp', 'C'),
        '3': ('Meters to Feet', 'meters', 'feet', 'length', 'ft'),
        '4': ('Feet to Meters', 'feet', 'meters', 'length', 'm'),
        '5': ('Kilometers to Miles', 'kilometers', 'miles', 'distance', 'mi'),
        '6': ('Miles to Kilometers', 'miles', 'kilometers', 'distance', 'km'),
        '7': ('Kilograms to Pounds', 'kilograms', 'pounds', 'weight', 'lb'),
        '8': ('Pounds to Kilograms', 'pounds', 'kilograms', 'weight', 'kg')
    }

    print("Unit Converter")
    for key, value in conversions.items():
        print(f"{key}. {value[0]}")

    choice = input("Enter your choice (1-8): ")
    if choice in conversions:
        label = conversions[choice]
        value = float(input(f"Enter value in {label[1]}: "))

        if label[3] == 'temp':
            result = convert_temperature(value, label[4])
        elif label[3] == 'length':
            result = convert_length(value, label[4])
        elif label[3] == 'distance':
            result = convert_distance(value, label[4])
        elif label[3] == 'weight':
            result = convert_weight(value, label[4])

        print(f"{value} {label[1]} is {result} {label[2]}")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
