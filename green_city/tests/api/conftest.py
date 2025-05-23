import pytest
import requests
from green_city.src.config import TEST_USER_EMAIL, TEST_USER_PASSWORD, SECRET_KEY
from green_city.src.config import API_BASE_URL_8065, ENDPOINTS

@pytest.fixture(scope="session")
def login_token():
    login_data = {
        "email": TEST_USER_EMAIL,
        "password": TEST_USER_PASSWORD,
        "secretKey": SECRET_KEY
    }
    response = requests.post(f"{API_BASE_URL_8065}{ENDPOINTS['user_login']}", json=login_data)
    assert response.status_code == 200, "Login failed"
    token = response.json().get("accessToken")
    assert token is not None, "Token not found in response"
    return token

@pytest.fixture
def auth_token(login_token):
    return f"Bearer {login_token}"


@pytest.fixture
def create_comment(auth_token):
    print("▶ Створення коментаря...")

    print("🗑 Видалення коментаря...")


