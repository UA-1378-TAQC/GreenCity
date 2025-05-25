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

    "events": "/events",
    "event_by_id": "/events/{0}"
}

TEST_USER_EMAIL = os.getenv("TEST_USER_EMAIL")
TEST_USER_PASSWORD = os.getenv("TEST_USER_PASSWORD")
CREATOR_USER_EMAIL= os.getenv("CREATOR_USER_EMAIL")
CREATOR_USER_PASSWORD= os.getenv("CREATOR_USER_PASSWORD")
SECRET_KEY = os.getenv("SECRET_KEY")
