import pytest
import requests
from green_city.src.config import API_BASE_URL_8065, ENDPOINTS

def test_perform_simple_login(login_payload):
    response = requests.post(
        f"{API_BASE_URL_8065}{ENDPOINTS['user_login']}",
        json=login_payload,
        headers={"Content-Type": "application/json"}
    )
    assert response.status_code == 200, "Login is failed"
    access_token = response.json().get("accessToken")
    assert access_token is not None, "Token is not obtained"
