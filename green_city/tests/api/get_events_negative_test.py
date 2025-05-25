import logging
import pytest
import requests
from jsonschema import validate

from green_city.src.config import API_BASE_URL_8085
from green_city.tests.data.schema.event_schema import EVENT_400_SCHEMA, EVENT_404_SCHEMA

logger = logging.getLogger(__name__)

@pytest.mark.api
@pytest.mark.negative
@pytest.mark.parametrize(
    "path, expected_status, schema, expected_fragment",
    [
        ("/events/0",        404, EVENT_404_SCHEMA,  "Event hasn't been found"),
        ("/events?page=-1",  400, EVENT_400_SCHEMA,  "page must be a positive"),
        ("/events?size=-1",  400, EVENT_400_SCHEMA,  "size must be a positive"),
    ],
    ids=["id=0-404", "page=-1-400", "size=-1-400"],
)
def test_get_events_negative(path, expected_status, schema, expected_fragment):

    url = f"{API_BASE_URL_8085}{path}"
    resp = requests.get(url)

    logger.debug("GET %s → %s\nBody: %s", url, resp.status_code, resp.text)

    assert resp.status_code == expected_status
    validate(resp.json(), schema)

    assert expected_fragment in resp.json().get("message", "")
