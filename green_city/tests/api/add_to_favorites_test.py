import green_city.src.util.logging_config
import pytest
import requests
from green_city.src.config import API_BASE_URL_8085, ENDPOINTS
import logging
from jsonschema import validate
from ..data.schema.general_schemas import error_schema, single_message_schema

logger = logging.getLogger(__name__)

def request_add_to_favorites(token, id):
      return requests.post(
        f'{API_BASE_URL_8085}{ENDPOINTS["favorites"].format(id)}',
        headers={"Authorization": token}
      )

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

      assert response.status_code == expected_status_code, f"Expected status code {expected_status_code}, but got {response.status_code}"
      validate(instance=response.json(), schema=single_message_schema)
      assert response.json()[param]==expected_response_by_param, f"Expected {param}: {expected_response_by_param} but got {response.json()[param]}"

def test_add_to_favorites_incorrect_id(auth_token):
      id= '8&'
      logger.info(f'Request to add new eco-new with id={id} to favorites')
      response = request_add_to_favorites(auth_token, id)
      logger.info(f"Status code: {response.status_code}")
      
      expected_status_code = 400
      param="message"
      expected_response_by_param = "Wrong ecoNewsId. Should be 'Long'"

      assert response.status_code == expected_status_code, f"Expected status code {expected_status_code}, but got {response.status_code}"
      validate(instance=response.json(), schema=single_message_schema)
      assert response.json()[param]==expected_response_by_param, f"Expected {param}: {expected_response_by_param} but got {response.json()[param]}"      

    