import pytest
from green_city.src.config import TEST_USER_EMAIL, TEST_USER_PASSWORD, SECRET_KEY

@pytest.fixture
def login_payload():
    return {
        "email": TEST_USER_EMAIL,
        "password": TEST_USER_PASSWORD,
        "secretKey": SECRET_KEY
    }
