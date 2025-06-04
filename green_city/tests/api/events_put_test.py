import json

import pytest
import requests
from jsonschema import validate

from green_city.config.config import API_BASE_URL_8085
from green_city.data.fixture_dto.create_event_dto_request import update_event_dto_request
from green_city.data.schema.event_schema import EVENT_201


def test_update_event_by_id_success(create_event, auth_token):
    event_id =create_event.get("id")
    payload = update_event_dto_request(event_id)

    response = requests.put(
        f"{API_BASE_URL_8085}/events/{event_id}",
        headers={"Authorization": auth_token},
        files={"eventDto": (None, json.dumps(payload), "application/json")}
    )

    assert response.status_code == 200
    data = response.json()
    validate(instance=data, schema=EVENT_201)
    assert(data.get("id") == event_id), f"Expected event ID {event_id}, got {data.get('id')}"

def test_update_event_by_id_not_found(auth_token):
    non_existing_id = -1
    payload = update_event_dto_request(non_existing_id)

    response = requests.put(
        f"{API_BASE_URL_8085}/events/{non_existing_id}",
        headers={"Authorization": auth_token},
        files={"eventDto": (None, json.dumps(payload), "application/json")}
    )

    assert response.status_code == 404
    assert response.json()["message"] == "Event hasn't been found"


def test_update_event_by_id_invalid_id(auth_token):
    payload = update_event_dto_request(123)

    response = requests.put(
        f"{API_BASE_URL_8085}/events/invalid_id",
        headers={"Authorization": auth_token},
        files={"eventDto": (None, json.dumps(payload), "application/json")}
    )

    assert response.status_code == 400
    assert response.json()["message"] == "Wrong eventId. Should be 'Long'"


def test_update_event_by_id_unauthorized(create_event):
    event_id = create_event.get("id")
    payload = update_event_dto_request(event_id)

    response = requests.put(
        f"{API_BASE_URL_8085}/events/{event_id}",
        files={"eventDto": (None, json.dumps(payload), "application/json")}
    )

    assert response.status_code == 401
    assert response.json()["error"] == "Unauthorized"