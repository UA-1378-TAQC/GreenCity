import pytest
import requests
import json
from jsonschema.validators import validate

from green_city.src.config import API_BASE_URL_8085


@pytest.fixture
def create_and_cleanup_eco_news(auth_token):

    eco_news_json = {
        "title": "Test Eco News for Favorites",
        "text": "This is a test eco news content for testing favorites functionality. It needs to be long enough to meet requirements.",
        "tags": ["news"],
        "source": "https://example.org/",
        "shortInfo": "Test eco news for favorites testing"
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

    assert response.status_code == 201, f"Failed to create eco news: {response.status_code}, {response.text}"

    eco_news_id = response.json()["id"]

    yield eco_news_id

    try:
        requests.delete(
            f"{API_BASE_URL_8085}/eco-news/{eco_news_id}/favorites",
            headers={"Authorization": auth_token}
        )
    except:
        pass


@pytest.fixture
def eco_news_in_favorites(create_and_cleanup_eco_news, auth_token):
    eco_news_id = create_and_cleanup_eco_news

    response = requests.post(
        f"{API_BASE_URL_8085}/eco-news/{eco_news_id}/favorites",
        headers={"Authorization": auth_token}
    )
    assert response.status_code == 200, f"Failed to add to favorites: {response.status_code}, {response.text}"

    return eco_news_id


def test_remove_eco_news_from_favorites_success(eco_news_in_favorites, auth_token):
    eco_news_id = eco_news_in_favorites

    response = requests.delete(
        f"{API_BASE_URL_8085}/eco-news/{eco_news_id}/favorites",
        headers={"Authorization": auth_token}
    )

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    assert response.text == "", f"Expected empty response, got {response.text}"


def test_remove_eco_news_from_favorites_unauthorized():
    eco_news_id = 1

    response = requests.delete(
        f"{API_BASE_URL_8085}/eco-news/{eco_news_id}/favorites"
    )

    expected_response = {
        "status": 401,
        "error": "Unauthorized"
    }

    assert response.status_code == 401, f"Expected 401, got {response.status_code}"

    response_data = response.json()
    assert response_data["status"] == expected_response["status"]
    assert response_data["error"] == expected_response["error"]


def test_remove_eco_news_from_favorites_not_found(auth_token):
    non_existent_id = 999999

    response = requests.delete(
        f"{API_BASE_URL_8085}/eco-news/{non_existent_id}/favorites",
        headers={"Authorization": auth_token}
    )

    assert response.status_code == 404, f"Expected 404, got {response.status_code}"


def test_remove_eco_news_from_favorites_bad_request(auth_token):
    invalid_id = "invalid_id"

    response = requests.delete(
        f"{API_BASE_URL_8085}/eco-news/{invalid_id}/favorites",
        headers={"Authorization": auth_token}
    )

    assert response.status_code == 400, f"Expected 400, got {response.status_code}"


def test_remove_eco_news_from_favorites_negative_id(auth_token):
    negative_id = -1

    response = requests.delete(
        f"{API_BASE_URL_8085}/eco-news/{negative_id}/favorites",
        headers={"Authorization": auth_token}
    )

    assert response.status_code in [400, 404], f"Expected 400 or 404, got {response.status_code}"


def test_remove_eco_news_from_favorites_not_in_favorites(create_and_cleanup_eco_news, auth_token):
    eco_news_id = create_and_cleanup_eco_news

    response = requests.delete(
        f"{API_BASE_URL_8085}/eco-news/{eco_news_id}/favorites",
        headers={"Authorization": auth_token}
    )

    assert response.status_code in [400], f"Expected 400, got {response.status_code}"


def test_add_eco_news_to_favorites_success(create_and_cleanup_eco_news, auth_token):
    eco_news_id = create_and_cleanup_eco_news

    response = requests.post(
        f"{API_BASE_URL_8085}/eco-news/{eco_news_id}/favorites",
        headers={"Authorization": auth_token}
    )

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    assert response.text == "", f"Expected empty response, got {response.text}"


def test_add_eco_news_to_favorites_unauthorized():
    eco_news_id = 1

    response = requests.post(
        f"{API_BASE_URL_8085}/eco-news/{eco_news_id}/favorites"
    )

    expected_response = {
        "status": 401,
        "error": "Unauthorized"
    }

    assert response.status_code == 401, f"Expected 401, got {response.status_code}"

    response_data = response.json()
    assert response_data["status"] == expected_response["status"]
    assert response_data["error"] == expected_response["error"]


def test_add_eco_news_to_favorites_not_found(auth_token):
    non_existent_id = 999999

    response = requests.post(
        f"{API_BASE_URL_8085}/eco-news/{non_existent_id}/favorites",
        headers={"Authorization": auth_token}
    )

    assert response.status_code == 404, f"Expected 404, got {response.status_code}"


def test_add_eco_news_to_favorites_bad_request(auth_token):
    invalid_id = "invalid_id"

    response = requests.post(
        f"{API_BASE_URL_8085}/eco-news/{invalid_id}/favorites",
        headers={"Authorization": auth_token}
    )

    assert response.status_code == 400, f"Expected 400, got {response.status_code}"


def test_favorites_workflow_complete(create_and_cleanup_eco_news, auth_token):
    eco_news_id = create_and_cleanup_eco_news

    # Step 1: Add to favorites
    add_response = requests.post(
        f"{API_BASE_URL_8085}/eco-news/{eco_news_id}/favorites",
        headers={"Authorization": auth_token}
    )
    assert add_response.status_code == 200
    assert add_response.text == "", f"Expected empty response, got {add_response.text}"

    # Step 2: Remove from favorites
    remove_response = requests.delete(
        f"{API_BASE_URL_8085}/eco-news/{eco_news_id}/favorites",
        headers={"Authorization": auth_token}
    )
    assert remove_response.status_code == 200
    assert remove_response.text == "", f"Expected empty response, got {remove_response.text}"


def test_favorites_response_headers(create_and_cleanup_eco_news, auth_token):
    eco_news_id = create_and_cleanup_eco_news

    post_response = requests.post(
        f"{API_BASE_URL_8085}/eco-news/{eco_news_id}/favorites",
        headers={"Authorization": auth_token}
    )

    assert post_response.status_code == 200

    headers = post_response.headers
    assert "x-content-type-options" in headers.keys()
    assert "x-frame-options" in headers.keys()
    assert "cache-control" in headers.keys()

    delete_response = requests.delete(
        f"{API_BASE_URL_8085}/eco-news/{eco_news_id}/favorites",
        headers={"Authorization": auth_token}
    )

    assert delete_response.status_code == 200

    headers = delete_response.headers
    assert "x-content-type-options" in headers.keys()
    assert "x-frame-options" in headers.keys()
    assert "cache-control" in headers.keys()


@pytest.mark.parametrize("eco_news_id", [1, 2, 3])
def test_favorites_operations_various_ids(eco_news_id, auth_token):

    add_response = requests.post(
        f"{API_BASE_URL_8085}/eco-news/{eco_news_id}/favorites",
        headers={"Authorization": auth_token}
    )

    assert add_response.status_code in [200, 404], f"Expected 200 or 404 for ADD, got {add_response.status_code}"

    remove_response = requests.delete(
        f"{API_BASE_URL_8085}/eco-news/{eco_news_id}/favorites",
        headers={"Authorization": auth_token}
    )

    assert remove_response.status_code in [200,
                                           404], f"Expected 200 or 404 for REMOVE, got {remove_response.status_code}"