import requests
from green_city.config.config import API_BASE_URL_8085, CREATOR_USER_EMAIL, ENDPOINTS

def test_like_news(
    news_factory,
    auth_token,
    auth_token_second_user,
    user_id_by_email_factory,
    like_news_factory,
    check_like_status_factory
):
    news_id = news_factory(auth_token)

    like_news_factory(news_id, auth_token_second_user)

    user_id = user_id_by_email_factory(auth_token_second_user, CREATOR_USER_EMAIL)

    liked_before = check_like_status_factory(news_id, user_id, auth_token_second_user)
    assert liked_before is True, "News should be liked, but it's not."

    likes_url = f"{API_BASE_URL_8085}{ENDPOINTS['check_eco_news_likes_count'].format(news_id)}"
    headers = {"Authorization": auth_token_second_user}

    likes_response = requests.get(likes_url, headers=headers)

    assert likes_response.status_code == 200
    assert likes_response.text == '1', f"Expected 1 like, got {likes_response.text}"
