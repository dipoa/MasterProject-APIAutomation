import pytest
from pytest_steps import test_steps
from steps.create_booking_step import create_booking

@test_steps('post_booking_data', 'validate_response_data')
def test_suite():
    
    # Payload for booking
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
    
    # Step 1: Post booking data
    response_data = create_booking(payload)
    # print(data)
    yield 'post_booking_data'
    
    # Step 2: Validate response data
    print(response_data)
    assert isinstance(response_data["bookingid"],int), "Booking ID is not an integer"
    assert response_data["booking"]["firstname"] == payload["firstname"], "Firstname does not match expected value"
    assert response_data["booking"]["lastname"] == payload["lastname"], "Lastname does not match expected value"
    assert response_data["booking"]["totalprice"] == payload["totalprice"], "Total price does not match expected value"
    assert response_data["booking"]["depositpaid"] == payload["depositpaid"], "Deposit paid value does not match expected value"
    assert response_data["booking"]["bookingdates"]["checkin"] == payload["bookingdates"]["checkin"], "Checkin date does not match expected value"
    assert response_data["booking"]["bookingdates"]["checkout"] == payload["bookingdates"]["checkout"], "Checkout date does not match expected value"
    assert response_data["booking"]["additionalneeds"] == payload["additionalneeds"], "Additional needs do not match expected value"

    yield 'validate_response_data'
