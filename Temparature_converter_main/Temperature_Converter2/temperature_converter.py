def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return celsius_to_kelvin(fahrenheit_to_celsius(f))

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return celsius_to_fahrenheit(kelvin_to_celsius(k))

def convert_temperature(value, from_unit, to_unit):
    conversions = {
        ('C', 'F'): celsius_to_fahrenheit,
        ('C', 'K'): celsius_to_kelvin,
        ('F', 'C'): fahrenheit_to_celsius,
        ('F', 'K'): fahrenheit_to_kelvin,
        ('K', 'C'): kelvin_to_celsius,
        ('K', 'F'): kelvin_to_fahrenheit,
    }

    try:
        return conversions[(from_unit, to_unit)](value)
    except KeyError:
        return None

def main():
    print("Temperature Converter")
    print("Units: C = Celsius, F = Fahrenheit, K = Kelvin")
    
    value = float(input("Enter the temperature value: "))
    from_unit = input("From unit (C/F/K): ").strip().upper()

    # Restrict output options based on input unit
    to_unit_options = {'C': ['F', 'K'], 'F': ['C', 'K'], 'K': ['C', 'F']}
    if from_unit in to_unit_options:
        to_unit = input(f"Convert to ({'/'.join(to_unit_options[from_unit])}): ").strip().upper()
        while to_unit not in to_unit_options[from_unit]:
            print(f"Invalid choice. Choose only {', '.join(to_unit_options[from_unit])}.")
            to_unit = input(f"Convert to ({'/'.join(to_unit_options[from_unit])}): ").strip().upper()
    else:
        print("Invalid unit entered.")
        return

    result = convert_temperature(value, from_unit, to_unit)
    
    if result is not None:
        print(f"{value} {from_unit} is {result:.2f} {to_unit}.")
    else:
        print("Conversion error.")

if __name__ == "__main__":
    main()
