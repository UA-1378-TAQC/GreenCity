import pytest
import requests
import json
from jsonschema.validators import validate

from green_city.src.config import API_BASE_URL_8085


@pytest.fixture
def create_and_cleanup_eco_news(auth_token):

    eco_news_json = {
        "title": "Test Eco News Title",
        "text": "This is a test eco news content for testing likes count functionality. It needs to be long enough to meet requirements.",
        "tags": ["news"],
        "source": "https://example.org/",
        "shortInfo": "Test eco news for likes count testing"
    }

    files = {
        'addEcoNewsDtoRequest': (None, json.dumps(eco_news_json)),
        'image': (None, '')
    }

    response = requests.post(
        f"{API_BASE_URL_8085}/eco-news",
        files=files,
        headers={"Authorization": auth_token}
    )

    assert response.status_code == 201, f"Failed to create eco news: {response.status_code}"

    eco_news_id = response.json()["id"]

    yield eco_news_id

def test_get_eco_news_likes_count_success(create_and_cleanup_eco_news):
    eco_news_id = create_and_cleanup_eco_news

    response = requests.get(
        f"{API_BASE_URL_8085}/eco-news/{eco_news_id}/likes/count"
    )

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    likes_count = response.json()
    assert isinstance(likes_count, int), f"Expected integer, got {type(likes_count)}"
    assert likes_count >= 0, f"Likes count should be non-negative, got {likes_count}"


def test_get_eco_news_likes_count_not_found():
    non_existent_id = 999999

    response = requests.get(
        f"{API_BASE_URL_8085}/eco-news/{non_existent_id}/likes/count"
    )

    assert response.status_code == 404, f"Expected 404, got {response.status_code}"


def test_get_eco_news_likes_count_bad_request():
    invalid_id = "invalid_id"

    response = requests.get(
        f"{API_BASE_URL_8085}/eco-news/{invalid_id}/likes/count"
    )

    assert response.status_code == 400, f"Expected 400, got {response.status_code}"


def test_get_eco_news_likes_count_negative_id():
    negative_id = -1

    response = requests.get(
        f"{API_BASE_URL_8085}/eco-news/{negative_id}/likes/count"
    )
    assert response.status_code in [400, 404], f"Expected 400 or 404, got {response.status_code}"


def test_get_eco_news_likes_count_zero_id():
    zero_id = 0

    response = requests.get(
        f"{API_BASE_URL_8085}/eco-news/{zero_id}/likes/count"
    )

    assert response.status_code in [400, 404], f"Expected 400 or 404, got {response.status_code}"


def test_get_eco_news_likes_count_response_headers(create_and_cleanup_eco_news):
    eco_news_id = create_and_cleanup_eco_news

    response = requests.get(
        f"{API_BASE_URL_8085}/eco-news/{eco_news_id}/likes/count"
    )

    assert response.status_code == 200

    headers = response.headers
    assert "x-content-type-options" in headers.keys()
    assert "x-frame-options" in headers.keys()
    assert "cache-control" in headers.keys()
    assert "application/json" in headers.get("content-type", "")


@pytest.mark.parametrize("eco_news_id", [1, 2, 3])
def test_get_eco_news_likes_count_various_ids(eco_news_id):
    response = requests.get(
        f"{API_BASE_URL_8085}/eco-news/{eco_news_id}/likes/count"
    )
    assert response.status_code in [200, 404], f"Expected 200 or 404, got {response.status_code}"

    if response.status_code == 200:
        likes_count = response.json()
        assert isinstance(likes_count, int)
        assert likes_count >= 0