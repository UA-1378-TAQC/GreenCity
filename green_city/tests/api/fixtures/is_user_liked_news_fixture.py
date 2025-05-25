import pytest
import requests
from green_city.src.config import API_BASE_URL_8085, ENDPOINTS

@pytest.fixture(scope="function")
def is_user_liked_news(auth_token_second_user,create_news, find_user_by_id):
    news_id = create_news
    user_id = find_user_by_id
    full_url = f"{API_BASE_URL_8085}{ENDPOINTS['is_user_liked_eco_news'].format(news_id,user_id)}"
    headers = {"Authorization": auth_token_second_user}
    response = requests.get(full_url, headers=headers)

    assert response.status_code == 200, "The news wasn't liked by user"

@pytest.fixture
def check_like_status_factory():
    def _check(news_id, user_id, auth_token):
        full_url = f"{API_BASE_URL_8085}{ENDPOINTS['is_user_liked_eco_news'].format(news_id, user_id)}"
        headers = {"Authorization": auth_token}
        response = requests.get(full_url, headers=headers)
        assert response.status_code == 200, "Failed to check like status"
        return response.json()
    return _check
