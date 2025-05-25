import pytest
import requests
from green_city.src.config import API_BASE_URL_8085, ENDPOINTS
from jsonschema import validate
from ..data.schema.tags_schema import TAGS_SCHEMA, TAGS_ERROR_MESSAGE_SCHEMA
import green_city.src.util.logging_config
import logging

logger = logging.getLogger(__name__)

def test():
    logger.info("info")

def test_get_tags_default_returns_200():
    response = requests.get(f"{API_BASE_URL_8085}{ENDPOINTS['news_tags']}")

    assert response.status_code == 200, \
        "Request should return status code 200"
    assert response.headers['Content-Type'] == 'application/json', \
        "Response content type should be application/json"

    validate(instance=response.json(), schema=TAGS_SCHEMA)

@pytest.mark.parametrize("lang_code", ["en", "ua"])
def test_get_tags_in_language_returns_200(lang_code):

    response = requests.get(
        f"{API_BASE_URL_8085}{ENDPOINTS['news_tags']}",
        params={"lang": lang_code}
    )

    assert response.status_code == 200, \
        f"Request with '{lang_code}' should return status code 200"
    assert response.headers['Content-Type'] == 'application/json', \
        "Response content type should be application/json"

    tags = response.json()
    validate(instance=tags, schema=TAGS_SCHEMA)

    for tag in tags:
        assert tag.get('languageCode') in [lang_code, None], \
            f"All tags should either have language code '{lang_code}' or be None"


@pytest.mark.parametrize("invalid_lang,expected_status,expected_message", [
    ("1", 400, "Select correct language: 'en' or 'ua'"),
    ("*", 400, "Select correct language: 'en' or 'ua'"),
    ("esp", 400, "Select correct language: 'en' or 'ua'"),
])
def test_invalid_language_parameter_returns_400(invalid_lang, expected_status, expected_message):

    response = requests.get(
        f"{API_BASE_URL_8085}{ENDPOINTS['news_tags']}",
        params={"lang": invalid_lang}
    )

    assert response.status_code == expected_status, \
        f"Request with '{invalid_lang}' should return status code {expected_status}"
    assert response.headers['Content-Type'] == 'application/json', \
        "Error response content type should be application/json"

    if expected_status == 400:
        response_json = response.json()
        validate(instance=response_json, schema=TAGS_ERROR_MESSAGE_SCHEMA)

        assert response_json['message'] == expected_message, \
            f"Error message for '{invalid_lang}' should match expected pattern"
