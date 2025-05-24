import pytest
from green_city.src.util.auth_helpers import get_auth_token
from green_city.src.config import API_BASE_URL_8065, API_BASE_URL_8085, ENDPOINTS, TEST_USER_EMAIL, TEST_USER_PASSWORD, CREATOR_USER_EMAIL, CREATOR_USER_PASSWORD

@pytest.fixture(scope="session")
def auth_token():
    return get_auth_token(TEST_USER_EMAIL, TEST_USER_PASSWORD)

@pytest.fixture(scope="session")
def auth_token_second_user():
    return get_auth_token(CREATOR_USER_EMAIL, CREATOR_USER_PASSWORD)

