from datetime import datetime
import pytz

def convert_timezones(timezone_from, timezone_to):
    """
    Converts the current time from one timezone to another.
    
    Parameters:
    - timezone_from (str): The source timezone.
    - timezone_to (str): The target timezone.
    
    Returns:
    - str: The converted time as a string.
    """
    # Get the current time in the source timezone
    local_time = datetime.now(pytz.timezone(timezone_from))
    
    # Convert to the target timezone
    target_time = local_time.astimezone(pytz.timezone(timezone_to))
    
    return target_time.strftime('%Y-%m-%d %H:%M:%S')

def main():
    print("Welcome to the World Time Converter!")
    
    # List available timezones
    timezones = pytz.all_timezones
    print("Available timezones:")
    for tz in timezones:
        print(tz)
    
    # User input for timezones
    timezone_from = input("Enter the timezone to convert from: ")
    timezone_to = input("Enter the timezone to convert to: ")
    
    # Convert time and display results
    converted_time = convert_timezones(timezone_from, timezone_to)
    print(f"\nCurrent time in {timezone_from}: {datetime.now(pytz.timezone(timezone_from)).strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Current time in {timezone_to}: {converted_time}")

# Run the time converter
if __name__ == "__main__":
    main()
