import requests
from jsonschema.validators import validate

from green_city.config.config import API_BASE_URL_8085
from green_city.data.schema.event_schema import EVENT_201


def test_get_event_by_id_success(create_event, auth_token):
    event_id = create_event.get("id")

    response = requests.get(
        f"{API_BASE_URL_8085}/events/{event_id}",
        headers={"Authorization": auth_token}
    )
    data = response.json()

    assert response.status_code == 200
    validate(instance=data, schema=EVENT_201)
    assert (data.get("id") == event_id), f"Expected event ID {event_id}, got {data.get('id')}"


def test_get_event_by_id_invalid_id():
    url = f"{API_BASE_URL_8085}/events/-1"
    response = requests.get(url)

    expected_response = {
        "message": "Event hasn't been found"
    }

    assert response.status_code == 404, f"Expected 404, got {response.status_code}"
    assert response.json() == expected_response, f"Expected {expected_response}, got {response.json()}"


def test_get_event_by_id_bad_request():
    url = f"{API_BASE_URL_8085}/events/hi"
    response = requests.get(url)

    expected_response = {
        "message": "Wrong eventId. Should be 'Long'"
    }

    assert response.status_code == 400, f"Expected 400, got {response.status_code}"
    assert response.json() == expected_response, f"Expected {expected_response}, got {response.json()}"
