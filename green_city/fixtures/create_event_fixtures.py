import json

import pytest
import requests

from green_city.config.config import API_BASE_URL_8085, ENDPOINTS
from green_city.data.fixture_dto.create_event_dto_request import create_event_dto_request


@pytest.fixture
def create_event(auth_token):
    url = f"{API_BASE_URL_8085}{ENDPOINTS['events']}"
    dto_request_str = json.dumps(create_event_dto_request)

    files = {
        'addEventDtoRequest': (None, dto_request_str),
        'image': (None, '')
    }

    response = requests.post(url, headers={"Authorization": auth_token}, files=files)

    event_data = response.json()
    event_id = event_data.get("id")
    yield event_data

    delete_url = f"{API_BASE_URL_8085}{ENDPOINTS['delete_events'].format(event_id)}"
    del_response = requests.delete(delete_url, headers={"Authorization": auth_token})
