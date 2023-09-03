import pytest
from pytest_steps import test_steps
from steps.update_booking_step import partial_update_booking
# from test_create_booking import BOOKING_ID

# BOOKING_ID = 1  # This can be dynamically set based on previous test results or other factors

PAYLOAD = {
    "firstname": "Max",
    "lastname": "Karl",
    "totalprice": 15000,
    "additionalneeds": "Non Smoking Room"
}

@pytest.mark.usefixtures("created_booking")
@test_steps('update_booking', 'validate_updated_booking')
def test_suite(created_booking):
    
    # Step 1: Update Booking
    booking_id=created_booking["bookingid"]
    data = partial_update_booking(booking_id, PAYLOAD)
    # return {'updated_data': data}
    yield 'update_booking'

    # Step 2: Validate Updated Booking
    # def validate_updated_booking(step_results):
    print(data)
    response_data = data
    assert response_data["firstname"] == PAYLOAD["firstname"], "Firstname does not match expected value"
    assert response_data["lastname"] == PAYLOAD["lastname"], "Lastname does not match expected value"
    assert response_data["totalprice"] == PAYLOAD["totalprice"], "Total price does not match expected value"
    assert response_data["depositpaid"] == created_booking["booking"]["depositpaid"], "Deposit paid value does not match expected value"
    assert response_data["bookingdates"]["checkin"] == created_booking["booking"]["bookingdates"]["checkin"], "Checkin date does not match expected value"
    assert response_data["bookingdates"]["checkout"] == created_booking["booking"]["bookingdates"]["checkout"], "Checkout date does not match expected value"
    assert response_data["additionalneeds"] == PAYLOAD["additionalneeds"], "Additional needs do not match expected value"

    yield 'validate_updated_booking'
