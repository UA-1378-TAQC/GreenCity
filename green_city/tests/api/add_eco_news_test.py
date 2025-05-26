import pytest
import json
import requests
from jsonschema import validate
from green_city.src.config import API_BASE_URL_8085, ENDPOINTS
from green_city.tests.data.schema.add_news_schema import post_schema
import green_city.src.util.logging_config
import logging

logger = logging.getLogger(__name__)


def post_news(payload: dict, auth_token=None):
    url = f"{API_BASE_URL_8085}{ENDPOINTS['create_eco_news']}"
    headers = {"Authorization": auth_token} if auth_token else {}

    files = {
        'addEcoNewsDtoRequest': (None, json.dumps(payload)),
        'image': (None, '')
    }

    return requests.post(url, headers=headers, files=files)


@pytest.mark.api
def test_add_news_201(auth_token, valid_news_payload):
    resp = post_news(valid_news_payload, auth_token)
    logger.info(f"POST news response: {resp.status_code} - {resp.text}")

    assert resp.status_code == 201
    validate(resp.json(), post_schema["201_schema"])
    assert isinstance(resp.json().get("id"), int)


def test_add_news_unauthorized(valid_news_payload):
    resp = post_news(valid_news_payload)
    logger.info(f"Unauthorized news POST: {resp.status_code} - {resp.text}")
    assert resp.status_code == 401
    validate(resp.json(), post_schema["401_schema"])


@pytest.mark.parametrize("tags, expected_message", [
    (["String"], "There should be at least one valid tag")
])
def test_add_news_invalid_tags(auth_token, valid_news_payload, tags, expected_message):
    valid_news_payload["tags"] = tags
    resp = post_news(valid_news_payload, auth_token)

    assert resp.status_code == 400
    json_body = resp.json()
    assert expected_message in json_body.get("message", "")
    logger.info("Validating response schema for 400...")
    validate(json_body, post_schema["400_schema"])


def test_add_news_invalid_source(auth_token, valid_news_payload):
    valid_news_payload["source"] = "example.org"
    resp = post_news(valid_news_payload, auth_token)

    assert resp.status_code == 400
    json_body = resp.json()
    assert "URI" in json_body.get("message", "")
    logger.info("Validating response schema for 400...")
    validate(json_body, post_schema["400_schema"])
