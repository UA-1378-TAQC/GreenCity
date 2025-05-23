import  green_city.src.logging_config
import pytest
import requests
from green_city.src.config import API_BASE_URL_8085, ENDPOINTS
import logging
from jsonschema import validate
from ..test_data.summary_source_content_data import get_schema, get_data

logger = logging.getLogger(__name__)

@pytest.mark.parametrize(
    "eco_news_id, expected_param, expected_response, expected_schema, token",
    [
        ("8&", "message", get_data["400_response_body"], get_schema["summary_schema_message"], True),
        ("%25", "error", get_data["400_response_body_html"], get_schema["summary_schema_error"], True),
        ("1","error", get_data["401_response_body"], get_schema["summary_schema_error"], False),
        ("101", "message", get_data["404_response_body"], get_schema["summary_schema_message"], True),
        ("1", "content", get_data["200_response_body"], get_schema["summary_schema_valid_result"], True)
    ]
)

def test_get_summary_by_id(eco_news_id, expected_param, expected_response, expected_schema, token, auth_token):
    token_for_use = auth_token if token is True else ''
    response = requests.get(
        f'{API_BASE_URL_8085}{ENDPOINTS["summary"].format(eco_news_id)}',
        headers={"Authorization": token_for_use},
    )
    logger.info(f"Status code: {response.status_code}")
    logger.info(f"Response body: {response.json()}")
    validate(instance=response.json(), schema=expected_schema)
    expected_status_code = expected_response.get("status")
    assert response.status_code == expected_status_code, f"Expected status code {expected_status_code}, but got {response.status_code}"
    assert response.json()[expected_param]==expected_response.get(expected_param)

