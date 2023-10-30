from geopy.geocoders import Nominatim


# teste usando o geopy, coders pra achar latitude e longitude 
geolocator = Nominatim(user_agent="teste")

result = geolocator.geocode('Avenida Paulista, Cerqueira Cesar Sao Paulo')

print(result.latitude,result.longitude)

location = geolocator.reverse(f'{result.latitude},{result.longitude}')

print(location.address)