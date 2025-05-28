from green_city.config.logging_config import get_logger
import requests
import pytest
from green_city.config.config import API_BASE_URL_8085, ENDPOINTS
from jsonschema import validate, ValidationError
from ..data.schema.general_schemas import error_schema, single_message_schema

logger = get_logger(__name__)

def request_add_to_favorites(token, id):
      return requests.post(
        f'{API_BASE_URL_8085}{ENDPOINTS["favorites"].format(id)}',
        headers={"Authorization": token}
      )

def assert_test_response(response, expected_status_code, param, expected_response_by_param, schema_by_param):
      assert response.status_code == expected_status_code, f"Expected status code {expected_status_code}, but got {response.status_code}"
      data_json = get_response_json(response)
      assert_scheme(data_json,schema_by_param)
      assert response.json()[param]==expected_response_by_param, f"Expected {param}: {expected_response_by_param} but got {response.json()[param]}" 

def test_add_to_favorites_already_in(create_news, auth_token):
      id= create_news
      logger.info(f'Request to add new eco-new with id={id} to favorites')
      response = request_add_to_favorites(auth_token, id)
      logger.info(f"Status code: {response.status_code}")
      
      logger.info(f'Second request to add new eco-new with id={id} to favorites')
      response = request_add_to_favorites(auth_token, id)
      logger.info(f"Status code: {response.status_code}")

      expected_status_code = 400
      param="message"
      expected_response_by_param = "User has already added this eco new to favorites."
      schema_by_param = single_message_schema
      assert_test_response(response, expected_status_code, param, expected_response_by_param, schema_by_param)

def test_add_to_favorites_incorrect_id(auth_token):
      id= '8&'
      logger.info(f'Request to add new eco-new with id={id} to favorites')
      response = request_add_to_favorites(auth_token, id)
      logger.info(f"Status code: {response.status_code}")
      
      expected_status_code = 400
      param="message"
      expected_response_by_param = "Wrong ecoNewsId. Should be 'Long'"
      schema_by_param = single_message_schema
      assert_test_response(response, expected_status_code, param, expected_response_by_param, schema_by_param)

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
