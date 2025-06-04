import pytest
import requests
from green_city.config.config import API_BASE_URL_8085, ENDPOINTS
from green_city.tests.data.test_data.eco_news_invalid_page_values import eco_news_invalid_page_values

@pytest.mark.parametrize("page_param, expected_status, expected_message", eco_news_invalid_page_values)
def test_get_eco_news_invalid_pages(auth_token, page_param, expected_status, expected_message):
    url = f"{API_BASE_URL_8085}{ENDPOINTS['get_eco_news']}"
    headers = {"Authorization": auth_token}
    params = {"page": page_param}

    response = requests.get(url, headers=headers, params=params)

    assert response.status_code == expected_status, f"Unexpected status for page='{page_param}'"

    try:
        error_message = response.json().get("message", "")
    except ValueError:
        error_message = response.text

    assert expected_message in error_message, f"Expected message to contain '{expected_message}', got '{error_message}'"
