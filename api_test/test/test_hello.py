import pytest
from pytest_steps import test_steps
from steps.get_booking_step import get_booking

BOOKING_ID = 1

@test_steps('fetch_booking')
def test_fetch_booking():
    data = get_booking(BOOKING_ID)
    print(data)
    yield 'fetch_booking'
