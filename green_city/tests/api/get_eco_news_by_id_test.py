import pytest
import requests
from jsonschema import validate
from green_city.src.config import API_BASE_URL_8085, ENDPOINTS
from green_city.tests.data.schema.news_id_schema import get_schema
from green_city.tests.data.test_data.news_id_data import get_data
import green_city.src.util.logging_config
import logging
logger = logging.getLogger(__name__)


@pytest.mark.parametrize("eco_news_id, expected_status, expected_response, schema_name", [
    (get_data["valid_eco_news_id"], 200, get_data["200_response_body"], "200_response_schema"),
    ("invalid_id", 400, get_data["400_string_id_response"], "400_schema"),
    (" ", 400, get_data["400_empty_response"], "empty_id_schema"),
    (-1, 404, get_data["404_negative_id_response"], "404_schema"),
    (0, 404, get_data["404_zero_id_response"], "404_schema"),
    (100, 404, get_data["404_not_exist_id_response"], "404_schema"),
])
def test_get_eco_news_by_id(auth_token, eco_news_id, expected_status, expected_response, schema_name):
    logger.info(f"\nStarting test for ID: {eco_news_id}")

    url = f"{API_BASE_URL_8085}{ENDPOINTS['news'].format(eco_news_id)}"
    headers = {"Authorization": auth_token} if auth_token else {}
    logger.info(f"Testing GET {url}")
    logger.info(f"Expected status: {expected_status}")
    response = requests.get(url, headers=headers)
    logger.info(f"Response status: {response.status_code}")

    assert response.status_code == expected_status, \
        f"Expected status {expected_status}, but got {response.status_code}"

    response_data = response.json()
    validate(instance=response_data, schema=get_schema[schema_name])

    if expected_status == 200:
        assert response_data["id"], "id"
        assert response_data["title"], "title"
        assert response_data["content"], "content"
        logger.info("All success assertions passed")
    else:
        if "message" in expected_response:
            assert expected_response["message"] in response_data.get("message", ""), \
                f"Expected error message to contain '{expected_response['message']}', but got '{response_data.get('message', '')}'"
        elif "detail" in expected_response:
            assert expected_response["detail"] in response_data.get("detail", ""), \
                f"Expected error detail to contain '{expected_response['detail']}', but got '{response_data.get('detail', '')}'"
        logger.info("All error message assertions passed")
