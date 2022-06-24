import phonenumbers
import folium
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode

key = '6c88f3edf15448a582a99183d722b39c'

number = phonenumbers.parse('+17206018844')
location = geocoder.description_for_number(number, "en")
carrier = carrier.name_for_number(number, "en")

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)
myMap.save("mylocation.html")

print(results)
