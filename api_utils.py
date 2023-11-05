import requests

BASE_URL = "http://localhost:4800"

def registra_problema(data,file):
    try:
        response = requests.post(f"{BASE_URL}/problemas",data=data,files=file)
        response.raise_for_status()
        return True, response.json()
    except Exception as e:
        return False, {"message": str(e)}