import requests

BASE_URL = "https://restful-booker.herokuapp.com/booking"

def get_booking(booking_id):
    response = requests.get(f"{BASE_URL}/{booking_id}")
    assert response.status_code == 200, f"Status code is not 200 for booking ID: {booking_id}"
    return response.json()  # return data for the next step