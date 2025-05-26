import json
import pytest
import requests
from jsonschema import validate
from green_city.src.config import API_BASE_URL_8085, ENDPOINTS
from green_city.tests.data.fixture_dto.create_event_dto_request import create_event_dto_request
from green_city.tests.data.schema.error_event_schema import error_event_schemas
from green_city.tests.data.schema.event_schema import EVENT_SCHEMA
import green_city.src.util.logging_config
import logging

from green_city.tests.data.test_data.post_event_error_message import post_event_test_data

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

    logger.info(f"Status code: {response.status_code}")
    logger.info(f"Response body: {response.text}")

    assert response.status_code == 401, (
        f"Expected status code 401, got {response.status_code}"
    )

    response_data = response.json()

    logger.debug(f"Parsed response JSON: {json.dumps(response_data, indent=2)}")

    assert response_data['status'] == 401, "Status field should be 401"
    assert response_data['error'] == "Unauthorized", "Error field should be 'Unauthorized'"

    assert 'application/json' in response.headers['Content-Type'].lower(), (
        "Response should be in JSON format"
    )


@pytest.mark.parametrize("test_case_key", list(post_event_test_data.keys()))
def test_create_event_returns_400(test_case_key, auth_token):
    test_case = post_event_test_data[test_case_key]
    url = f"{API_BASE_URL_8085}{ENDPOINTS['events']}"

    headers = {
        'Authorization': auth_token
    }

    dto_request_str = json.dumps(test_case["payload"])

    files = {
        'addEventDtoRequest': (None, dto_request_str, 'application/json'),
        'image': ('empty.jpg', '', 'image/jpeg')
    }

    response = requests.post(url, files=files, headers=headers)

    logger.info(f"Status code: {response.status_code}")
    logger.info(f"Response body: {response.text}")

    assert response.status_code == 400, f"Expected 400 for '{test_case_key}', got {response.status_code}"

    response_json = response.json()
    if isinstance(response_json, dict):
        response_json = [response_json]

    logger.debug(f"Parsed response JSON: {json.dumps(response_json, indent=2)}")

    validate(instance=response_json, schema=error_event_schemas["400_validation_errors"])

    for expected_error in test_case["expected_errors"]:
        assert expected_error in response_json, (
            f"Expected error {expected_error} not found in response: {response_json}"
        )
