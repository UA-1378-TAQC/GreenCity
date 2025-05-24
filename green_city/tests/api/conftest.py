import pytest
import requests
import json
from green_city.src.config import TEST_USER_EMAIL, TEST_USER_PASSWORD, SECRET_KEY
from green_city.src.config import API_BASE_URL_8065, API_BASE_URL_8085, ENDPOINTS

@pytest.fixture(scope="session")
def login_token():
    login_data = {
        "email": TEST_USER_EMAIL,
        "password": TEST_USER_PASSWORD,
        "secretKey": SECRET_KEY
    }
    response = requests.post(f"{API_BASE_URL_8065}{ENDPOINTS['user_login']}", json=login_data)
    assert response.status_code == 200, "Login failed"
    token = response.json().get("accessToken")
    assert token is not None, "Token not found in response"
    return token

@pytest.fixture
def auth_token(login_token):
    return f"Bearer {login_token}"


@pytest.fixture
def create_comment(auth_token):
    print("Comment creation...")
    data = '{"text": "{comment text here}", "parentCommentId": 0}'
    files = {'request': (None, data)}

    yield files
    print("Place comment deleted logic below")


@pytest.fixture(scope="function")
def create_news(auth_token):
    url = f"{API_BASE_URL_8085}{ENDPOINTS['create_eco_news']}"

    dto_request = {
        "image": "string",
        "source": "https://example.org/",
        "shortInfo": "string",
        "title": "Some OMEGA cool title here!!!",
        "text": "Some cool text here!!!",
        "tags": ["news"],
        "titleTranslation": {
            "content": "string",
            "languageCode": "string"
        },
        "textTranslation": {
            "content": "string",
            "languageCode": "string"
        }
    }

    dto_request_str = json.dumps(dto_request)

    files = {
        'addEcoNewsDtoRequest': (None, dto_request_str),
        'image': (None, '')
    }

    headers = {
        "Authorization": auth_token
    }

    response = requests.post(url, headers=headers, files=files)

    news_id = response.json().get("id")
    yield news_id

    delete_url = f"{API_BASE_URL_8085}{ENDPOINTS['delete_eco_news'].format(news_id)}"
    del_response = requests.delete(delete_url, headers=headers)
    assert del_response.status_code == 200, "Failed to delete news"
