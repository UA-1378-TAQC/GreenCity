import json

import pytest
import requests
from green_city.src.config import TEST_USER_EMAIL, TEST_USER_PASSWORD, SECRET_KEY
from green_city.src.config import API_BASE_URL_8085, API_BASE_URL_8065, ENDPOINTS

@pytest.fixture(scope="session")
def login_token():
    login_data = {
        "email": TEST_USER_EMAIL,
        "password": TEST_USER_PASSWORD,
        "secretKey": SECRET_KEY
    }
    response = requests.post(f"{API_BASE_URL_8065}{ENDPOINTS['user_login']}", json=login_data)
    assert response.status_code == 200, "Login failed"
    token = response.json().get("accessToken")
    assert token is not None, "Token not found in response"
    return token

@pytest.fixture
def auth_token(login_token):
    return f"Bearer {login_token}"


@pytest.fixture
def create_comment(auth_token):
    print("Comment creation...")
    data = '{"text": "{comment text here}", "parentCommentId": 0}'
    files = {'request': (None, data)}

    yield files
    print("Place comment deleted logic below")

@pytest.fixture
def test_event_json_schema(auth_token):
    return {"type": "object",
            "required": [
                "id", "title", "organizer", "creationDate", "description",
                "dates", "tags", "titleImage", "additionalImages", "type",
                "isRelevant", "likes", "dislikes", "countComments", "eventRate",
                "currentUserGrade", "open", "isSubscribed", "isFavorite", "isOrganizedByFriend"
            ],
            "properties": {
                "id": {"type": "integer"},
                "title": {"type": "string"},
                "organizer": {
                    "type": "object",
                    "required": ["id", "name", "organizerRating", "email"],
                    "properties": {
                        "id": {"type": "integer"},
                        "name": {"type": "string"},
                        "organizerRating": {"type": ["number", "null"]},
                        "email": {"type": "string", "format": "email"}
                    }
                },
                "creationDate": {"type": "string", "format": "date"},
                "description": {"type": "string"},
                "dates": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "required": ["startDate", "finishDate", "onlineLink"],
                        "properties": {
                            "startDate": {"type": "string", "format": "date-time"},
                            "finishDate": {"type": "string", "format": "date-time"},
                            "onlineLink": {"type": "string", "format": "uri"},
                            "id": {"type": ["integer", "null"]},
                            "event": {"type": ["string", "null"]},
                            "coordinates": {"type": ["object", "null"]}
                        }
                    }
                },
                "tags": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "required": ["id", "nameUa", "nameEn"],
                        "properties": {
                            "id": {"type": "integer"},
                            "nameUa": {"type": "string"},
                            "nameEn": {"type": "string"}
                        }
                    }
                },
                "titleImage": {"type": "string"},
                "additionalImages": {"type": "array"},
                "type": {"type": "string", "enum": ["ONLINE", "OFFLINE", "MIXED"]},
                "isRelevant": {"type": "boolean"},
                "likes": {"type": "integer"},
                "dislikes": {"type": "integer"},
                "countComments": {"type": "integer"},
                "eventRate": {"type": "number"},
                "currentUserGrade": {"type": ["number", "null"]},
                "open": {"type": "boolean"},
                "isSubscribed": {"type": "boolean"},
                "isFavorite": {"type": "boolean"},
                "isOrganizedByFriend": {"type": "boolean"}
            }
            }

@pytest.fixture
def test_event_json(auth_token):
    return {
        "title":"string",
        "description":"TEST CASE DESCRIPTION",
        "open":True,
        "datesLocations":[
            {
                "startDate":"2033-05-27T15:00:00Z",
                "finishDate":"2033-05-27T17:00:00Z",
                "onlineLink": "http://test.example.com",
            }
        ],
        "tags":["Social"]
    }

@pytest.fixture
def create_event(auth_token, test_event_json):

    files = {
        'addEventDtoRequest': (None, json.dumps(test_event_json), 'application/json'),
        'images': (None, '')
    }

    response = requests.post(
        f"{API_BASE_URL_8085}/events",
        headers={
            "Authorization": auth_token,
        },
        files = files
    )

    assert response.status_code == 201
    return response.json().get("id")

@pytest.fixture
def create_and_cleanup_event(create_event, auth_token):
    event_id = create_event
    yield event_id

    response = requests.delete(
        f"{API_BASE_URL_8085}/events/{event_id}",
        headers={"Authorization": auth_token}
    )
    assert response.status_code in [200, 204]
