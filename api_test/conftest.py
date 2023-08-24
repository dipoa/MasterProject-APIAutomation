import pytest
from steps.create_booking_step import create_booking  # Import the function that sends the POST request

@pytest.fixture(scope="module")
def created_booking_id():
    payload = {
        "firstname": "Dipo",
        "lastname": "Supriadi",
        "totalprice": 500,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-01-01",
            "checkout": "2024-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = create_booking(payload)
    booking_id = response['bookingid']
    return booking_id
