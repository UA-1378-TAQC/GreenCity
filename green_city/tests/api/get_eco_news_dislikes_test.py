import pytest
import requests

from green_city.src.config import API_BASE_URL_8085, ENDPOINTS


def test_get_eco_news_dislikes_count_success(create_news, auth_token):
    eco_news_id = create_news
    headers = {"Authorization": f"Bearer {auth_token}"}

    like_response = requests.post(
        f"{API_BASE_URL_8085}{ENDPOINTS['create_eco_news']}/{eco_news_id}/like",
        headers=headers
    )
    assert like_response.status_code in [200, 201], "Failed to like the news"

    dislike_response = requests.post(
        f"{API_BASE_URL_8085}{ENDPOINTS['create_eco_news']}/{eco_news_id}/like",
        headers=headers
    )
    assert dislike_response.status_code in [200, 201], "Failed to unlike the news"

    response = requests.get(
        f"{API_BASE_URL_8085}{ENDPOINTS['create_eco_news']}/{eco_news_id}/likes/count"
    )

    assert response.status_code == 200
    count = response.json()
    assert isinstance(count, int), f"Expected int, got {type(count)}"
    assert count == 0, f"Expected 0 after dislike, got {count}"


def test_get_eco_news_dislikes_count_not_found(auth_token):
    non_existent_id = 999999
    headers = {"Authorization": f"Bearer {auth_token}"}

    response = requests.post(
        f"{API_BASE_URL_8085}{ENDPOINTS['create_eco_news']}/{non_existent_id}/like",
        headers=headers
    )
    assert response.status_code == 404, f"Expected 404, got {response.status_code}"


def test_get_eco_news_dislikes_count_bad_request(auth_token):
    invalid_id = "invalid_id"
    headers = {"Authorization": f"Bearer {auth_token}"}

    response = requests.post(
        f"{API_BASE_URL_8085}{ENDPOINTS['create_eco_news']}/{invalid_id}/like",
        headers=headers
    )
    assert response.status_code == 400, f"Expected 400, got {response.status_code}"


def test_get_eco_news_dislikes_negative_id(auth_token):
    negative_id = -1
    headers = {"Authorization": f"Bearer {auth_token}"}

    response = requests.post(
        f"{API_BASE_URL_8085}{ENDPOINTS['create_eco_news']}/{negative_id}/like",
        headers=headers
    )
    assert response.status_code in [400, 404]


def test_get_eco_news_dislikes_zero_id(auth_token):
    zero_id = 0
    headers = {"Authorization": f"Bearer {auth_token}"}

    response = requests.post(
        f"{API_BASE_URL_8085}{ENDPOINTS['create_eco_news']}/{zero_id}/like",
        headers=headers
    )
    assert response.status_code in [400, 404]


@pytest.mark.parametrize("eco_news_id", [1, 2, 3])
def test_get_eco_news_dislikes_various_ids(eco_news_id, auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}

    response = requests.post(
        f"{API_BASE_URL_8085}{ENDPOINTS['create_eco_news']}/{eco_news_id}/like",
        headers=headers
    )
    assert response.status_code in [200, 201, 404]

    if response.status_code in [200, 201]:
        second_response = requests.post(
            f"{API_BASE_URL_8085}{ENDPOINTS['create_eco_news']}/{eco_news_id}/like",
            headers=headers
        )
        assert second_response.status_code in [200, 201]
