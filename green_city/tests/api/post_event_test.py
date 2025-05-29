import json
import pytest
import requests
from jsonschema import validate
from green_city.config.config import API_BASE_URL_8085, ENDPOINTS
from green_city.data.schema.error_event_schema import error_event_schemas
from green_city.data.schema.event_schema import EVENT_SCHEMA
from green_city.fixtures.create_event_fixtures import create_event
from green_city.fixtures.login_fixture import auth_token
from green_city.data.test_data.post_event_error_message import post_event_test_data
from green_city.data.fixture_dto.create_event_dto_request import create_event_dto_request

def test_create_event_returns_201(create_event):
    event_data = create_event

    assert validate(instance=event_data, schema=EVENT_SCHEMA) is None, (
        "Response data does not match schema"
    )

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

    assert response.status_code == 400, f"Expected 400 for '{test_case_key}', got {response.status_code}"

    response_json = response.json()
    if isinstance(response_json, dict):
        response_json = [response_json]

    assert validate(instance=response_json, schema=error_event_schemas["400_validation_errors"]) is None, (
        "Response data does not match schema"
    )

    for expected_error in test_case["expected_errors"]:
        assert expected_error in response_json, (
            f"Expected error {expected_error} not found in response: {response_json}"
        )
