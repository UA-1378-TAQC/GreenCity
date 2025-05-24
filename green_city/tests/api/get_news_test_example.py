import  green_city.src.util.logging_config
import logging
import requests
from green_city.src.config import API_BASE_URL_8085, ENDPOINTS

logger = logging.getLogger(__name__)

def test_get_news(create_news):
    NEWS_ID = create_news
    logger.info(f'Id of news is {NEWS_ID}')
    full_url = f"{API_BASE_URL_8085}{ENDPOINTS['news'].format(NEWS_ID)}"
    response = requests.get(full_url)
    logger.info(f"Status code: {response.status_code}")
    assert response.status_code == 200, "Failed to get news"
    data = response.json()
    assert data.get("id") == NEWS_ID
    assert data.get("title") == "Some OMEGA cool title here!!!", f"Unexpected title: {data.get('title')}"
    assert data.get("author", {}).get("name") == "TestUser", f"Unexpected author: {data.get('author')}"
    assert "News" in data['tags'], f"'Education' not found in tags: {data['tags']}"
    
