import random
import pytest
import requests
from green_city.config.config import API_BASE_URL_8085, ENDPOINTS

@pytest.fixture
def nonexistent_event_id():
    for _ in range(3):
        maybe_id = random.randint(10_000_000, 20_000_000)
        url = f"{API_BASE_URL_8085}{ENDPOINTS['event_by_id'].format(maybe_id)}"
        if requests.get(url).status_code == 404:
            return maybe_id
    pytest.skip("Couldn't find out your ID")