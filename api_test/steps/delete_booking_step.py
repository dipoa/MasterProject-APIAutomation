import requests
from config import BASE_URL, AUTH_TOKEN

def delete_booking(booking_id):
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Basic {AUTH_TOKEN}"
    }

    response = requests.delete(f"{BASE_URL}/booking/{booking_id}", headers=headers)
    response.raise_for_status()  # Raise an exception for HTTP errors

    return response
