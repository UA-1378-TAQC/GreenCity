import requests
from green_city.src.config import API_BASE_URL_8085, ENDPOINTS


def test_add_comment_to_news(auth_token):
    user_id = 1
    data = '{"text": "your test comment here", "parentCommentId": 0}'
    files = {
        'request': (None, data)
    }

    response = requests.post(
        f"{API_BASE_URL_8085}{ENDPOINTS["comments"].format(user_id)}",
        headers={"Authorization": auth_token},
        files=files
    )

    assert response.status_code == 201, "Login is failed"
