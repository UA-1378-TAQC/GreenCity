import requests
from green_city.src.config import API_URL
from green_city.src.mappers import NewsMapper
from green_city.src.config import ENDPOINTS

def test_get_news():
    response = requests.get(f"{API_URL}/eco-news/1")
    assert response.status_code == 200
    data = response.json()
    assert "title" in data
    assert "author" in data
    assert "tags" in data
    assert "content" in data

def test_get_non_existent_news():
    response = requests.get(f"{API_URL}/eco-news/9999")
    assert response.status_code == 404

def test_get_news():
    response = requests.get(ENDPOINTS["get_news"].format(id=1))
    assert response.status_code == 200
    data = response.json()
    news = NewsMapper.map_news(data)

    assert news["title"] is not None
    assert news["author"] is not None
    assert isinstance(news["tags"], list)
    assert news["content"] is not None
