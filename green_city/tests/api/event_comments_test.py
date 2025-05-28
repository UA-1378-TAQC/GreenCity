# green_city/tests/api/events/event_comments_test.py
import json
import logging
import pytest
import requests
from jsonschema import validate

from green_city.src.config import API_BASE_URL_8085, ENDPOINTS
from green_city.tests.data.schema.event_comment_schema import (
    EVENT_COMMENT_201,
    EVENT_COMMENT_400,
    EVENT_COMMENT_401,
    EVENT_COMMENT_404,
)

logger = logging.getLogger(__name__)

# ---------------- 201 -----------------
@pytest.mark.api
def test_add_comment_201(auth_token, create_event):
    event_id = create_event["id"]
    url = f"{API_BASE_URL_8085}{ENDPOINTS['event_comments'].format(event_id)}"

    resp = requests.post(
        url,
        headers={"Authorization": auth_token},
        files={"request": (None, json.dumps({"text": "comment from test", "parentComment": 0}))},
    )
    logger.debug("POST %s → %s\nBody: %s", url, resp.status_code, resp.text)

    assert resp.status_code == 201
    validate(instance=resp.json(), schema=EVENT_COMMENT_201)

    assert resp.json()["text"] == "comment from test"


# ---------------- 400 -----------------
@pytest.mark.api
@pytest.mark.parametrize(
    "payload, expected_msgs",
    [
        (
            {"text": "", "parentComment": 0},
            {
                "Text must not be null and must contain at least one non-whitespace character.",
                "length must be between 1 and 8000",
            },
        ),
        (
            {"text": " ", "parentComment": 0},
            {
                "Text must not be null and must contain at least one non-whitespace character.",
            },
        ),
    ],
    ids=["empty_text", "whitespace_text"],
)
def test_add_comment_400(auth_token, create_event, payload, expected_msgs):
    event_id = create_event["id"]
    url = f"{API_BASE_URL_8085}{ENDPOINTS['event_comments'].format(event_id)}"

    resp = requests.post(
        url,
        headers={"Authorization": auth_token},
        files={"request": (None, json.dumps(payload))},
    )
    logger.debug("POST %s → %s\nBody: %s", url, resp.status_code, resp.text)

    assert resp.status_code == 400
    body = resp.json()

    validate(instance=body, schema=EVENT_COMMENT_400)

    returned = {item["message"] for item in body}
    assert expected_msgs.issubset(returned)


# ---------------- 401 -----------------
@pytest.mark.api
def test_add_comment_401_no_auth(create_event):

    event_id = create_event["id"]
    url = f"{API_BASE_URL_8085}{ENDPOINTS['event_comments'].format(event_id)}"

    resp = requests.post(
        url,
        files={"request": (None, json.dumps({"text": "Hello from me!", "parentComment": 0}))},
    )

    assert resp.status_code == 401
    validate(resp.json(), EVENT_COMMENT_401)
    assert resp.json()["error"] == "Unauthorized"


# ---------------- 404 -----------------
@pytest.mark.api
def test_add_comment_404_event_not_found(auth_token, nonexistent_event_id):

    url = f"{API_BASE_URL_8085}{ENDPOINTS['event_comments'].format(nonexistent_event_id)}"

    resp = requests.post(
        url,
        headers={"Authorization": auth_token},
        files={"request": (None, json.dumps({"text": "Hello from me!", "parentComment": 0}))},
    )

    assert resp.status_code == 404
    validate(resp.json(), EVENT_COMMENT_404)
    assert str(nonexistent_event_id) in resp.json()["message"]
