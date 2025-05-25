import pytest
import requests
import json
from green_city.src.config import API_BASE_URL_8085, ENDPOINTS
from ...data.fixture_dto.create_news_dto import create_news_dto_request

@pytest.fixture(scope="function")
def create_news(auth_token):
    url = f"{API_BASE_URL_8085}{ENDPOINTS['create_eco_news']}"
    dto_request_str = json.dumps(create_news_dto_request)
    files = {'addEcoNewsDtoRequest': (None, dto_request_str),'image': (None, '')}
    headers = {"Authorization": auth_token}
    response = requests.post(url, headers=headers, files=files)
    news_id = response.json().get("id")
    yield news_id

    delete_url = f"{API_BASE_URL_8085}{ENDPOINTS['delete_eco_news'].format(news_id)}"
    del_response = requests.delete(delete_url, headers=headers)

    assert del_response.status_code == 200, "Failed to delete news"

@pytest.fixture(scope="function")
def create_not_found_news(auth_token):
    url = f"{API_BASE_URL_8085}{ENDPOINTS['create_eco_news']}"
    dto_request_str = json.dumps(create_news_dto_request)
    files = {
        'addEcoNewsDtoRequest': (None, dto_request_str),
        'image': (None, '')
    }
    headers = {
        "Authorization": auth_token
    }
    response = requests.post(url, headers=headers, files=files)
    news_id = response.json().get("id")
    delete_url = f"{API_BASE_URL_8085}{ENDPOINTS['delete_eco_news'].format(news_id)}"
    del_response = requests.delete(delete_url, headers=headers)
    assert del_response.status_code == 200, "Failed to delete news"
    yield news_id

