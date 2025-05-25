import requests
from green_city.src.config import API_BASE_URL_8085, CREATOR_USER_EMAIL, ENDPOINTS

def test_dislike_news(
    news_factory,
    like_news_factory,
    dislike_news_factory,
    auth_token,
    auth_token_second_user,
    user_id_by_email_factory,
    check_like_status_factory
):
    news_id = news_factory(auth_token)

    like_news_factory(news_id, auth_token_second_user)

    user_id = user_id_by_email_factory(auth_token_second_user, CREATOR_USER_EMAIL)
    liked_before = check_like_status_factory(news_id, user_id, auth_token_second_user)

    assert liked_before is True

    response = dislike_news_factory(news_id, auth_token_second_user)
    assert response.status_code == 200, "Failed to dislike news"

    likes_url = f"{API_BASE_URL_8085}{ENDPOINTS['check_eco_news_likes_count'].format(news_id)}"
    dislikes_url = f"{API_BASE_URL_8085}{ENDPOINTS['check_eco_news_dislikes_count'].format(news_id)}"
    headers = {"Authorization": auth_token_second_user}

    likes_response = requests.get(likes_url, headers=headers)
    dislikes_response = requests.get(dislikes_url, headers=headers)

    assert likes_response.status_code == 200
    assert dislikes_response.status_code == 200
    assert likes_response.text == '0'
    assert dislikes_response.text == '1'
