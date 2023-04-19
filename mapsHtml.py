import gmaps
import googlemaps

apiKey = 'AIzaSyAGezmSgwpnLcivR3Ja-OyMo2PyJuLvT5c'

# Enter your Google Maps API key
gmaps.configure(api_key=apiKey)
google_maps = googlemaps.Client(key=apiKey)

# Enter the starting and ending locations for the route
start_loc = input("Please enter the starting location: ")
end_loc = input("Please enter the ending location: ")

# Get the directions for the route
directions = google_maps.directions(start_loc, end_loc, mode="driving", units="metric")

route_steps = [step['html_instructions'] for step in directions[0]['legs'][0]['steps']]


# Open a new HTML file
with open('route.html', 'w') as f:
    # Write the HTML headers
    f.write('<html><body><ol>')

    # Loop through each step and write the html_instructions to the file
    for step in route_steps:
        f.write('<li>' + step + '</li>')

    # Write the HTML footers
    f.write('</ol></body></html>')

print("All of the instructions have been printed onto the route.html file.")
