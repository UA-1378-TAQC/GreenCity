import pytest
import requests
from jsonschema import validate

from green_city.src.config import ENDPOINTS, API_BASE_URL_8085
from green_city.tests.data.schema.get_news_likes_unauthorized_schema import unauthorized_schema


@pytest.mark.parametrize(("event_id", "user_id"),
                         [(1, 1), (1, "!"), ("!", 1), (-1, 1), (1, -1)])
def test_get_user_like_on_event_while_unauthorized(event_id, user_id, like_news):
    like_response = like_news
    assert like_response.status_code == 200

    endpoint = ENDPOINTS["check_eco_news_user_likes"].format(event_id, user_id)
    url = f"{API_BASE_URL_8085}{endpoint}"
    headers = {"accept": "*/*"}
    response = requests.get(url, headers=headers)

    assert response.status_code == 401
    validate(instance=response.json(), schema=unauthorized_schema)