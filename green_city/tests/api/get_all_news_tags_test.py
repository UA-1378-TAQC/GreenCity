import pytest
import requests
from green_city.src.config import API_BASE_URL_8085, ENDPOINTS
from jsonschema import validate
from ..data.schema.tags_schema import TAGS_SCHEMA
import green_city.src.util.logging_config
import logging

logger = logging.getLogger(__name__)

def test():
    logger.info("info")

def test_get_tags_default():
    response = requests.get(f"{API_BASE_URL_8085}{ENDPOINTS['news_tags']}")

    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'

    validate(instance=response.json(), schema=TAGS_SCHEMA)

@pytest.mark.parametrize("lang_code", ["en", "ua"])
def test_get_tags_in_language(lang_code):
    response = requests.get(
        f"{API_BASE_URL_8085}{ENDPOINTS['news_tags']}",
        params={"lang": lang_code}
    )

    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'

    tags = response.json()
    validate(instance=tags, schema=TAGS_SCHEMA)

    for tag in tags:
        assert tag.get('languageCode') in [lang_code, None]