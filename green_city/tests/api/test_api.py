import requests
from green_city.src.config import API_URL, ENDPOINTS
from green_city.src.mappers import NewsMapper

def test_get_news():
    full_url = f"{API_URL}{ENDPOINTS['get_news'].format(id=1)}"
    response = requests.get(full_url)
    assert response.status_code == 200
    data = response.json()
    news = NewsMapper.map_news(data)

    assert news["title"] is not None
    assert news["author"] is not None
    assert news["content"] is not None
