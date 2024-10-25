from datetime import datetime


def calculate_age(birthdate):
    """
    Calculate age from birthdate.

    Args:
        birthdate: Date in format 'YYYY-MM-DD'

    Returns:
        tuple: (years, months, days)
    """
    # Convert birthdate string to datetime object
    birth_date = datetime.strptime(birthdate, '%Y-%m-%d')

    # Get current date
    current_date = datetime.now()

    # Calculate age
    years = current_date.year - birth_date.year
    months = current_date.month - birth_date.month
    days = current_date.day - birth_date.day

    # Adjust years and months if needed
    if days < 0:
        months -= 1
        days += 30  # Approximate days in a month

    if months < 0:
        years -= 1
        months += 12

    return years, months, days


def main():
    try:
        # Get birthdate from user
        print("Please enter your birthdate (YYYY-MM-DD):")
        birthdate = input()

        # Calculate and display age
        years, months, days = calculate_age(birthdate)

        print(f"\nYour age is:")
        print(f"{years} years, {months} months, and {days} days")

    except ValueError:
        print("Invalid date format! Please use YYYY-MM-DD format.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()