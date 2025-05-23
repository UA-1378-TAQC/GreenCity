import  green_city.src.logging_config
import requests
from green_city.src.config import API_BASE_URL_8085, ENDPOINTS
import logging
from jsonschema import validate

logger = logging.getLogger(__name__)

summary_schema_message = {
  "type": "object",
    "properties": {
        "message": {"type": "string"}
    },
    "required": ["message"],
    "additionalProperties": False
}

summary_schema_valid_result = {
  "type": "object",
    "properties": {
        "content": {"type": "string"},
        "source": {"type": "string"}
    },
    "required": ["content","source"],
    "additionalProperties": False
}

data = {
    "200_response_body":{
        "content": "<p>My Test Eco News My Test Eco News</p>",
        "source": ""
    },
    "404_response_body":{
        "message":"Eco new doesn't exist by this id: 101"
    }
}
    
def test_get_summary_by_id_not_found(auth_token):
    news_invalid_id = 101
    response = requests.get(
        f'{API_BASE_URL_8085}{ENDPOINTS["summary"].format(news_invalid_id)}',
        headers={"Authorization": auth_token},
    )
    logger.info(f"Status code: {response.status_code}")
    validate(instance=response.json(), schema=summary_schema)
    expected_status_code = 404
    assert response.status_code == expected_status_code, f"Expected status code {expected_status_code}, but got {response.status_code}"
    assert response.json()["message"]==data["404_response_body"].get("message")

def test_get_summary_by_id_success(auth_token):
    news_id = 1
    response = requests.get(
        f'{API_BASE_URL_8085}{ENDPOINTS["summary"].format(news_id)}',
        headers={"Authorization": auth_token},
    )
    logger.info(f"Status code: {response.status_code}")
    validate(instance=response.json(), schema=summary_schema_valid_result)
    expected_status_code = 200
    assert response.status_code == expected_status_code, f"Expected status code {expected_status_code}, but got {response.status_code}"
    assert response.json()["content"]==data["200_response_body"].get("content")

