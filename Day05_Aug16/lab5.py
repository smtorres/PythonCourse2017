# pip install googlemaps
from googlemaps import Client
from datetime import datetime


api_key = 'yourkey'
gmaps = Client(api_key)
dir(gmaps)
whitehouse = '1600 Pennsylvania Avenue, Washington, DC'
whitehouse_geoloc = gmaps.geocode(whitehouse)
print whitehouse_geoloc

destination = gmaps.reverse_geocode((38.897096, -77.036545))
print destination

now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)

lat_long = (gmaps.geocode('326 Perkins Library, Durham, NC 27708')[0]['geometry']['location']['lat'], gmaps.geocode('326 Perkins Library, Durham, NC 27708')[0]['geometry']['location']['lng'])
print lat_long
duke = gmaps.reverse_geocode(lat_long)[0]['formatted_address']
print duke 

local = gmaps.places('restaurant near ' + duke)
print local['results'][0]['formatted_address']
print local['results'][0]['name']

directions = gmaps.directions(duke, whitehouse)
print directions[0]['legs'][0]['distance']

for step in directions[0]['legs'][0]['steps']:
	print step['html_instructions']

embassies = [[38.917228,-77.0522365], 
	[38.9076502, -77.0370427], 
	[38.916944, -77.048739] ]

# TODO: write code to answer the following questions: 
# which embassy is closest to the White House in meters? how far? 
# what is its address? 
# if I wanted to hold a morning meeting there, which cafe would you suggest?
# if I wanted to hold an evening meeting there, which bar would you suggest? 

