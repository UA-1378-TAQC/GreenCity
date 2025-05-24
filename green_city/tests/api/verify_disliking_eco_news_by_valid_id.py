import requests
from green_city.src.config import API_BASE_URL_8085, ENDPOINTS

def test_dislike_news(create_news,auth_token_second_user):
    news_id = create_news
    #todo like news here
    full_url = f"{API_BASE_URL_8085}{ENDPOINTS['dislike_eco_news'].format(news_id)}"
    headers = {
        "Authorization": auth_token_second_user
    }

    response = requests.post(full_url, headers=headers)

    assert response.status_code == 200, "Failed to dislike selected news"
