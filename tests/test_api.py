import requests
import pytest

from ControlUp.utils.config import END_POINT_AIRPORTS, END_POINT_AIRPORT_DISTANCE
from ControlUp.utils.validation_api import validate_airport_count, validate_airport_name, validate_airport_distance
from ControlUp.utils.http_enums import HttpMethod
from tests.conftest import base_page


def test_verify_airport_count(base_page):
    response = base_page.safe_api_call(HttpMethod.GET, END_POINT_AIRPORTS)
    validate_airport_count(response)

@pytest.mark.parametrize(
    "airport",
    [
        "Akureyri Airport",
        "St. Anthony Airport",
        "CFB Bagotville"
    ]
)
def test_verify_specific_airports(base_page, airport):
    response = base_page.safe_api_call(HttpMethod.GET,END_POINT_AIRPORTS)
    validate_airport_name(response, airport)

@pytest.mark.parametrize(
    "payload, expected_minimum_distance",
    [
        ({"from": "KIX", "to": "NRT"}, 400)
    ]
)
def test_verify_distance_between_airports(base_page, payload, expected_minimum_distance):
    response = base_page.safe_api_call(HttpMethod.POST,END_POINT_AIRPORT_DISTANCE, json=payload)
    validate_airport_distance(response, expected_minimum_distance)






