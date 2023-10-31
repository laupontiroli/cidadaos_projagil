import requests

BASE_URL = "http://localhost:5000"

def registra_problema(data,file):
    try:
        response = requests.get(f"{BASE_URL}/problema",data=data,files=file)
        response.raise_for_status()
        return True, response.json()
    except Exception as e:
        return False, {"message": str(e)}