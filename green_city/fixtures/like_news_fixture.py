import pytest
import requests

from green_city.config.config import API_BASE_URL_8085, ENDPOINTS


@pytest.fixture(scope="function")
def like_news(create_news, auth_token_second_user):
    news_id = create_news
    full_url = f"{API_BASE_URL_8085}{ENDPOINTS['like_eco_news'].format(news_id)}"
    headers = {"Authorization": auth_token_second_user}
    response = requests.post(full_url, headers=headers)

    assert response.status_code == 200, "Failed to like selected news"


@pytest.fixture
def like_news_factory():
    def _like(news_id, auth_token):
        full_url = f"{API_BASE_URL_8085}{ENDPOINTS['like_eco_news'].format(news_id)}"
        headers = {"Authorization": auth_token}
        response = requests.post(full_url, headers=headers)
        assert response.status_code == 200, "Failed to like news"

    return _like
