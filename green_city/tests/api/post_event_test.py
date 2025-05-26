import json
import pytest
import requests
from jsonschema import validate
from green_city.src.config import API_BASE_URL_8085, ENDPOINTS
from green_city.tests.data.fixture_dto.create_event_dto_request import create_event_dto_request
from green_city.tests.data.schema.event_schema import EVENT_SCHEMA
import green_city.src.util.logging_config
import logging

from green_city.tests.data.test_data.post_event_validation_test_cases import post_event_validation_test_cases

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


@pytest.mark.parametrize("test_case", post_event_validation_test_cases)
def test_create_event_returns_400(test_case, auth_token):
    url = f"{API_BASE_URL_8085}{ENDPOINTS['events']}"

    headers = {
        'Authorization': auth_token
    }

    request_data = create_event_dto_request.copy()
    for key, value in test_case["payload"].items():
        request_data[key] = value

    dto_request_str = json.dumps(request_data)

    files = {
        'addEventDtoRequest': (None, dto_request_str, 'application/json'),
        'image': ('empty.jpg', '', 'image/jpeg')
    }

    response = requests.post(url, files=files, headers=headers)

    assert response.status_code == 400, (
        f"Expected status code 400 for test case '{test_case['name']}', got {response.status_code}. "
        f"Response: {response.text}"
    )

    response_data = response.json()
    if isinstance(response_data, dict):
        response_data = [response_data]

    assert isinstance(response_data, list), f"Expected list of errors, got: {type(response_data)}"

    for expected_error in test_case["expected_errors"]:
        assert expected_error in response_data, (
            f"Expected error {expected_error} not found in response: {response_data}"
        )
