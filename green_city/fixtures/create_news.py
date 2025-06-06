import copy
import json

import pytest
import requests

from green_city.config.config import API_BASE_URL_8085, ENDPOINTS
from green_city.data.fixture_dto.create_news_dto import create_news_dto_request


@pytest.fixture(scope="function")
def create_news(auth_token):
    url = f"{API_BASE_URL_8085}{ENDPOINTS['create_eco_news']}"
    dto_request_str = json.dumps(create_news_dto_request)
    files = {'addEcoNewsDtoRequest': (None, dto_request_str), 'image': (None, '')}
    headers = {"Authorization": auth_token}
    response = requests.post(url, headers=headers, files=files)
    news_id = response.json().get("id")
    yield news_id

    delete_url = f"{API_BASE_URL_8085}{ENDPOINTS['delete_eco_news'].format(news_id)}"
    requests.delete(delete_url, headers=headers)


@pytest.fixture
def news_factory():
    created_news = []

    def _create(auth_token):
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
        created_news.append((news_id, auth_token))
        return news_id

    yield _create

    for news_id, token in created_news:
        delete_url = f"{API_BASE_URL_8085}{ENDPOINTS['delete_eco_news'].format(news_id)}"
        headers = {"Authorization": token}
        requests.delete(delete_url, headers=headers)


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
    requests.delete(delete_url, headers=headers)
    yield news_id


@pytest.fixture(scope="function")
def valid_news_payload():
    return copy.deepcopy(create_news_dto_request)
