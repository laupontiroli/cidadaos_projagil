import requests

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