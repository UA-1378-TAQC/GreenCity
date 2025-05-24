import green_city.src.util.logging_config
import pytest
import requests
from green_city.src.config import API_BASE_URL_8085, ENDPOINTS
import logging
from jsonschema import validate

logger = logging.getLogger(__name__)

def test_add_to_favorites_success(create_news, auth_token):
    id = create_news
    logger.info(f'Request to add eco-new with id={id} to favorites')
    response = requests.post(
        f'{API_BASE_URL_8085}{ENDPOINTS["favorites"].format(id)}',
        headers={"Authorization": auth_token}
    )
    logger.info(f"Status code: {response.status_code}")
    expected_status_code = 200
    assert response.status_code == expected_status_code, f"Expected status code {expected_status_code}, but got {response.status_code}"
    assert len(response.text)==0, f"Expected response should have be empty, but was {response.json()}"

    logger.info('Request to get all news')
    response = requests.get(
        f"{API_BASE_URL_8085}{ENDPOINTS['all_news']}",
        headers={"Authorization": auth_token}
    )
    logger.info(f"Status code: {response.status_code}")
    data=response.json()
    matching_users = next((entry for entry in data["page"] if entry["id"] == id), None)
    assert matching_users['favorite'] == True, f'Expected "favorite": True, but was {matching_users["favorite"]}'
    
    