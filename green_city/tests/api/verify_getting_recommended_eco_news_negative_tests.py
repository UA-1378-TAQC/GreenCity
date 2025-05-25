import pytest
import requests
from green_city.src.config import API_BASE_URL_8085, ENDPOINTS

@pytest.mark.parametrize("eco_news_id, expected_status, expected_message", [
    ("abc", 400, "Wrong ecoNewsId. Should be 'Long'"),
    ("-42", 400, "Eco new doesn't exist by this id: -42"),
    ("", 400, "")
])
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
