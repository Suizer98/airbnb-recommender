import folium
from suggest import suggest
from IPython.display import display

options = [
    "Holiday/ Rest & Relax",
    "General business purpose",
    "Sightseeing/ Attractions",
    "General business purpose",
    "IR (e.g. MBS, RWS)",
    "Sightseeing/ Attractions",
    "To shop/attend shopping events in Singapore",
    "Exhibition/Trade show",
    "Company sponsored holiday",
    "To experience different cultures",
    "Cultural Festivals",
    "Family Entertainment",
    "To experience different cultures",
    "To experience the food/food events in Singapore",
    "To experience the nightlife in Singapore",
]

nearest_airbnb_listings, destinations = suggest(options[0])
print(nearest_airbnb_listings)
print(destinations)

# Create a Folium map centered around the first destination
map_center = [destinations.iloc[0]["latitude"], destinations.iloc[0]["longitude"]]
map_destination = folium.Map(location=map_center, zoom_start=15)

# Add markers for all destinations with a different color and icon
for index, destination in destinations.iterrows():
    folium.Marker(
        location=[destination["latitude"], destination["longitude"]],
        popup=destination["Name"],
        icon=folium.Icon(color="red", icon="star"),
    ).add_to(map_destination)

# Add markers for the nearest Airbnb listings with a different color and icon
for index, row in nearest_airbnb_listings.iterrows():
    folium.Marker(
        location=[row["latitude"], row["longitude"]],
        popup=row["name"],
        icon=folium.Icon(color="blue", icon="home"),
    ).add_to(map_destination)

# Display the map directly in the notebook
display(map_destination)
