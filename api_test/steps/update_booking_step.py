import requests
from config import BASE_URL, AUTH_TOKEN

def update_booking(booking_id, payload):
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Basic {AUTH_TOKEN}"
    }

    response = requests.put(f"{BASE_URL}/booking/{booking_id}", json=payload, headers=headers)
    response.raise_for_status()  # Raise an exception for HTTP errors

    return response.json()
