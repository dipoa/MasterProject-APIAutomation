import pytest
from pytest_steps import test_steps
from jsonschema import validate
from steps.get_booking_step import get_booking

BOOKING_ID = 1

@test_steps('fetch_booking', 'validate_response_data_types')
def test_suite():
    
    # Step 1: Fetch Booking
    data = get_booking(BOOKING_ID)
    # print(data)
    yield 'fetch_booking'
    
    # Step 2: Validate Response Data Types
    assert isinstance(data["firstname"], str), "Firstname is not a string"
    assert isinstance(data["lastname"], str), "Lastname is not a string"
    assert isinstance(data["totalprice"], int), "Total price is not an integer"
    assert isinstance(data["depositpaid"], bool), "Deposit paid value is not a boolean"
    assert isinstance(data["bookingdates"]["checkin"], str), "Checkin date is not a string"
    assert isinstance(data["bookingdates"]["checkout"], str), "Checkout date is not a string"
    # assert isinstance(data["additionalneeds"], str), "Additional needs is not a string"
    yield 'validate_response_data_types'
