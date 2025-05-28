import pytest
import requests
from jsonschema import validate, ValidationError

from green_city.src.config import API_BASE_URL_8085, ENDPOINTS
from green_city.tests.data.schema.eco_news_response_schema import eco_news_response_schema


def test_get_eco_news_valid_response_schema(auth_token):
    url = f"{API_BASE_URL_8085}{ENDPOINTS['get_eco_news']}"
    headers = {"Authorization": auth_token}
    params = {"page": 0, "size": 5}

    response = requests.get(url, headers=headers, params=params)
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"

    try:
        json_data = response.json()
    except ValueError:
        pytest.fail("Response is not valid JSON")

    try:
        validate(instance=json_data, schema=eco_news_response_schema)
    except ValidationError as e:
        pytest.fail(f"Response JSON does not match schema: {e.message}")
