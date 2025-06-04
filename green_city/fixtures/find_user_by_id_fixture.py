import pytest
import requests

from green_city.config.config import API_BASE_URL_8065, ENDPOINTS


@pytest.fixture
def user_id_by_email_factory():
    def _get_user_id(auth_token, email):
        full_url = f"{API_BASE_URL_8065}{ENDPOINTS['get_user_id_by_email']}"
        headers = {"Authorization": auth_token}
        params = {"email": email}
        response = requests.get(full_url, headers=headers, params=params)
        assert response.status_code == 200, "Failed to get user ID"
        return response.text

    return _get_user_id
