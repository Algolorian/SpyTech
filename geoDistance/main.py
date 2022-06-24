from geopy.distance import geodesic

first_place = (52.6165651, 21.5115684)
second_place = (52.4165651, 16.5115684)

distance = geodesic(first_place, second_place).mi

print("miles:", distance)
