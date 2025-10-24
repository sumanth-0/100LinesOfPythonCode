from countryinfo import CountryInfo

def main():
    while True:
        # Remove leading and trailing whitespaces
        your_country = input("\nEnter country (or type 'exit' to quit): ").strip()

        # Exit condition
        if your_country.lower() == 'exit':
            print("Goodbye!")
            break

        # Check if the input is empty
        if not your_country:
            print("No input detected. Please enter a country name.")
            continue  # Ask again

        try:
            country = CountryInfo(your_country)

            # Display country information
            print("Capital:", country.capital())
            print("Population:", country.population())
            print("Currency:", country.currencies())
            print("Languages:", country.languages())
            print("Borders:", country.borders())
            print("Provinces:", country.provinces())
            print("Area:", country.area())
            print("Calling Codes:", country.calling_codes())
            print("Capital Lat/Long:", country.capital_latlng())
            print("Timezones:", country.timezones())
            print("Alternative Names:", country.alt_spellings())

        except KeyError:
            print("❌ Country not found. Please check your spelling.")
        except Exception as e:
            print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    main()
