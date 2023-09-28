import pytest
import requests
from pytest_steps import test_steps
from steps.delete_booking_step import delete_booking
from config import BASE_URL

@pytest.mark.usefixtures("created_booking")
@test_steps('delete_booking', 'validate_deletion')
def test_suite(created_booking):
    
    # Step 1: Delete Booking
    booking_id = created_booking['bookingid']
    response = delete_booking(booking_id)
    assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"
    yield 'delete_booking'
    
    # Step 2: Validate Deletion
    response = requests.get(f"{BASE_URL}/booking/{booking_id}")
    assert response.status_code == 404, "Booking still exists, expected status code 404 but got {}".format(response.status_code)
    yield 'validate_deletion'
    