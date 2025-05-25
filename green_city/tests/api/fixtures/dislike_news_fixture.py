import pytest
import requests
from green_city.src.config import API_BASE_URL_8085, ENDPOINTS

@pytest.fixture
def dislike_news_factory():
    def _dislike(news_id, auth_token):
        full_url = f"{API_BASE_URL_8085}{ENDPOINTS['dislike_eco_news'].format(news_id)}"
        headers = {"Authorization": auth_token}
        response = requests.post(full_url, headers=headers)
        assert response.status_code == 200, "Failed to dislike news"
    return _dislike
