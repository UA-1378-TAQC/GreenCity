import pytest

from green_city.api.auth_helpers import get_auth_token
from green_city.config.config import TEST_USER_EMAIL, TEST_USER_PASSWORD, CREATOR_USER_EMAIL, CREATOR_USER_PASSWORD


@pytest.fixture(scope="session")
def auth_token():
    return get_auth_token(TEST_USER_EMAIL, TEST_USER_PASSWORD)


@pytest.fixture(scope="session")
def auth_token_second_user():
    return get_auth_token(CREATOR_USER_EMAIL, CREATOR_USER_PASSWORD)
