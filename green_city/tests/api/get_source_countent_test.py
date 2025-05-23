import  green_city.src.logging_config
import pytest
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
    "400_response_body":{
        "message": "Wrong ecoNewsId. Should be 'Long'"
    },
    "400_response_body_html":{
        'status': 400,
        'error': 'Bad Request',
        'path': '/eco-news/%25/summary'
    },  
    "401_response_body":{
        "status": 401,
        "error": "Unauthorized",
        "path": "/eco-news/1/summary"
    }
}
    
def test_get_summary_by_id_not_found(auth_token):
    news_invalid_id = 101
    response = get_summary_request(auth_token, news_invalid_id)
    logger.info(f"Status code: {response.status_code}")
    validate(instance=response.json(), schema=summary_schema)
    expected_status_code = 404
    assert response.status_code == expected_status_code, f"Expected status code {expected_status_code}, but got {response.status_code}"
    assert response.json()["message"]==data["404_response_body"].get("message")


@pytest.mark.parametrize(
    "eco_news_id, expected_param, expected_response, expected_schema",
    [
        ("8&", "message", data["400_response_body"], summary_schema),
        ("%25", "error", data["400_response_body_html"], summary_schema_error),
    ]
)

def test_get_summary_by_id_incorrect(auth_token, eco_news_id, expected_param, expected_response, expected_schema):
    response = get_summary_request(auth_token, eco_news_id)
    logger.info(f"Status code: {response.status_code}")
    logger.info(f"Response body: {response.json()}")
    validate(instance=response.json(), schema=expected_schema)
    expected_status_code = 400
    assert response.status_code == expected_status_code, f"Expected status code {expected_status_code}, but got {response.status_code}"
    assert response.json()[expected_param]==expected_response.get(expected_param)

    
def get_summary_request(token, id):
    return requests.get(
        f'{API_BASE_URL_8085}{ENDPOINTS["summary"].format(id)}',
        headers={"Authorization": token},
    )

def test_get_summary_by_id_unauthorized():
    news_id = 1
    response = get_summary_request('', news_id)
    logger.info(f"Status code: {response.status_code}")
    validate(instance=response.json(), schema=summary_schema_error)
    expected_status_code = 401
    assert response.status_code == expected_status_code, f"Expected status code {expected_status_code}, but got {response.status_code}"
    assert response.json()["error"]==data["401_response_body"].get("error")
