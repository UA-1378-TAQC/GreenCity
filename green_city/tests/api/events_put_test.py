import json

import pytest
import requests
from jsonschema import validate
from green_city.src.config import API_BASE_URL_8085


def updated_event_payload(event_id):
    return {
        "id": event_id,
        "title": "Updated Event Title",
        "description": "Updated Description",
        "datesLocations": [
            {
                "startDate": "2033-05-27T15:00:00Z",
                "finishDate": "2033-05-27T17:00:00Z",
                "onlineLink": "http://test.example.com"
            }
        ],
        "tags": ["Social"],
        "open": True
    }


def test_update_event_by_id_success(create_and_cleanup_event, auth_token, test_event_json_schema):
    event_id = create_and_cleanup_event
    payload = updated_event_payload(event_id)

    response = requests.put(
        f"{API_BASE_URL_8085}/events/{event_id}",
        headers={"Authorization": auth_token},
        files={"eventDto": (None, json.dumps(payload), "application/json")}
    )

    assert response.status_code == 200
    data = response.json()
    validate(instance=data, schema=test_event_json_schema)
    assert data["id"] == event_id
    assert data["title"] == payload["title"]


def test_update_event_by_id_not_found(auth_token):
    non_existing_id = -1
    payload = updated_event_payload(non_existing_id)

    response = requests.put(
        f"{API_BASE_URL_8085}/events/{non_existing_id}",
        headers={"Authorization": auth_token},
        files={"eventDto": (None, json.dumps(payload), "application/json")}
    )

    assert response.status_code == 404
    assert response.json()["message"] == "Event hasn't been found"


def test_update_event_by_id_invalid_id(auth_token):
    payload = updated_event_payload(123)

    response = requests.put(
        f"{API_BASE_URL_8085}/events/invalid_id",
        headers={"Authorization": auth_token},
        files={"eventDto": (None, json.dumps(payload), "application/json")}
    )

    assert response.status_code == 400
    assert response.json()["message"] == "Wrong eventId. Should be 'Long'"


def test_update_event_by_id_unauthorized(create_and_cleanup_event):
    event_id = create_and_cleanup_event
    payload = updated_event_payload(event_id)

    response = requests.put(
        f"{API_BASE_URL_8085}/events/{event_id}",
        files={"eventDto": (None, json.dumps(payload), "application/json")}
    )

    assert response.status_code == 401
    assert response.json()["error"] == "Unauthorized"