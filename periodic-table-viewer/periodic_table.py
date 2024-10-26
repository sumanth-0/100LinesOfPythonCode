import requests

def get_element_info(symbol_or_number):
    # Define the API URL
    url = f"https://periodic-table-api.herokuapp.com/element/{symbol_or_number}"
    
    try:
        response = requests.get(url)

        if response.status_code == 200:
            # Return the element data as a dictionary
            return response.json()
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def display_element(element):
    if element:
        print(f"Element: {element['name']}")
        print(f"Symbol: {element['symbol']}")
        print(f"Atomic Number: {element['atomicNumber']}")
        print(f"Atomic Mass: {element['atomicMass']}")
        print(f"Group: {element['group']}")
        print(f"Period: {element['period']}")
        print(f"Density: {element['density']}")
        print(f"Melting Point: {element['meltingPoint']}")
        print(f"Boiling Point: {element['boilingPoint']}\n")
    else:
        print("Element not found or invalid input.")

def main():
    print("Welcome to the Periodic Table Information Program!")
    user_input = input("Enter an atomic number or symbol (e.g., 'H' or '1'): ")
    element = get_element_info(user_input)
    display_element(element)

if __name__ == "__main__":
    main()
