import pytest
import requests
from green_city.src.config import API_BASE_URL_8065, ENDPOINTS, CREATOR_USER_EMAIL

@pytest.fixture(scope="function")
def find_user_by_id(auth_token_second_user):
    full_url = f"{API_BASE_URL_8065}{ENDPOINTS['get_user_id_by_email']}"
    headers = {"Authorization": auth_token_second_user}
    params = {"email": CREATOR_USER_EMAIL}
    response = requests.get(full_url, headers=headers, params=params)
    return response.text
