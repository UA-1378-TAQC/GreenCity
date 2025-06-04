import requests

from green_city.config.config import API_BASE_URL_8065, ENDPOINTS, SECRET_KEY


def get_auth_token(email: str, password: str) -> str:
    login_data = {
        "email": email,
        "password": password,
        "secretKey": SECRET_KEY
    }
    response = requests.post(f"{API_BASE_URL_8065}{ENDPOINTS['user_login']}", json=login_data)
    assert response.status_code == 200, f"Login failed for {email}"
    token = response.json().get("accessToken")
    assert token is not None, f"Token not found for {email}"
    return f"Bearer {token}"
