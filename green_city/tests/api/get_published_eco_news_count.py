import pytest
import requests
import logging
import green_city.src.util.logging_config

from jsonschema import validate
from green_city.src.config import API_BASE_URL_8085, ENDPOINTS
from ..data.schema.get_published_eco_news_count_schema import ECO_NEWS_COUNT_SCHEMA

logger = logging.getLogger(__name__)

def test_get_eco_news_count_returns_200_and_valid_value():
    url = f"{API_BASE_URL_8085}{ENDPOINTS['count_eco_news']}"
    logger.info(f"Requesting eco news count from: {url}")

    response = requests.get(url)

    assert response.status_code == 200, \
        "Should return status code 200"
    assert response.headers['Content-Type'] == 'application/json', \
        "Content-Type should be application/json"

    json_data = response.json()
    validate(instance=json_data, schema=ECO_NEWS_COUNT_SCHEMA)

    assert isinstance(json_data, int), "Count should be an integer"
    assert json_data >= 0, "Count should be non-negative"
