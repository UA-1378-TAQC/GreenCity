import pytest
import requests

from green_city.src.config import ENDPOINTS, API_BASE_URL_8085

@pytest.fixture(scope='function')
def like_news(create_news, auth_token_second_user):
    endpoint = ENDPOINTS['like_eco_news'].format(create_news)
    url = f"{API_BASE_URL_8085}{endpoint}"
    headers = {'Authorization': auth_token_second_user}
    response = requests.post(url, headers=headers)
    return response