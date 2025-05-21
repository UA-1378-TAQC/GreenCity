import requests
from src.config import API_URL
class APIClient:
    def get_news(self, news_id):
        response = requests.get(f"{API_URL}/eco-news/{news_id}")
        return response
    def get_all_news(self):
        response = requests.get(f"{API_URL}/eco-news")
        return response
