def test_dislike_news_unauthorized(news_factory, dislike_news_factory, auth_token):
    news_id = news_factory(auth_token)

    response = dislike_news_factory(news_id, auth_token=None)
    json_body = response.json()
    assert response.status_code == 401
    assert json_body["error"] == "Unauthorized"
