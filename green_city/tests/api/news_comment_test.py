import requests
from green_city.src.config import API_BASE_URL_8085, ENDPOINTS

def test_add_comment_to_news(auth_token, create_comment):
    news_id = 1

    files = create_comment

    response = requests.post(
        f"{API_BASE_URL_8085}{ENDPOINTS["comments"].format(news_id)}",
        headers={"Authorization": auth_token},
        files=files
    )

    comment_id = response.json().get("id")
    assert response.status_code == 201, "Login is failed"
