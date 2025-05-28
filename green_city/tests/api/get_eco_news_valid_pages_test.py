import requests
from jsonschema import validate

from green_city.src.config import API_BASE_URL_8085, ENDPOINTS
from green_city.tests.data.schema.eco_news_response_schema import eco_news_response_schema


def test_get_eco_news_valid_response_schema(auth_token):
    url = f"{API_BASE_URL_8085}{ENDPOINTS['get_eco_news']}"
    headers = {"Authorization": auth_token}
    params = {"page": 0, "size": 5}

    response = requests.get(url, headers=headers, params=params)
    assert response.status_code == 200

    json_data = response.json()

    validate(instance=json_data, schema=eco_news_response_schema)
