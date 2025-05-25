import json
import pytest
import requests
from jsonschema import validate
from green_city.src.config import API_BASE_URL_8085, ENDPOINTS
from green_city.tests.data.fixture_dto.create_event_dto_request import create_event_dto_request
from green_city.tests.data.schema.event_schema import EVENT_SCHEMA
import green_city.src.util.logging_config
import logging

logger = logging.getLogger(__name__)

def test_create_event_returns_201(create_event):
    event_data = create_event

    validate(instance=event_data, schema=EVENT_SCHEMA)


def test_create_event_unauthorized_returns_401():

    url = f"{API_BASE_URL_8085}{ENDPOINTS['events']}"

    dto_request_str = json.dumps(create_event_dto_request)

    files = {
        'addEventDtoRequest': (None, dto_request_str),
        'image': (None, '')
    }

    response = requests.post(url, files=files)

    assert response.status_code == 401, (
        f"Expected status code 401, got {response.status_code}"
    )

    response_data = response.json()

    assert response_data['status'] == 401, "Status field should be 401"
    assert response_data['error'] == "Unauthorized", "Error field should be 'Unauthorized'"

    assert 'application/json' in response.headers['Content-Type'].lower(), (
        "Response should be in JSON format"
    )
