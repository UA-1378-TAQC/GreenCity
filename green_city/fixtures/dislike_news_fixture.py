import pytest
import requests

from green_city.config.config import API_BASE_URL_8085, ENDPOINTS


@pytest.fixture
def dislike_news_factory():
    def _dislike(news_id, auth_token):
        full_url = f"{API_BASE_URL_8085}{ENDPOINTS['dislike_eco_news'].format(news_id)}"
        headers = {"Authorization": auth_token}
        return requests.post(full_url, headers=headers)

    return _dislike
