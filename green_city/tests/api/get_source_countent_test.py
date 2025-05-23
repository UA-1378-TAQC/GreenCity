import  green_city.src.logging_config
import requests
from green_city.src.config import API_BASE_URL_8085, ENDPOINTS
import logging
from jsonschema import validate

logger = logging.getLogger(__name__)

summary_schema = {
  "type": "object",
    "properties": {
        "message": {"type": "string"}
    },
    "required": ["message"],
    "additionalProperties": False
}

summary_schema_error = {
  "type": "object",
    "properties": {
        "timestamp": {"type": "string"},
        "status": {"type": "number"},
        "error": {"type": "string"},
        "path": {"type": "string"}
    },
    "required": ["timestamp", "status", "error", "path"],
    "additionalProperties": False
}
    
data = {
    "404_response_body":{
        "message":"Eco new doesn't exist by this id: 101"
    },
    "401_response_body":{
        "status": 401,
        "error": "Unauthorized",
        "path": "/eco-news/1/summary"
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

def test_get_summary_by_id_unauthorized():
    news_id = 1
    response = requests.get(
        f'{API_BASE_URL_8085}{ENDPOINTS["summary"].format(news_id)}',
        headers={"Authorization": ''},
    )
    logger.info(f"Status code: {response.status_code}")
    validate(instance=response.json(), schema=summary_schema_error)
    expected_status_code = 401
    assert response.status_code == expected_status_code, f"Expected status code {expected_status_code}, but got {response.status_code}"
    assert response.json()["error"]==data["401_response_body"].get("error")