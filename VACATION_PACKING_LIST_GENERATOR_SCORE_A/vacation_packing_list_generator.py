
# Vacation Packing List Generator

def generate_packing_list(location, season, trip_length):
    packing_list = []

    if location.lower() == "beach":
        packing_list.extend(["Swimsuit", "Sunscreen", "Beach Towel"])
        if season.lower() == "winter":
            packing_list.append("Light Jacket")
    elif location.lower() == "city":
        packing_list.extend(["Comfortable Shoes", "Sunglasses"])
        if season.lower() == "summer":
            packing_list.append("Light Clothes")
        elif season.lower() == "winter":
            packing_list.append("Warm Clothes")

    packing_list.append(f"Number of Outfits: {trip_length}")

    return packing_list

def main():
    location = input("Enter your vacation location (e.g., beach, city): ")
    season = input("Enter the season of your trip (e.g., summer, winter): ")
    trip_length = int(input("Enter the number of days for your trip: "))

    packing_list = generate_packing_list(location, season, trip_length)
    
    print("\nSuggested Packing List:")
    for item in packing_list:
        print("- " + item)

if __name__ == "__main__":
    main()
