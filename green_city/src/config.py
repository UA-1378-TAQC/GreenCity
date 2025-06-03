import os
from dotenv import load_dotenv

load_dotenv()

API_BASE_URL_8065 = os.getenv("API_BASE_URL_8065")
API_BASE_URL_8085 = os.getenv("API_BASE_URL_8085")

ENDPOINTS = {
    "user_login": "/api/testers/sign-in",
    "news": "/eco-news/{0}",
    "comments": "/eco-news/{0}/comments",
    "create_eco_news": "/eco-news",
    "delete_eco_news":"/eco-news/{0}",
    "dislike_eco_news": "/eco-news/{0}/dislikes",
    "like_eco_news": "/eco-news/{0}/likes",
    "get_user_id_by_email": "/user/findIdByEmail",
    "is_user_liked_eco_news": "/eco-news/{0}/likes/{1}",
    "check_eco_news_likes_count": "/eco-news/{0}/likes/count",
    "check_eco_news_dislikes_count": "/eco-news/{0}/dislikes/count",
    "news_recommended": "/eco-news/{0}/recommended"
}

TEST_USER_EMAIL = os.getenv("TEST_USER_EMAIL")
TEST_USER_PASSWORD = os.getenv("TEST_USER_PASSWORD")
CREATOR_USER_EMAIL= os.getenv("CREATOR_USER_EMAIL")
CREATOR_USER_PASSWORD= os.getenv("CREATOR_USER_PASSWORD")
SECRET_KEY = os.getenv("SECRET_KEY")
