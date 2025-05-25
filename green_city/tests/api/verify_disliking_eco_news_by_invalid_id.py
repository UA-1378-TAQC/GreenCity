import pytest
from green_city.tests.data.test_data.recommended_news_invalid_ids import recommended_news_invalid_ids

@pytest.mark.parametrize("eco_news_id, expected_status, expected_message", recommended_news_invalid_ids)
def test_dislike_news(
        dislike_news_factory,
        auth_token_second_user
):
    news_id = -1

    response = dislike_news_factory(news_id, auth_token_second_user)

    assert response.status_code == 400
