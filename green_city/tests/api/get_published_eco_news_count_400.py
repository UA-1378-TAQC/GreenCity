import os
import sys
import logging
import pytest
import requests

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

import green_city.config.config
import green_city.config.logging_config

from jsonschema import validate
from green_city.config.config import API_BASE_URL_8085, ENDPOINTS
from green_city.data.schema.get_published_eco_news_count_schema_bad_request import BAD_REQUEST_SCHEMA

logger = logging.getLogger(__name__)
    
def test_eco_news_count_with_invalid_author_id_returns_400():
    url = f"{API_BASE_URL_8085}{ENDPOINTS['count_eco_news']}?author-id=2" 
    response = requests.get(url)

    assert response.status_code == 400, f"Expected 400 Bad Request, got {response.status_code}"

    content_type = response.headers.get("Content-Type", "")
    assert "application/json" in content_type, \
        f"Expected 'application/json' in Content-Type, got {content_type}"

    try:
        json_data = response.json()
    except ValueError:
        pytest.fail("Response is not valid JSON")

    validate(instance=json_data, schema=BAD_REQUEST_SCHEMA)

    assert isinstance(json_data["message"], str) and json_data["message"], \
        "Error 'message' should be a non-empty string"
    assert json_data["status"] == 400, \
        f"Expected status 400, got {json_data['status']}"
    assert isinstance(json_data["timestamp"], str) and json_data["timestamp"], \
        "Error 'timestamp' should be a non-empty string"
