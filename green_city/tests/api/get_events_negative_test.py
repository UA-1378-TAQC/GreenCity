import logging
import pytest
import requests

from green_city.src.config import API_BASE_URL_8085

logger = logging.getLogger(__name__)

@pytest.mark.api
@pytest.mark.negative
@pytest.mark.parametrize(
    "path, expected_status, expected_message",
    [
        ("/events/0",       404, "Event hasn't been found"),
        ("/events?page=-1", 400, "page must be a positive number"),
        ("/events?size=-1", 400, "size must be a positive number"),
    ],
    ids=[
        "id=0 -> 404",
        "page=-1 -> 400",
        "size=-1 -> 400",
    ]
)
def test_get_events_negative(path, expected_status, expected_message):
    url = f"{API_BASE_URL_8085}{path}"
    response = requests.get(url)

    logger.debug("URL %s → %s, body: %s", url, response.status_code, response.text)

    assert response.status_code == expected_status
    body = response.json()
    assert expected_message in body.get("message", ""), (
        f"Expected '{expected_message}' but got it: {body}"
    )
