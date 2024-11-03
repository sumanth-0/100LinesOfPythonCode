import folium
import geopandas as gpd

# Load world map data
world_map = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Create an interactive map centered on the world
m = folium.Map(location=[0, 0], zoom_start=2)

# Function to add a marker to the map
def add_marker(lat, lon, popup_text):
    folium.Marker([lat, lon], popup=popup_text).add_to(m)

# Quiz loop
while True:
    country = input("Enter a country name: ")
    if country.lower() == 'quit':
        break

    # Find the country in the GeoDataFrame
    country_data = world_map[world_map['name'] == country]

    if not country_data.empty:
        # Get the latitude and longitude of the country's capital
        capital_lat = country_data['capital_lat'].values[0]
        capital_lon = country_data['capital_lon'].values[0]

        # Add a marker to the map
        add_marker(capital_lat, capital_lon, country_data['name'].values[0])

        # Prompt the user to guess the capital
        capital_guess = input("Guess the capital of {}: ".format(country))

        # Check if the guess is correct
        if capital_guess.lower() == country_data['capital'].values[0].lower():
            print("Correct!")
        else:
            print("Incorrect. The capital is {}.".format(country_data['capital'].values[0]))
    else:
        print("Country not found.")

# Display the map
m.save('world_map_quiz.html')
print("Quiz complete. Check the 'world_map_quiz.html' file.")
