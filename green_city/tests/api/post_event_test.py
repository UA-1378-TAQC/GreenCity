import json

import pytest
import requests
from jsonschema import validate
from green_city.tests.data.schema.event_schema import EVENT_SCHEMA
from green_city.src.config import API_BASE_URL_8085, ENDPOINTS
from green_city.tests.data.fixture_dto.create_event_dto_request import create_event_dto_request
import green_city.src.util.logging_config
import logging

logger = logging.getLogger(__name__)

def test_create_event_returns_201(auth_token):
    dto_request_str = json.dumps(create_event_dto_request)
    response = requests.post(
        f"{API_BASE_URL_8085}{ENDPOINTS['events']}",
        headers={"Authorization": auth_token},
        files={
        'addEventDtoRequest': (None, dto_request_str)

    })

    assert response.status_code == 201
    assert response.headers['Content-Type'] == 'application/json'

    event_json = response.json()
    validate(instance=event_json, schema=EVENT_SCHEMA)



