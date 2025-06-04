import os

from dotenv import load_dotenv

load_dotenv()

API_BASE_URL_8065 = os.getenv("API_BASE_URL_8065", "http://localhost:8065/")
API_BASE_URL_8085 = os.getenv("API_BASE_URL_8085", "http://localhost:8085/")

TEST_USER_EMAIL = os.getenv("TEST_USER_EMAIL")
TEST_USER_PASSWORD = os.getenv("TEST_USER_PASSWORD")

CREATOR_USER_EMAIL = os.getenv("CREATOR_USER_EMAIL")
CREATOR_USER_PASSWORD = os.getenv("CREATOR_USER_PASSWORD")

SECRET_KEY = os.getenv("SECRET_KEY")

ENDPOINTS = {
    'check_eco_news_dislikes_count': '/eco-news/{0}/dislikes/count',
    'check_eco_news_likes_count': '/eco-news/{0}/likes/count',
    'comments': '/eco-news/{0}/comments',
    "summary": "/eco-news/{0}/summary",
    'count_eco_news': '/eco-news/count',
    'create_eco_news': '/eco-news',
    'delete_eco_news': '/eco-news/{0}',
    'delete_events': '/events/{0}',
    'favorites': '/eco-news/{0}/favorites',
    'all_news': '/eco-news',
    'dislike_eco_news': '/eco-news/{0}/dislikes',
    'event_by_id': '/events/{0}',
    'event_comments': '/events/{0}/comments',
    'events': '/events',
    'favorites': '/eco-news/{0}/favorites',
    'get_eco_news': '/eco-news',
    'get_user_id_by_email': '/user/findIdByEmail',
    'is_user_liked_eco_news': '/eco-news/{0}/likes/{1}',
    'like_eco_news': '/eco-news/{0}/likes',
    'news': '/eco-news/{0}',
    'news_recommended': '/eco-news/{0}/recommended',
    'recommended_eco_news': '/eco-news/{0}/recommended',
    'user_login': '/api/testers/sign-in'
}
