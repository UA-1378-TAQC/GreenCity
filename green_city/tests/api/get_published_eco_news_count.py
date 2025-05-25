import pytest
import requests
import logging
import green_city.src.util.logging_config

from jsonschema import validate
from green_city.src.config import API_BASE_URL_8085, ENDPOINTS
from ..data.schema.get_published_eco_news_count_schema_bad_request import BAD_REQUEST_SCHEMA
from ..data.schema.get_published_eco_news_count_schema import ECO_NEWS_COUNT_SCHEMA

logger = logging.getLogger(__name__)

def test_eco_news_count_with_invalid_method_returns_400():
    url = f"{API_BASE_URL_8085}{ENDPOINTS['count_eco_news']}"
    response = requests.post(url)

    assert response.status_code == 400, "Should return status code 400"
    assert response.headers['Content-Type'] == 'application/json', \
        "Content-Type should be application/json"

    json_data = response.json()
    validate(instance=json_data, schema=BAD_REQUEST_SCHEMA)
