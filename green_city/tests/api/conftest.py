import pytest
import requests
import json
from green_city.src.util.auth_helpers import get_auth_token
from green_city.src.config import API_BASE_URL_8065, API_BASE_URL_8085, ENDPOINTS, TEST_USER_EMAIL, TEST_USER_PASSWORD, CREATOR_USER_EMAIL, CREATOR_USER_PASSWORD

@pytest.fixture(scope="session")
def auth_token():
    return get_auth_token(TEST_USER_EMAIL, TEST_USER_PASSWORD)

@pytest.fixture(scope="session")
def auth_token_second_user():
    return get_auth_token(CREATOR_USER_EMAIL, CREATOR_USER_PASSWORD)

@pytest.fixture
def create_comment(auth_token):
    data = '{"text": "{comment text here}", "parentCommentId": 0}'
    files = {'request': (None, data)}
    yield files


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


