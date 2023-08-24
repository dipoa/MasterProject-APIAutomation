import pytest
from pytest_steps import test_steps
from steps.update_booking_step import update_booking
# from test_create_booking import BOOKING_ID

# BOOKING_ID = 1  # This can be dynamically set based on previous test results or other factors

PAYLOAD = {
    "firstname": "Dipo",
    "lastname": "Anugrah",
    "totalprice": 1000,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2023-06-06",
        "checkout": "2024-01-01"
    },
    "additionalneeds": "Full Meal"
}

@pytest.mark.usefixtures("created_booking_id")
@test_steps('update_booking', 'validate_updated_booking')
def test_suite(created_booking_id):
    
    # Step 1: Update Booking
    # def update_booking_step(step_results):
    data = update_booking(created_booking_id, PAYLOAD)
    # return {'updated_data': data}
    yield 'update_booking'

    # Step 2: Validate Updated Booking
    # def validate_updated_booking(step_results):
    print(data)
    response_data = data
    assert response_data["firstname"] == PAYLOAD["firstname"], "Firstname does not match expected value"
    assert response_data["lastname"] == PAYLOAD["lastname"], "Lastname does not match expected value"
    assert response_data["totalprice"] == PAYLOAD["totalprice"], "Total price does not match expected value"
    assert response_data["depositpaid"] == PAYLOAD["depositpaid"], "Deposit paid value does not match expected value"
    assert response_data["bookingdates"]["checkin"] == PAYLOAD["bookingdates"]["checkin"], "Checkin date does not match expected value"
    assert response_data["bookingdates"]["checkout"] == PAYLOAD["bookingdates"]["checkout"], "Checkout date does not match expected value"
    assert response_data["additionalneeds"] == PAYLOAD["additionalneeds"], "Additional needs do not match expected value"

    yield 'validate_updated_booking'
