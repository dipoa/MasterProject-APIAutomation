import requests
from config import BASE_URL

# BASE_URL = "https://restful-booker.herokuapp.com"

def create_booking(payload):
    """
    Make a POST request to create a booking and return the response.
    """
    endpoint = f"{BASE_URL}/booking"
    response = requests.post(endpoint, json=payload)
    response.raise_for_status()  # Ensure the request was successful
    return response.json()
