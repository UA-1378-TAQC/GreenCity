import pytest
import requests
from src.config import API_URL
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

def test_get_non_existent_news():
    r = requests.get('http://localhost:8085/eco-news/1')
    if r.status_code == 200:
        data = r.json()
        print("Title:", data["title"])
        print("Author name:", data["author"]["name"])
        print("Tags:", ", ".join(data["tags"]))
        print("Content:", data["content"])
    else:
        print(f"Failed to get data. Status code: {r.status_code}")
