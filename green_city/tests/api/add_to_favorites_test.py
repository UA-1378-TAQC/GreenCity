from green_city.config.logging_config import get_logger
import requests
import pytest
from green_city.config.config import API_BASE_URL_8085, ENDPOINTS
from jsonschema import validate, ValidationError
from ..data.schema.general_schemas import error_schema, single_message_schema
from ..data.schema.all_news_schema import schema_all_news

logger = get_logger(__name__)

def request_add_to_favorites(token, id):
    return requests.post(
      f'{API_BASE_URL_8085}{ENDPOINTS["favorites"].format(id)}',
      headers={"Authorization": token}
    )

def test_add_to_favorites_success(create_news, auth_token):
    id = create_news
    logger.info(f'Request to add eco-new with id={id} to favorites')
    response = request_add_to_favorites(auth_token, id)
    logger.info(f"Status code: {response.status_code}")
    expected_status_code = 200
    assert response.status_code == expected_status_code, f"Expected status code {expected_status_code}, but got {response.status_code}"
    assert len(response.text)==0, f"Expected response should have be empty"

    logger.info('Request to get all news')
    response = requests.get(
        f"{API_BASE_URL_8085}{ENDPOINTS['all_news']}",
        headers={"Authorization": auth_token}
    )
    logger.info(f"Status code: {response.status_code}")
  
    data=get_response_json(response)
    assert_scheme(data,schema_all_news)
    matching_users = next((entry for entry in data["page"] if entry["id"] == id), None)
    assert matching_users['favorite'] == True, f'Expected "favorite": True, but was {matching_users["favorite"]}'

def assert_scheme(json_data, response_schema ):
    try:
        validate(instance=json_data, schema=response_schema)
    except ValidationError as e:
        pytest.fail(f"Response JSON does not match schema: {e.message}")

def get_response_json(response):
    try:
        return response.json()
    except ValueError:
        pytest.fail("Response is not valid JSON")
