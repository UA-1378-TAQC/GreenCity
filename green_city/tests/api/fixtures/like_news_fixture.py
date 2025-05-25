import pytest
import requests
from green_city.src.config import API_BASE_URL_8085, ENDPOINTS

@pytest.fixture(scope="function")
def like_news(create_news):
    news_id = create_news
    full_url = f"{API_BASE_URL_8085}{ENDPOINTS['like_eco_news'].format(news_id)}"
    headers = {
        "Authorization": auth_token_second_user
    }
    response = requests.post(full_url, headers=headers)
    assert response.status_code == 200, "Failed to like selected news"
