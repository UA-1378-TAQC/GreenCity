from green_city.config.logging_config import get_logger
import requests
from green_city.config.config import API_BASE_URL_8085, ENDPOINTS
from jsonschema import validate
from ..data.schema.general_schemas import error_schema, single_message_schema

logger = get_logger(__name__)

def request_add_to_favorites(token, id):
      return requests.post(
        f'{API_BASE_URL_8085}{ENDPOINTS["favorites"].format(id)}',
        headers={"Authorization": token}
      )

def assert_test_response(response, expected_status_code, param, expected_response_by_param, schema_by_param):
      assert response.status_code == expected_status_code, f"Expected status code {expected_status_code}, but got {response.status_code}"
      validate(instance=response.json(), schema=schema_by_param)
      assert response.json()[param]==expected_response_by_param, f"Expected {param}: {expected_response_by_param} but got {response.json()[param]}"
 
def test_add_to_favorites_unauthorized(create_news):
      id= create_news
      logger.info(f'Request to add new eco-new with id={id} to favorites')
      response = request_add_to_favorites('', id)
      logger.info(f"Status code: {response.status_code}")
      
      expected_status_code = 401
      param="error"
      expected_response_by_param = "Unauthorized"
      schema_by_param = error_schema
      assert_test_response(response, expected_status_code, param, expected_response_by_param, schema_by_param)
