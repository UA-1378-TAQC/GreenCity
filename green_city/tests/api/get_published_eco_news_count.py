import os
import sys
import logging
import pytest
import requests

import green_city.config.config
import green_city.config.logging_config

from jsonschema import validate
from green_city.config.config import API_BASE_URL_8085, ENDPOINTS

from green_city.data.schema.get_published_eco_news_count_schema import ECO_NEWS_COUNT_SCHEMA
from green_city.data.schema.get_published_eco_news_count_schema_unauthorized import UNAUTHORIZED_REQUEST_SCHEMA

logger = logging.getLogger(__name__)

def test_eco_news_count_unauthorized_access_returns_401():
    url = f"{API_BASE_URL_8085}{ENDPOINTS['count_eco_news']}"
    response = requests.get(url)

    assert response.status_code == 401, \
        f"Expected status code 401, got {response.status_code}"

    content_type = response.headers.get("Content-Type", "")
    assert "application/json" in content_type, \
        f"Expected 'application/json' in Content-Type, got {content_type}"

    try:
        json_data = response.json()
    except ValueError:
        pytest.fail("Response is not valid JSON")

    validate(instance=json_data, schema=UNAUTHORIZED_REQUEST_SCHEMA)

    assert json_data.get("error") == "Unauthorized", \
        f"Expected error message to be 'Unauthorized', got {json_data.get('error')}"


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

