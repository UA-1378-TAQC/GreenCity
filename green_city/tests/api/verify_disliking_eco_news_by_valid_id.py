import requests
from green_city.src.config import API_BASE_URL_8085, ENDPOINTS

def test_dislike_news(create_news,auth_token):
    news_id = create_news
    #switch to another user here
    full_url = f"{API_BASE_URL_8085}{ENDPOINTS['dislike_eco_news'].format(news_id)}"
    headers = {
        "Authorization": auth_token
    }

    response = requests.post(full_url, headers=headers)

    assert response.status_code == 200, "Failed to dislike selected news"
    data = response.json()
    assert any(news.get("id") == news_id for news in data), f"News with ID {news_id} not found in response: {[n.get('id') for n in data]}"
