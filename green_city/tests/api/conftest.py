import pytest
import requests
import json
from green_city.src.util.auth_helpers import get_auth_token
from green_city.src.config import TEST_USER_EMAIL, TEST_USER_PASSWORD, CREATOR_USER_EMAIL, CREATOR_USER_PASSWORD, API_BASE_URL_8085, ENDPOINTS

@pytest.fixture(scope="session")
def auth_token():
    return get_auth_token(TEST_USER_EMAIL, TEST_USER_PASSWORD)

@pytest.fixture(scope="session")
def auth_token_second_user():
    return get_auth_token(CREATOR_USER_EMAIL, CREATOR_USER_PASSWORD)

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
