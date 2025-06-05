import pytest

from green_city.tests.data.test_data.recommended_news_invalid_ids import recommended_news_invalid_ids

invalid_ids_only = [(eco_news_id,) for eco_news_id, _, _ in recommended_news_invalid_ids]


@pytest.mark.parametrize("eco_news_id", invalid_ids_only)
def test_dislike_news(
        dislike_news_factory,
        auth_token_second_user,
        eco_news_id
):
    response = dislike_news_factory(eco_news_id, auth_token_second_user)

    assert response.status_code == 400
