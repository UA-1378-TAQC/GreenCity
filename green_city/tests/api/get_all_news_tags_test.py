import pytest
import requests
from green_city.src.config import API_BASE_URL_8085, ENDPOINTS
from jsonschema import validate


TAGS_SCHEMA = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
            "name": {"type": "string"},
            "languageCode": {"type": ["string", "null"]}
        },
        "required": ["id", "name"]
    }
}


def test_get_tags_default():

    response = requests.get(f"{API_BASE_URL_8085}{ENDPOINTS['news_tags']}")

    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

    assert response.headers['Content-Type'] == 'application/json', \
        f"Expected Content-Type application/json, got {response.headers['Content-Type']}"

    tags = response.json()
    validate(instance=tags, schema=TAGS_SCHEMA)


def test_get_tags_ua_language():

    response = requests.get(f"{API_BASE_URL_8085}{ENDPOINTS['news_tags']}?lang=ua")

    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

    assert response.headers['Content-Type'] == 'application/json', \
        f"Expected Content-Type application/json, got {response.headers['Content-Type']}"

    tags = response.json()
    validate(instance=tags, schema=TAGS_SCHEMA)

    for tag in tags:
        assert tag.get('languageCode') in ['ua', None], \
            f"Expected languageCode 'ua' or None, got {tag.get('languageCode')}"


def test_get_tags_en_language():

    response = requests.get(f"{API_BASE_URL_8085}{ENDPOINTS['news_tags']}?lang=en")

    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

    assert response.headers['Content-Type'] == 'application/json', \
        f"Expected Content-Type application/json, got {response.headers['Content-Type']}"

    tags = response.json()
    validate(instance=tags, schema=TAGS_SCHEMA)

    for tag in tags:
        assert tag.get('languageCode') in ['en', None], \
            f"Expected languageCode 'en' or None, got {tag.get('languageCode')}"
