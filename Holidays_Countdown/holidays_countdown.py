from datetime import datetime

def days_until_holiday(target_date):
    # Get today's date
    today = datetime.now().date()
    
    # Calculate the difference in days
    delta = (target_date - today).days
    
    # Return the number of days
    return delta

# Dictionary of major fixed-date holidays
holidays = {
    "New Year's Day": datetime(datetime.now().year + 1, 1, 1).date(),
    "Republic Day (India)": datetime(datetime.now().year, 1, 26).date(),
    "Valentine's Day": datetime(datetime.now().year, 2, 14).date(),
    "Women's Day": datetime(datetime.now().year, 3, 8).date(),
    "St. Patrick's Day": datetime(datetime.now().year, 3, 17).date(),
    "April Fool's Day": datetime(datetime.now().year, 4, 1).date(),
    "Labor Day": datetime(datetime.now().year, 5, 1).date(),
    "Mother's Day (Mexico)": datetime(datetime.now().year, 5, 10).date(),
    "Flag Day (US)": datetime(datetime.now().year, 6, 14).date(),
    "Independence Day (US)": datetime(datetime.now().year, 7, 4).date(),
    "Bastille Day (France)": datetime(datetime.now().year, 7, 14).date(),
    "Friendship Day": datetime(datetime.now().year, 8, 1).date(),
    "Independence Day (India)": datetime(datetime.now().year, 8, 15).date(),
    "National Dog Day": datetime(datetime.now().year, 8, 26).date(),
    "Teachers' Day (India)": datetime(datetime.now().year, 9, 5).date(),
    "Independence Day (Mexico)": datetime(datetime.now().year, 9, 16).date(),
    "Chinese National Day": datetime(datetime.now().year, 10, 1).date(),
    "Thanksgiving (Canada)": datetime(datetime.now().year, 10, 9).date(),
    "Halloween": datetime(datetime.now().year, 10, 31).date(),
    "Veterans Day (US)": datetime(datetime.now().year, 11, 11).date(),
    "Armistice Day (France)": datetime(datetime.now().year, 11, 11).date(),
    "Children's Day (India)": datetime(datetime.now().year, 11, 14).date(),
    "Constitution Day (Japan)": datetime(datetime.now().year, 11, 23).date(),
    "Thanksgiving (Japan)": datetime(datetime.now().year, 11, 23).date(),
    "Christmas": datetime(datetime.now().year, 12, 25).date(),
    "Boxing Day": datetime(datetime.now().year, 12, 26).date(),
    "Kwanzaa": datetime(datetime.now().year, 12, 26).date(),
    "New Year's Eve": datetime(datetime.now().year, 12, 31).date(),
}

# Display the countdown for each holiday
for holiday, date in holidays.items():
    days_left = days_until_holiday(date)
    
    # Adjust for holidays that already passed this year
    if days_left < 0:
        date = datetime(datetime.now().year + 1, date.month, date.day).date()
        days_left = days_until_holiday(date)
    
    print(f"{holiday} is in {days_left} days!")
