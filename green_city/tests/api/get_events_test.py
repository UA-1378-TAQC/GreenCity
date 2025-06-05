import logging
import pytest
import requests

from green_city.config.config import API_BASE_URL_8085, ENDPOINTS
from green_city.tests.data.schema.event_schema import EVENT_SCHEMA, EVENT_PAGE_SCHEMA
from jsonschema import validate

logger = logging.getLogger(__name__)

@pytest.mark.api
def test_get_all_events_200(create_event):
    url = f"{API_BASE_URL_8085}{ENDPOINTS['events']}"
    resp = requests.get(url)

    logger.debug("Status %s, body len: %s", resp.status_code, len(resp.text))
    assert resp.status_code == 200

    validate(resp.json(), EVENT_PAGE_SCHEMA)

    ids = [item["id"] for item in resp.json()["page"]]
    assert create_event["id"] in ids, "Created event not found on /events page"

@pytest.mark.api
def test_get_event_by_id_200(create_event):
    event_id = create_event["id"]
    url = f"{API_BASE_URL_8085}{ENDPOINTS['event_by_id'].format(event_id)}"
    resp = requests.get(url)

    logger.debug("Status %s, body: %s", resp.status_code, resp.text)
    assert resp.status_code == 200

    validate(resp.json(), EVENT_SCHEMA)
    assert resp.json()["id"] == event_id
