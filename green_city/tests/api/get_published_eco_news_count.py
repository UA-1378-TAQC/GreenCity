import pytest
import requests
from green_city.src.config import API_BASE_URL_8085, ENDPOINTS
from jsonschema import validate
from ..data.schema.get_published_eco_news_count_schema import TAGS_SCHEMA, TAGS_ERROR_MESSAGE_SCHEMA
import green_city.src.util.logging_config
import logging



