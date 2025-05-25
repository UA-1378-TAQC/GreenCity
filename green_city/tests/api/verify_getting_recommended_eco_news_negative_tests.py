import pytest
import requests
from green_city.src.config import API_BASE_URL_8085, ENDPOINTS
from green_city.tests.data.test_data.recommended_news_invalid_ids import recommended_news_invalid_ids


@pytest.mark.parametrize("eco_news_id, expected_status, expected_message", recommended_news_invalid_ids)
def test_get_recommended_news_invalid_ids(auth_token, eco_news_id, expected_status, expected_message):
    url = f"{API_BASE_URL_8085}{ENDPOINTS['news_recommended'].format(eco_news_id)}"
    headers = {"Authorization": auth_token}

    response = requests.get(url, headers=headers)

    assert response.status_code == expected_status, f"Unexpected status for ID '{eco_news_id}'"

    try:
        error_message = response.json().get("message", "")
    except ValueError:
        error_message = response.text

    assert expected_message in error_message, f"Expected '{expected_message}', got '{error_message}'"
