import pytest
import requests
from jsonschema.validators import validate

from green_city.src.config import API_BASE_URL_8085

def test_get_event_by_id_success(create_and_cleanup_event, test_event_json, test_event_json_schema, auth_token):
    event_id = create_and_cleanup_event

    response = requests.get(
        f"{API_BASE_URL_8085}/events/{event_id}",
        headers={"Authorization": auth_token}
    )

    assert response.status_code == 200

    data = response.json()

    validate(instance=data, schema=test_event_json_schema)

    assert data["id"] == event_id
    assert data["title"] == test_event_json["title"]

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