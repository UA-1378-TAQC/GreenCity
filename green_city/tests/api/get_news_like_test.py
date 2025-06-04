import pytest
import requests
from jsonschema import validate

from green_city.config.config import ENDPOINTS, API_BASE_URL_8085
from green_city.tests.data.schema.not_found_schema import not_found_schema


@pytest.mark.parametrize(("event_id", "user_id"),
                         [(-1, 1), (1, -1), (0, 1), (1, 0), (1, 99999999), (99999999, 1)])
def test_get_user_like_on_event_while_unauthorized(event_id, user_id, auth_token):
    endpoint = ENDPOINTS["check_eco_news_user_likes"].format(event_id, user_id)
    url = f"{API_BASE_URL_8085}{endpoint}"
    headers = {"Authorization": auth_token}
    response = requests.get(url, headers=headers)

    assert response.status_code == 404
    validate(instance=response.json(), schema=not_found_schema)