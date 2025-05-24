import requests
from jsonschema import validate
from green_city.src.config import API_BASE_URL_8085, ENDPOINTS
from green_city.tests.api.fixtures.create_news import create_news
from green_city.tests.test_data.schema.recommended_news_schema import recommended_news_schema

def test_get_recommended_news(create_news):
    DEFAULT_NEWS_ID = 1
    news_id = create_news
    full_url = f"{API_BASE_URL_8085}{ENDPOINTS['recommended_eco_news'].format(DEFAULT_NEWS_ID)}"
    response = requests.get(full_url)

    assert response.status_code == 200, "Failed to get news"
    data = response.json()

    validate(instance=data, schema=recommended_news_schema)

    assert any(news.get("id") == news_id for news in data), f"News with ID {news_id} not found in response: {[n.get('id') for n in data]}"
    assert any(news.get("title") == "Some OMEGA cool title here!!!" for news in data), \
        f"'Some OMEGA cool title here!!!' not found in titles: {[n.get('title') for n in data]}"
    assert any("news" in [tag.lower() for tag in news.get("tags", [])] for news in data), \
        f"'news' not found in tags: {[n.get('tags') for n in data]}"
