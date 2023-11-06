import requests
from geopy.geocoders import Nominatim


# teste usando o geopy, coders pra achar latitude e longitude pro bubblemap 

def give_lat_lon(rua,bairro):
    geolocator = Nominatim(user_agent="teste")

    geocode = lambda query, **kw: geolocator.geocode("%s Sao Paulo" % query, **kw)

    result = geocode(f'{rua},{bairro}',language="pt-BR")

    return result.latitude,result.longitude


BASE_URL = "http://localhost:4800"

def registra_problema(data,file):
    try:
        response = requests.post(f"{BASE_URL}/problemas",data=data,files=file)
        response.raise_for_status()
        return True, response.json()
    except Exception as e:
        return False, {"message": str(e)}
    
def get_problema_id(id):
    try:
        json = {"_id":str(id)}
        response = requests.get(f"{BASE_URL}/problemas/filter",json=json)
        response.raise_for_status()
        return True, response.json()
    except Exception as e:
        return False, {"message": str(e)}