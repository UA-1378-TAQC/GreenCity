# Configuration file for API settings
API_URL = "http://localhost:8085"

ENDPOINTS = {
    "get_news": f"{API_URL}/eco-news/{{id}}",
    "get_all_news": f"{API_URL}/eco-news",
}
