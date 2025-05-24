import pytest
from green_city.src.util.auth_helpers import get_auth_token
from green_city.src.config import TEST_USER_EMAIL, TEST_USER_PASSWORD, CREATOR_USER_EMAIL, CREATOR_USER_PASSWORD

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


