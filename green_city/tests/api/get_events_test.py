import logging
import pytest
import requests

from green_city.src.config import API_BASE_URL_8085, ENDPOINTS

logger = logging.getLogger(__name__)

@pytest.mark.api
def test_get_all_events_status_200():
    url = f"{API_BASE_URL_8085}{ENDPOINTS['events']}"
    response = requests.get(url)

    logger.debug("Status %s, body: %s", response.status_code, response.text)
    assert response.status_code == 200
    assert "page" in response.json(), "'page' key is missing from the response"

@pytest.mark.api
@pytest.mark.parametrize("event_id", [1, 2, 3])
def test_get_event_by_id_status_200(event_id):
    url = f"{API_BASE_URL_8085}{ENDPOINTS['event_by_id'].format(event_id)}"
    response = requests.get(url)

    logger.debug("Status %s, body: %s", response.status_code, response.text)
    assert response.status_code == 200
    body = response.json()
    assert body["id"] == event_id
    assert body["title"], "title must not be empty"
