import pytest
import requests
from jsonschema import validate, ValidationError

from green_city.config.config import API_BASE_URL_8085, ENDPOINTS
from green_city.config.logging_config import get_logger
from ..data.schema.summary_source_content_schema import schemas_get_request as get_schema
from ..data.test_data.summary_source_content_data import data_get_request as get_data

logger = get_logger(__name__)

get_summary_data = [
    ("8&", ["message"], get_data["400_response_body"], get_schema["summary_schema_message"]),
    ("%25", ["error"], get_data["400_response_body_html"], get_schema["summary_schema_error"]),
    ("1", ["error"], get_data["401_response_body"], get_schema["summary_schema_error"]),
    ("404", ["message"], get_data["404_response_body"], get_schema["summary_schema_message"]),
    ("1", ["content", "source"], get_data["200_response_body"], get_schema["summary_schema_valid_result"])
]


def test_get_summary_success(auth_token, create_news):
    id = create_news
    token_for_use = auth_token
    expected_result = get_summary_data[4]
    get_summary_by_id_testbody(expected_result[2], id, token_for_use, expected_result[3], expected_result[1])


def test_get_summary_not_found(auth_token, create_not_found_news):
    id = create_not_found_news
    token_for_use = auth_token
    expected_result = get_summary_data[3]
    get_summary_by_id_testbody(expected_result[2], id, token_for_use, expected_result[3], expected_result[1])


def test_get_summary_unauthorized(create_news):
    id = create_news
    token_for_use = ''
    expected_result = get_summary_data[2]
    get_summary_by_id_testbody(expected_result[2], id, token_for_use, expected_result[3], expected_result[1])


@pytest.mark.parametrize(
    "eco_news_id, expected_param, expected_response, expected_schema",
    [
        get_summary_data[0],
        get_summary_data[1]
    ]
)
def test_get_summary_bad_response(eco_news_id, expected_param, expected_response, expected_schema, auth_token):
    id = eco_news_id
    token_for_use = auth_token
    get_summary_by_id_testbody(expected_response, id, token_for_use, expected_schema, expected_param)


def get_summary_request(id, token_for_use):
    return requests.get(
        f'{API_BASE_URL_8085}{ENDPOINTS["summary"].format(id)}',
        headers={"Authorization": token_for_use},
    )


def assert_scheme(json_data, response_schema):
    try:
        validate(instance=json_data, schema=response_schema)
    except ValidationError as e:
        pytest.fail(f"Response JSON does not match schema: {e.message}")


def get_response_json(response):
    try:
        return response.json()
    except ValueError:
        pytest.fail("Response is not valid JSON")


def get_summary_by_id_testbody(expected_response, id, token_for_use, expected_schema, expected_param):
    expected_status_code = expected_response.get("status")
    response = get_summary_request(id, token_for_use)
    logger.info(f"Status code: {response.status_code}")
    json_data = get_response_json(response)
    logger.info(f"Response body: {json_data}")
    assert_scheme(json_data, expected_schema)
    assert response.status_code == expected_status_code, f"Expected status code {expected_status_code}, but got {response.status_code}"
    for param in expected_param:
        expected_response_by_param = expected_response.get(param).format(id)
        assert response.json()[
                   param] == expected_response_by_param, f"Expected {param}: {expected_response_by_param} but got {response.json()[param]}"
