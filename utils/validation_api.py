from ControlUp.utils.http_enums import HttpStatusCode, HttpMethod



def validate_status_code(response, expected_status: HttpStatusCode, message):
        assert response.status_code == expected_status.value, (
            f"Expected status code {expected_status.value}, "
            f"but got {response.status_code}."
            f"message: {message}"
        )

def validate_airport_count(response, count = 30):
    data = response.json()
    assert len(data["data"]) == count, "Airport count mismatch"

def validate_airport_name(response, airport_name):
    data = response.json()

    # using set to get O(1) time complexity
    all_airports_name = {airport["attributes"]["name"] for airport in data["data"]}

    assert airport_name in all_airports_name,  "Airport name mismatch"

def validate_airport_distance(response, minimum_distance):
    data = response.json()
    distance = data.get("data").get("attributes").get("kilometers")
    assert distance > minimum_distance, f"Expected distance > {minimum_distance} km, but got {distance} km"


