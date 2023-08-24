import requests

BASE_URL = "https://restful-booker.herokuapp.com"

def get_auth_token():
    endpoint = "/auth"
    data = {
        "username": "admin",
        "password": "password123"
    }
    
    response = requests.post(f"{BASE_URL}{endpoint}", json=data)
    
    # Ensure a successful response before proceeding.
    response.raise_for_status()

    return response.json().get('token', None)

# Generate the token once when the module is imported.
AUTH_TOKEN = "YWRtaW46cGFzc3dvcmQxMjM="