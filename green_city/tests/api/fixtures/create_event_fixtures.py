import pytest
import requests
import json
from green_city.src.config import API_BASE_URL_8085, ENDPOINTS
from green_city.tests.data.fixture_dto.create_event_dto_request import create_event_dto_request
import green_city.src.util.logging_config
import logging

logger = logging.getLogger(__name__)

@pytest.fixture
def create_event(auth_token):
    url = f"{API_BASE_URL_8085}{ENDPOINTS['events']}"
    dto_request_str = json.dumps(create_event_dto_request)

    files = {
        'addEventDtoRequest': (None, dto_request_str),
        'image': (None, '')
    }

    response = requests.post(url, headers={"Authorization": auth_token}, files=files)

    logger.info(f"Status code: {response.status_code}")
    logger.info(f"Response body: {response.text}")

    assert response.status_code == 201
    assert response.headers['Content-Type'] == 'application/json'

    event_data = response.json()
    logger.debug(f"Parsed response JSON: {json.dumps(event_data, indent=2)}")
    event_id = event_data.get("id")
    yield event_data

    delete_url = f"{API_BASE_URL_8085}{ENDPOINTS['delete_events'].format(event_id)}"
    del_response = requests.delete(delete_url, headers={"Authorization": auth_token})
    assert del_response.status_code == 200, "Failed to delete event"
