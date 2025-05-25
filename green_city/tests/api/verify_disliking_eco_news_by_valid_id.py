import requests
from green_city.src.config import API_BASE_URL_8085, ENDPOINTS

def test_dislike_news(create_news,auth_token_second_user, is_user_liked_news):
    news_id = create_news

    full_url = f"{API_BASE_URL_8085}{ENDPOINTS['check_eco_news_likes_count'].format(news_id)}"
    headers = {
        "Authorization": auth_token_second_user
    }

    response = requests.get(full_url, headers=headers)
    likes_count = response.text
    assert response.status_code == 200, "The news like count is incorrect"

    full_url = f"{API_BASE_URL_8085}{ENDPOINTS['dislike_eco_news'].format(news_id)}"
    headers = {
        "Authorization": auth_token_second_user
    }

    response = requests.post(full_url, headers=headers)
    assert response.status_code == 200, "Failed to dislike selected news"

    full_url = f"{API_BASE_URL_8085}{ENDPOINTS['check_eco_news_dislikes_count'].format(news_id)}"
    headers = {
        "Authorization": auth_token_second_user
    }

    response = requests.get(full_url, headers=headers)
    dislikes_count = response.text
    assert response.status_code == 200, "The news count is incorrect"
    assert likes_count == '0', "The news like count is incorrect"
    assert dislikes_count == '1', "The news dis/like count is incorrect"
